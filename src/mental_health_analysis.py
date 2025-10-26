"""
Student Mental Health Analysis - Main Analysis Script
Analyzes relationships between campus environment, academic expectations, and mental health
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import pearsonr, ttest_ind, f_oneway
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Configuration
FIGURE_SIZE = (20, 12)
DPI = 100
RANDOM_SEED = 42

def load_data(filepath=None):
    """
    Load dataset from CSV or generate sample data
    """
    if filepath:
        try:
            df = pd.read_csv(filepath)
            print(f"✓ Loaded data from {filepath}")
            print(f"  Shape: {df.shape}")
            return df
        except FileNotFoundError:
            print(f"✗ File not found: {filepath}")
            print("  Generating sample data instead...")
    
    # Generate sample data
    print("\n" + "="*70)
    print("GENERATING SAMPLE DATA")
    print("="*70)
    
    np.random.seed(RANDOM_SEED)
    n = 500
    
    data = {
        'student_id': range(1, n + 1),
        'age': np.random.randint(18, 26, n),
        'gender': np.random.choice(['Male', 'Female', 'Other'], n, p=[0.45, 0.50, 0.05]),
        'year_of_study': np.random.choice([1, 2, 3, 4], n),
        'cgpa': np.round(np.random.uniform(2.0, 4.0, n), 2),
        'depression_score': np.random.randint(1, 6, n),
        'anxiety_score': np.random.randint(1, 6, n),
        'stress_level': np.random.randint(1, 6, n),
        'sleep_quality': np.random.randint(1, 6, n),
        'campus_safety': np.random.randint(1, 6, n),
        'social_support': np.random.randint(1, 6, n),
        'campus_facilities': np.random.randint(1, 6, n),
        'accommodation_satisfaction': np.random.randint(1, 6, n),
        'peer_relationships': np.random.randint(1, 6, n),
        'academic_pressure': np.random.randint(1, 6, n),
        'workload_stress': np.random.randint(1, 6, n),
        'exam_anxiety': np.random.randint(1, 6, n),
        'grade_expectations': np.random.randint(1, 6, n),
        'career_concerns': np.random.randint(1, 6, n),
        'seeks_counseling': np.random.choice(['Yes', 'No'], n, p=[0.3, 0.7]),
        'aware_of_services': np.random.choice(['Yes', 'No'], n, p=[0.6, 0.4]),
    }
    
    df = pd.DataFrame(data)
    
    # Add realistic correlations
    df['depression_score'] = np.clip(
        df['depression_score'] + 0.3 * df['academic_pressure'] - 0.2 * df['social_support'],
        1, 5
    ).astype(int)
    
    df['anxiety_score'] = np.clip(
        df['anxiety_score'] + 0.4 * df['exam_anxiety'] - 0.15 * df['campus_safety'],
        1, 5
    ).astype(int)
    
    df['stress_level'] = np.clip(
        df['stress_level'] + 0.35 * df['workload_stress'] - 0.2 * df['peer_relationships'],
        1, 5
    ).astype(int)
    
    print(f"✓ Generated sample data with {n} students")
    return df

def clean_data(df):
    """
    Clean and preprocess the dataset
    """
    print("\n" + "="*70)
    print("DATA CLEANING AND PREPROCESSING")
    print("="*70)
    
    # Convert year_of_study to numeric
    if 'year_of_study' in df.columns:
        df['year_of_study'] = pd.to_numeric(df['year_of_study'], errors='coerce')
        df['year_of_study'] = df['year_of_study'].fillna(df['year_of_study'].median())
        df['year_of_study'] = df['year_of_study'].astype(int)
        print("✓ Cleaned year_of_study column")
    
    # Convert age to numeric
    if 'age' in df.columns:
        df['age'] = pd.to_numeric(df['age'], errors='coerce')
        df['age'] = df['age'].fillna(df['age'].median())
        df['age'] = df['age'].clip(16, 50).astype(int)
        print("✓ Cleaned age column")
    
    # Convert CGPA to numeric
    if 'cgpa' in df.columns:
        df['cgpa'] = pd.to_numeric(df['cgpa'], errors='coerce')
        df['cgpa'] = df['cgpa'].fillna(df['cgpa'].median())
        df['cgpa'] = df['cgpa'].clip(0, 4.0)
        print("✓ Cleaned cgpa column")
    
    # Clean numeric score columns
    score_cols = [
        'depression_score', 'anxiety_score', 'stress_level', 'sleep_quality',
        'campus_safety', 'social_support', 'campus_facilities', 
        'accommodation_satisfaction', 'peer_relationships',
        'academic_pressure', 'workload_stress', 'exam_anxiety',
        'grade_expectations', 'career_concerns'
    ]
    
    for col in score_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(df[col].median())
            df[col] = df[col].clip(1, 5)
    
    print(f"✓ Cleaned {len([c for c in score_cols if c in df.columns])} score columns")
    
    # Clean categorical columns
    if 'gender' in df.columns:
        df['gender'] = df['gender'].astype(str).str.strip()
        df['gender'] = df['gender'].replace({'nan': 'Other', 'None': 'Other'})
        print("✓ Cleaned gender column")
    
    if 'seeks_counseling' in df.columns:
        df['seeks_counseling'] = df['seeks_counseling'].astype(str).str.strip()
        yes_values = ['Yes', 'yes', 'YES', 'Y', 'y', '1', 'True', 'true']
        df['seeks_counseling'] = df['seeks_counseling'].apply(
            lambda x: 'Yes' if x in yes_values else 'No'
        )
        print("✓ Cleaned seeks_counseling column")
    
    if 'aware_of_services' in df.columns:
        df['aware_of_services'] = df['aware_of_services'].astype(str).str.strip()
        yes_values = ['Yes', 'yes', 'YES', 'Y', 'y', '1', 'True', 'true']
        df['aware_of_services'] = df['aware_of_services'].apply(
            lambda x: 'Yes' if x in yes_values else 'No'
        )
        print("✓ Cleaned aware_of_services column")
    
    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    if before != after:
        print(f"✓ Removed {before - after} duplicate rows")
    
    return df

def create_composite_scores(df):
    """
    Create composite scores for analysis
    """
    print("\n" + "="*70)
    print("CREATING COMPOSITE SCORES")
    print("="*70)
    
    # Campus Environment Score
    campus_cols = ['campus_safety', 'social_support', 'campus_facilities', 
                   'accommodation_satisfaction', 'peer_relationships']
    available_campus_cols = [col for col in campus_cols if col in df.columns]
    if available_campus_cols:
        df['campus_environment_score'] = df[available_campus_cols].mean(axis=1)
        print(f"✓ Created campus_environment_score (using {len(available_campus_cols)} columns)")
    
    # Academic Expectation Score
    academic_cols = ['academic_pressure', 'workload_stress', 'exam_anxiety', 
                     'grade_expectations', 'career_concerns']
    available_academic_cols = [col for col in academic_cols if col in df.columns]
    if available_academic_cols:
        df['academic_expectation_score'] = df[available_academic_cols].mean(axis=1)
        print(f"✓ Created academic_expectation_score (using {len(available_academic_cols)} columns)")
    
    # Mental Health Score
    mental_cols = ['depression_score', 'anxiety_score', 'stress_level', 'sleep_quality']
    available_mental_cols = [col for col in mental_cols if col in df.columns]
    if available_mental_cols:
        df['mental_health_score'] = df[available_mental_cols].mean(axis=1)
        print(f"✓ Created mental_health_score (using {len(available_mental_cols)} columns)")
    
    return df

def exploratory_data_analysis(df):
    """
    Create comprehensive EDA visualizations
    """
    print("\n" + "="*70)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*70)
    
    fig = plt.figure(figsize=FIGURE_SIZE)
    fig.suptitle('Student Mental Health - Exploratory Data Analysis', 
                 fontsize=20, fontweight='bold', y=0.995)
    
    # 1. Age Distribution
    plt.subplot(3, 4, 1)
    plt.hist(df['age'], bins=15, edgecolor='black', alpha=0.7)
    plt.title('Age Distribution', fontweight='bold')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    
    # 2. Gender Distribution
    plt.subplot(3, 4, 2)
    gender_counts = df['gender'].value_counts()
    plt.bar(gender_counts.index, gender_counts.values, edgecolor='black', alpha=0.7)
    plt.title('Gender Distribution', fontweight='bold')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    
    # 3. Year of Study
    plt.subplot(3, 4, 3)
    if 'year_of_study' in df.columns:
        year_counts = df['year_of_study'].value_counts().sort_index()
        plt.bar(year_counts.index, year_counts.values, edgecolor='black', alpha=0.7)
        plt.title('Year of Study Distribution', fontweight='bold')
        plt.xlabel('Year')
        plt.ylabel('Count')
    else:
        plt.text(0.5, 0.5, 'Year of Study\nData Not Available', 
                ha='center', va='center', fontsize=12)
        plt.title('Year of Study Distribution', fontweight='bold')
    
    # 4. CGPA Distribution
    plt.subplot(3, 4, 4)
    plt.hist(df['cgpa'], bins=20, edgecolor='black', alpha=0.7)
    plt.title('CGPA Distribution', fontweight='bold')
    plt.xlabel('CGPA')
    plt.ylabel('Frequency')
    
    # 5. Depression Score
    plt.subplot(3, 4, 5)
    plt.hist(df['depression_score'], bins=5, edgecolor='black', alpha=0.7, color='purple')
    plt.title('Depression Score Distribution', fontweight='bold')
    plt.xlabel('Score (1-5)')
    plt.ylabel('Frequency')
    
    # 6. Anxiety Score
    plt.subplot(3, 4, 6)
    plt.hist(df['anxiety_score'], bins=5, edgecolor='black', alpha=0.7, color='red')
    plt.title('Anxiety Score Distribution', fontweight='bold')
    plt.xlabel('Score (1-5)')
    plt.ylabel('Frequency')
    
    # 7. Stress Level
    plt.subplot(3, 4, 7)
    plt.hist(df['stress_level'], bins=5, edgecolor='black', alpha=0.7, color='orange')
    plt.title('Stress Level Distribution', fontweight='bold')
    plt.xlabel('Score (1-5)')
    plt.ylabel('Frequency')
    
    # 8. Mental Health Score
    plt.subplot(3, 4, 8)
    plt.hist(df['mental_health_score'], bins=20, edgecolor='black', alpha=0.7, color='darkred')
    plt.title('Overall Mental Health Score', fontweight='bold')
    plt.xlabel('Score (1-5)')
    plt.ylabel('Frequency')
    
    # 9. Campus Environment Score
    plt.subplot(3, 4, 9)
    plt.hist(df['campus_environment_score'], bins=20, edgecolor='black', alpha=0.7, color='green')
    plt.title('Campus Environment Score', fontweight='bold')
    plt.xlabel('Score (1-5)')
    plt.ylabel('Frequency')
    
    # 10. Academic Expectation Score
    plt.subplot(3, 4, 10)
    plt.hist(df['academic_expectation_score'], bins=20, edgecolor='black', alpha=0.7, color='blue')
    plt.title('Academic Expectation Score', fontweight='bold')
    plt.xlabel('Score (1-5)')
    plt.ylabel('Frequency')
    
    # 11. Counseling Seeking Behavior
    plt.subplot(3, 4, 11)
    counseling_counts = df['seeks_counseling'].value_counts()
    plt.bar(counseling_counts.index, counseling_counts.values, edgecolor='black', alpha=0.7)
    plt.title('Seeks Counseling', fontweight='bold')
    plt.xlabel('Response')
    plt.ylabel('Count')
    
    # 12. Service Awareness
    plt.subplot(3, 4, 12)
    awareness_counts = df['aware_of_services'].value_counts()
    plt.bar(awareness_counts.index, awareness_counts.values, edgecolor='black', alpha=0.7)
    plt.title('Aware of Services', fontweight='bold')
    plt.xlabel('Response')
    plt.ylabel('Count')
    
    plt.tight_layout()
    plt.savefig('01_exploratory_data_analysis.png', dpi=DPI, bbox_inches='tight')
    print("✓ Saved: 01_exploratory_data_analysis.png")
    plt.close()

def correlation_analysis(df):
    """
    Perform and visualize correlation analysis
    """
    print("\n" + "="*70)
    print("CORRELATION ANALYSIS")
    print("="*70)
    
    fig = plt.figure(figsize=(24, 10))
    fig.suptitle('Correlation Analysis - Campus Environment, Academic Expectations & Mental Health', 
                 fontsize=18, fontweight='bold', y=0.995)
    
    # Select relevant columns
    correlation_cols = [
        'depression_score', 'anxiety_score', 'stress_level', 'sleep_quality',
        'campus_safety', 'social_support', 'campus_facilities', 
        'accommodation_satisfaction', 'peer_relationships',
        'academic_pressure', 'workload_stress', 'exam_anxiety',
        'grade_expectations', 'career_concerns'
    ]
    
    # 1. Full Correlation Heatmap
    plt.subplot(1, 2, 1)
    corr_matrix = df[correlation_cols].corr()
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Matrix - All Factors', fontweight='bold', fontsize=14)
    
    # 2. Main Factors Correlation
    plt.subplot(1, 2, 2)
    main_factors = ['campus_environment_score', 'academic_expectation_score', 'mental_health_score']
    main_corr = df[main_factors].corr()
    sns.heatmap(main_corr, annot=True, fmt='.3f', cmap='RdYlGn_r', 
                center=0, square=True, linewidths=2, cbar_kws={"shrink": 0.8},
                vmin=-1, vmax=1)
    plt.title('Main Composite Scores Correlation', fontweight='bold', fontsize=14)
    
    plt.tight_layout()
    plt.savefig('02_correlation_analysis.png', dpi=DPI, bbox_inches='tight')
    print("✓ Saved: 02_correlation_analysis.png")
    plt.close()
    
    # Print key correlations
    print("\nKey Correlation Coefficients:")
    print(f"  Campus Environment ↔ Mental Health: {df['campus_environment_score'].corr(df['mental_health_score']):.3f}")
    print(f"  Academic Expectations ↔ Mental Health: {df['academic_expectation_score'].corr(df['mental_health_score']):.3f}")

def advanced_visualizations(df):
    """
    Create advanced analytical visualizations
    """
    print("\n" + "="*70)
    print("ADVANCED VISUALIZATIONS")
    print("="*70)
    
    fig = plt.figure(figsize=(24, 16))
    fig.suptitle('Advanced Analysis - Relationships and Patterns', 
                 fontsize=20, fontweight='bold', y=0.995)
    
    # 1. Campus Environment vs Mental Health
    plt.subplot(2, 3, 1)
    plt.scatter(df['campus_environment_score'], df['mental_health_score'], 
                alpha=0.5, s=50)
    z = np.polyfit(df['campus_environment_score'], df['mental_health_score'], 1)
    p = np.poly1d(z)
    plt.plot(df['campus_environment_score'].sort_values(), 
             p(df['campus_environment_score'].sort_values()), 
             "r--", linewidth=2, label='Trend Line')
    plt.xlabel('Campus Environment Score', fontweight='bold')
    plt.ylabel('Mental Health Score', fontweight='bold')
    plt.title('Campus Environment vs Mental Health', fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 2. Academic Expectations vs Mental Health
    plt.subplot(2, 3, 2)
    plt.scatter(df['academic_expectation_score'], df['mental_health_score'], 
                alpha=0.5, s=50, color='orange')
    z = np.polyfit(df['academic_expectation_score'], df['mental_health_score'], 1)
    p = np.poly1d(z)
    plt.plot(df['academic_expectation_score'].sort_values(), 
             p(df['academic_expectation_score'].sort_values()), 
             "r--", linewidth=2, label='Trend Line')
    plt.xlabel('Academic Expectation Score', fontweight='bold')
    plt.ylabel('Mental Health Score', fontweight='bold')
    plt.title('Academic Expectations vs Mental Health', fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 3. Mental Health by Year of Study
    plt.subplot(2, 3, 3)
    if 'year_of_study' in df.columns:
        year_data = df.groupby('year_of_study')[['depression_score', 'anxiety_score', 'stress_level']].mean()
        x = year_data.index
        width = 0.25
        plt.bar(x - width, year_data['depression_score'], width, label='Depression', alpha=0.8)
        plt.bar(x, year_data['anxiety_score'], width, label='Anxiety', alpha=0.8)
        plt.bar(x + width, year_data['stress_level'], width, label='Stress', alpha=0.8)
        plt.xlabel('Year of Study', fontweight='bold')
        plt.ylabel('Average Score', fontweight='bold')
        plt.title('Mental Health by Academic Year', fontweight='bold')
        plt.legend()
        plt.xticks(x)
        plt.grid(True, alpha=0.3, axis='y')
    else:
        plt.text(0.5, 0.5, 'Year of Study\nData Not Available', 
                ha='center', va='center', fontsize=12)
        plt.title('Mental Health by Academic Year', fontweight='bold')
    
    # 4. Mental Health by Gender
    plt.subplot(2, 3, 4)
    gender_data = df.groupby('gender')[['depression_score', 'anxiety_score', 'stress_level']].mean()
    gender_data.plot(kind='bar', ax=plt.gca(), alpha=0.8)
    plt.xlabel('Gender', fontweight='bold')
    plt.ylabel('Average Score', fontweight='bold')
    plt.title('Mental Health by Gender', fontweight='bold')
    plt.legend(title='Indicator')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3, axis='y')
    
    # 5. CGPA vs Mental Health
    plt.subplot(2, 3, 5)
    plt.scatter(df['cgpa'], df['mental_health_score'], alpha=0.5, s=50, color='green')
    z = np.polyfit(df['cgpa'], df['mental_health_score'], 1)
    p = np.poly1d(z)
    plt.plot(df['cgpa'].sort_values(), 
             p(df['cgpa'].sort_values()), 
             "r--", linewidth=2, label='Trend Line')
    plt.xlabel('CGPA', fontweight='bold')
    plt.ylabel('Mental Health Score', fontweight='bold')
    plt.title('CGPA vs Mental Health', fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 6. Box Plot - Mental Health Indicators
    plt.subplot(2, 3, 6)
    mental_indicators = df[['depression_score', 'anxiety_score', 'stress_level', 'sleep_quality']]
    plt.boxplot([mental_indicators[col] for col in mental_indicators.columns],
                labels=['Depression', 'Anxiety', 'Stress', 'Sleep Quality'])
    plt.ylabel('Score (1-5)', fontweight='bold')
    plt.title('Mental Health Indicators Distribution', fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('03_advanced_visualizations.png', dpi=DPI, bbox_inches='tight')
    print("✓ Saved: 03_advanced_visualizations.png")
    plt.close()

def statistical_testing(df):
    """
    Perform statistical hypothesis testing
    """
    print("\n" + "="*70)
    print("STATISTICAL HYPOTHESIS TESTING")
    print("="*70)
    
    # Test 1: Campus Environment and Mental Health
    print("\n1. Campus Environment Impact on Mental Health")
    poor_campus = df[df['campus_environment_score'] < 2.5]['mental_health_score']
    good_campus = df[df['campus_environment_score'] > 3.5]['mental_health_score']
    
    if len(poor_campus) > 0 and len(good_campus) > 0:
        t_stat, p_value = ttest_ind(poor_campus, good_campus)
        print(f"   T-statistic: {t_stat:.4f}")
        print(f"   P-value: {p_value:.4f}")
        print(f"   Result: {'Statistically significant' if p_value < 0.05 else 'Not significant'} (α=0.05)")
    
    # Test 2: Academic Expectations and Mental Health
    print("\n2. Academic Expectations Impact on Mental Health")
    low_academic = df[df['academic_expectation_score'] < 2.5]['mental_health_score']
    high_academic = df[df['academic_expectation_score'] > 3.5]['mental_health_score']
    
    if len(low_academic) > 0 and len(high_academic) > 0:
        t_stat, p_value = ttest_ind(low_academic, high_academic)
        print(f"   T-statistic: {t_stat:.4f}")
        print(f"   P-value: {p_value:.4f}")
        print(f"   Result: {'Statistically significant' if p_value < 0.05 else 'Not significant'} (α=0.05)")
    
    # Test 3: ANOVA - Mental Health across Years
    print("\n3. Mental Health Differences Across Academic Years")
    if 'year_of_study' in df.columns and df['year_of_study'].nunique() >= 2:
        years = sorted(df['year_of_study'].unique())
        groups = [df[df['year_of_study'] == year]['mental_health_score'] for year in years if len(df[df['year_of_study'] == year]) > 0]
        if len(groups) >= 2:
            f_stat, p_value = f_oneway(*groups)
            print(f"   F-statistic: {f_stat:.4f}")
            print(f"   P-value: {p_value:.4f}")
            print(f"   Result: {'Statistically significant' if p_value < 0.05 else 'Not significant'} (α=0.05)")
        else:
            print("   Not enough year groups for ANOVA")
    else:
        print("   Year of study data not available or insufficient")
    
    # Test 4: Pearson Correlations
    print("\n4. Pearson Correlation Coefficients")
    corr1, p1 = pearsonr(df['campus_environment_score'], df['mental_health_score'])
    print(f"   Campus Environment ↔ Mental Health: r={corr1:.3f}, p={p1:.4f}")
    
    corr2, p2 = pearsonr(df['academic_expectation_score'], df['mental_health_score'])
    print(f"   Academic Expectations ↔ Mental Health: r={corr2:.3f}, p={p2:.4f}")

def key_findings_summary(df):
    """
    Create summary visualizations of key findings
    """
    print("\n" + "="*70)
    print("KEY FINDINGS SUMMARY")
    print("="*70)
    
    fig = plt.figure(figsize=(20, 14))
    fig.suptitle('Key Findings - Executive Summary', 
                 fontsize=20, fontweight='bold', y=0.995)
    
    # 1. Mental Health Status Pie Chart
    plt.subplot(2, 2, 1)
    df['mh_category'] = pd.cut(df['mental_health_score'], 
                                bins=[0, 2, 3, 4, 5], 
                                labels=['Good', 'Moderate', 'Poor', 'Severe'])
    mh_dist = df['mh_category'].value_counts()
    colors = ['#2ecc71', '#f39c12', '#e67e22', '#e74c3c']
    plt.pie(mh_dist.values, labels=mh_dist.index, autopct='%1.1f%%',
            colors=colors, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
    plt.title('Mental Health Status Distribution', fontweight='bold', fontsize=14)
    
    # 2. Service Utilization Gap
    plt.subplot(2, 2, 2)
    util_data = {
        'High MH Concerns': (df['mental_health_score'] >= 3.5).sum() / len(df) * 100,
        'Seeking Counseling': (df['seeks_counseling'] == 'Yes').sum() / len(df) * 100,
        'Aware of Services': (df['aware_of_services'] == 'Yes').sum() / len(df) * 100
    }
    bars = plt.bar(util_data.keys(), util_data.values(), 
                   color=['#e74c3c', '#3498db', '#2ecc71'], alpha=0.8, edgecolor='black')
    plt.ylabel('Percentage (%)', fontweight='bold', fontsize=12)
    plt.title('Service Utilization Gap', fontweight='bold', fontsize=14)
    plt.ylim(0, 100)
    plt.xticks(rotation=15, ha='right')
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    
    # 3. Factor Impact Comparison
    plt.subplot(2, 2, 3)
    factors = ['Campus\nEnvironment', 'Academic\nExpectations', 'Social\nSupport', 
               'Workload\nStress', 'Peer\nRelationships']
    correlations = [
        df['campus_environment_score'].corr(df['mental_health_score']),
        df['academic_expectation_score'].corr(df['mental_health_score']),
        df['social_support'].corr(df['mental_health_score']),
        df['workload_stress'].corr(df['mental_health_score']),
        df['peer_relationships'].corr(df['mental_health_score'])
    ]
    colors_corr = ['green' if c < 0 else 'red' for c in correlations]
    bars = plt.barh(factors, correlations, color=colors_corr, alpha=0.7, edgecolor='black')
    plt.xlabel('Correlation Coefficient', fontweight='bold', fontsize=12)
    plt.title('Factor Correlation with Mental Health', fontweight='bold', fontsize=14)
    plt.xlim(-1, 1)
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
    for i, (bar, val) in enumerate(zip(bars, correlations)):
        plt.text(val + (0.05 if val > 0 else -0.05), i, 
                f'{val:.3f}', ha='left' if val > 0 else 'right', va='center', fontweight='bold')
    plt.grid(True, alpha=0.3, axis='x')
    
    # 4. Mental Health Indicators Average
    plt.subplot(2, 2, 4)
    indicators = ['Depression', 'Anxiety', 'Stress', 'Overall\nMH Score']
    values = [
        df['depression_score'].mean(),
        df['anxiety_score'].mean(),
        df['stress_level'].mean(),
        df['mental_health_score'].mean()
    ]
    bars = plt.bar(indicators, values, color=['#9b59b6', '#e74c3c', '#f39c12', '#34495e'], 
                   alpha=0.8, edgecolor='black')
    plt.ylabel('Average Score (1-5)', fontweight='bold', fontsize=12)
    plt.title('Mental Health Indicators - Average Scores', fontweight='bold', fontsize=14)
    plt.ylim(0, 5)
    plt.axhline(y=3, color='red', linestyle='--', linewidth=1, alpha=0.7, label='Concern Threshold')
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}', ha='center', va='bottom', fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('04_key_findings_summary.png', dpi=DPI, bbox_inches='tight')
    print("✓ Saved: 04_key_findings_summary.png")
    plt.close()

def save_processed_data(df):
    """
    Save processed dataset
    """
    output_file = 'processed_mental_health_data.csv'
    df.to_csv(output_file, index=False)
    print(f"\n✓ Saved processed data: {output_file}")
    print(f"  Shape: {df.shape}")

def print_summary_statistics(df):
    """
    Print summary statistics
    """
    print("\n" + "="*70)
    print("SUMMARY STATISTICS")
    print("="*70)
    
    print(f"\n📊 Dataset Overview:")
    print(f"   Total Students: {len(df)}")
    print(f"   Average Age: {df['age'].mean():.1f} years")
    print(f"   Average CGPA: {df['cgpa'].mean():.2f}/4.0")
    
    print(f"\n🧠 Mental Health Indicators (Average):")
    print(f"   Depression Score: {df['depression_score'].mean():.2f}/5.0")
    print(f"   Anxiety Score: {df['anxiety_score'].mean():.2f}/5.0")
    print(f"   Stress Level: {df['stress_level'].mean():.2f}/5.0")
    print(f"   Mental Health Score: {df['mental_health_score'].mean():.2f}/5.0")
    
    print(f"\n🏫 Campus & Academic (Average):")
    print(f"   Campus Environment: {df['campus_environment_score'].mean():.2f}/5.0")
    print(f"   Academic Expectations: {df['academic_expectation_score'].mean():.2f}/5.0")
    
    print(f"\n⚠️ Risk Assessment:")
    high_risk = (df['mental_health_score'] >= 3.5).sum()
    print(f"   High Risk Students: {high_risk} ({high_risk/len(df)*100:.1f}%)")
    seeking = (df['seeks_counseling'] == 'Yes').sum()
    print(f"   Seeking Counseling: {seeking} ({seeking/len(df)*100:.1f}%)")
    aware = (df['aware_of_services'] == 'Yes').sum()
    print(f"   Aware of Services: {aware} ({aware/len(df)*100:.1f}%)")

def main():
    """
    Main execution function
    """
    print("\n" + "="*70)
    print("STUDENT MENTAL HEALTH ANALYSIS")
    print("Analyzing Campus Environment, Academic Expectations & Mental Health")
    print("="*70)
    
    # Load data - Change filepath to your CSV file or leave None for sample data
    df = load_data('combined_mental_health_data.csv')
    
    # Clean the data
    df = clean_data(df)
    
    # Create composite scores
    df = create_composite_scores(df)
    
    # Print summary statistics
    print_summary_statistics(df)
    
    # Run analyses
    exploratory_data_analysis(df)
    correlation_analysis(df)
    statistical_testing(df)
    advanced_visualizations(df)
    key_findings_summary(df)
    
    # Save processed data
    save_processed_data(df)
    
    print("\n" + "="*70)
    print("✅ ANALYSIS COMPLETE!")
    print("="*70)
    print("\n📁 Generated Files:")
    print("   1. 01_exploratory_data_analysis.png")
    print("   2. 02_correlation_analysis.png")
    print("   3. 03_advanced_visualizations.png")
    print("   4. 04_key_findings_summary.png")
    print("   5. processed_mental_health_data.csv")
    
    print("\n🎯 Next Steps:")
    print("   1. Review the generated visualizations")
    print("   2. Run the interactive dashboard: streamlit run dashboard.py")
    print("   3. Share findings with stakeholders")
    print("   4. Implement recommendations")
    
    print("\n💡 Key Findings:")
    high_risk_pct = (df['mental_health_score'] >= 3.5).sum() / len(df) * 100
    seeking_pct = (df['seeks_counseling'] == 'Yes').sum() / len(df) * 100
    print(f"   • {high_risk_pct:.1f}% students show high mental health concerns")
    print(f"   • Only {seeking_pct:.1f}% are seeking counseling services")
    print(f"   • Service utilization gap: {high_risk_pct - seeking_pct:.1f}%")
    
    campus_corr = df['campus_environment_score'].corr(df['mental_health_score'])
    academic_corr = df['academic_expectation_score'].corr(df['mental_health_score'])
    print(f"   • Campus Environment correlation: {campus_corr:.3f}")
    print(f"   • Academic Expectations correlation: {academic_corr:.3f}")
    
    print("\n" + "="*70)
    print("Thank you for using Student Mental Health Analysis!")
    print("For questions or issues, please check the README.md file")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
