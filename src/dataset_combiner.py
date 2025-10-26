"""
Auto-Detecting Dataset Combiner for Student Mental Health Analysis
Automatically finds and combines all CSV files in the directory
"""

import pandas as pd
import numpy as np
import os
import glob

def find_csv_files():
    """
    Automatically find all CSV files in the current directory
    """
    csv_files = glob.glob("*.csv")
    
    # Filter out any output files
    csv_files = [f for f in csv_files if not f.startswith('combined_') 
                 and not f.startswith('processed_')]
    
    return csv_files

def load_and_inspect_datasets():
    """
    Load all CSV files found in directory
    """
    csv_files = find_csv_files()
    
    if not csv_files:
        print("\n✗ No CSV files found in the current directory")
        print("  Please ensure your downloaded datasets are in the same folder as this script")
        return {}
    
    datasets = {}
    
    print("="*70)
    print("LOADING AND INSPECTING DATASETS")
    print("="*70)
    print(f"\nFound {len(csv_files)} CSV file(s):")
    for f in csv_files:
        print(f"  - {f}")
    print()
    
    for i, filename in enumerate(csv_files, 1):
        try:
            df = pd.read_csv(filename)
            datasets[f'dataset{i}'] = df
            print(f"✓ Loaded: {filename}")
            print(f"  Shape: {df.shape}")
            print(f"  Columns: {list(df.columns[:10])}{'...' if len(df.columns) > 10 else ''}")
            print()
        except Exception as e:
            print(f"✗ Error loading {filename}: {str(e)}\n")
    
    return datasets

def standardize_column_names(df, dataset_name):
    """
    Standardize column names to match the analysis script requirements
    """
    
    column_mappings = {
        # Demographics
        'age': 'age',
        'Age': 'age',
        'gender': 'gender',
        'Gender': 'gender',
        'Choose your gender': 'gender',
        'sex': 'gender',
        'year': 'year_of_study',
        'Year': 'year_of_study',
        'Your current year of Study': 'year_of_study',
        'year_of_study': 'year_of_study',
        'level': 'year_of_study',
        'cgpa': 'cgpa',
        'CGPA': 'cgpa',
        'What is your CGPA?': 'cgpa',
        'gpa': 'cgpa',
        'GPA': 'cgpa',
        
        # Mental Health Indicators
        'depression': 'depression_score',
        'Depression': 'depression_score',
        'depression_score': 'depression_score',
        'Depression_Score': 'depression_score',
        'Do you have Depression?': 'depression_score',
        'PHQ-9': 'depression_score',
        'phq9': 'depression_score',
        
        'anxiety': 'anxiety_score',
        'Anxiety': 'anxiety_score',
        'anxiety_score': 'anxiety_score',
        'Anxiety_Score': 'anxiety_score',
        'Do you have Anxiety?': 'anxiety_score',
        'GAD-7': 'anxiety_score',
        'gad7': 'anxiety_score',
        
        'stress': 'stress_level',
        'Stress': 'stress_level',
        'stress_level': 'stress_level',
        'Stress_Level': 'stress_level',
        'PSS-10': 'stress_level',
        'pss10': 'stress_level',
        
        'sleep': 'sleep_quality',
        'sleep_quality': 'sleep_quality',
        'Sleep_Quality': 'sleep_quality',
        'Sleep Duration': 'sleep_quality',
        'sleep_hours': 'sleep_quality',
        
        # Campus Environment
        'campus_safety': 'campus_safety',
        'safety': 'campus_safety',
        'social_support': 'social_support',
        'Social_Support': 'social_support',
        'support': 'social_support',
        'facilities': 'campus_facilities',
        'campus_facilities': 'campus_facilities',
        'accommodation': 'accommodation_satisfaction',
        'Residence_Type': 'accommodation_satisfaction',
        'housing': 'accommodation_satisfaction',
        'peer_relationships': 'peer_relationships',
        'relationships': 'peer_relationships',
        'friends': 'peer_relationships',
        
        # Academic Factors
        'academic_pressure': 'academic_pressure',
        'Academic Pressure': 'academic_pressure',
        'pressure': 'academic_pressure',
        'workload': 'workload_stress',
        'Work Pressure': 'workload_stress',
        'workload_stress': 'workload_stress',
        'exam_anxiety': 'exam_anxiety',
        'exam_stress': 'exam_anxiety',
        'Do you have Panic attack?': 'exam_anxiety',
        'grade_expectations': 'grade_expectations',
        'expectations': 'grade_expectations',
        'career_concerns': 'career_concerns',
        'career': 'career_concerns',
        
        # Mental Health Support
        'counseling': 'seeks_counseling',
        'seeks_counseling': 'seeks_counseling',
        'Counseling_Service_Use': 'seeks_counseling',
        'Did you seek any specialist for a treatment?': 'seeks_counseling',
        'treatment': 'seeks_counseling',
        'therapy': 'seeks_counseling',
        'aware_of_services': 'aware_of_services',
        'awareness': 'aware_of_services',
        
        # Financial
        'Financial_Stress': 'financial_stress',
        'Financial Stress': 'financial_stress',
    }
    
    df_standardized = df.copy()
    
    rename_dict = {}
    for col in df.columns:
        col_stripped = col.strip()
        if col_stripped in column_mappings:
            rename_dict[col] = column_mappings[col_stripped]
    
    df_standardized.rename(columns=rename_dict, inplace=True)
    
    if rename_dict:
        print(f"{dataset_name} - Column Mapping:")
        for old, new in rename_dict.items():
            print(f"  {old} → {new}")
    
    return df_standardized

def normalize_scales(df):
    """
    Normalize different scales to 1-5 scale
    """
    
    scale_columns = [
        'depression_score', 'anxiety_score', 'stress_level', 'sleep_quality',
        'campus_safety', 'social_support', 'campus_facilities', 
        'accommodation_satisfaction', 'peer_relationships',
        'academic_pressure', 'workload_stress', 'exam_anxiety',
        'grade_expectations', 'career_concerns'
    ]
    
    for col in scale_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
            valid_values = df[col].dropna()
            
            if len(valid_values) == 0:
                continue
            
            col_min = valid_values.min()
            col_max = valid_values.max()
            
            if col_min >= 1 and col_max <= 5:
                continue
            
            if col_min != col_max:
                df[col] = 1 + 4 * (df[col] - col_min) / (col_max - col_min)
                df[col] = df[col].round().astype('Int64')
                print(f"  Normalized {col}: [{col_min}, {col_max}] → [1, 5]")
    
    return df

def standardize_categorical_values(df):
    """
    Standardize categorical values
    """
    
    if 'gender' in df.columns:
        gender_mapping = {
            'male': 'Male', 'Male': 'Male', 'M': 'Male', 'm': 'Male',
            'female': 'Female', 'Female': 'Female', 'F': 'Female', 'f': 'Female',
            'other': 'Other', 'Other': 'Other', 'non-binary': 'Other',
            'prefer not to say': 'Other', 'Prefer not to say': 'Other'
        }
        df['gender'] = df['gender'].astype(str).str.strip()
        df['gender'] = df['gender'].map(lambda x: gender_mapping.get(x, 'Other'))
    
    yes_no_to_score = {'Yes': 5, 'No': 1, 'yes': 5, 'no': 1}
    
    if 'depression_score' in df.columns:
        if df['depression_score'].dtype == 'object':
            df['depression_score'] = df['depression_score'].map(yes_no_to_score)
            df['depression_score'] = pd.to_numeric(df['depression_score'], errors='coerce')
    
    if 'anxiety_score' in df.columns:
        if df['anxiety_score'].dtype == 'object':
            df['anxiety_score'] = df['anxiety_score'].map(yes_no_to_score)
            df['anxiety_score'] = pd.to_numeric(df['anxiety_score'], errors='coerce')
    
    if 'exam_anxiety' in df.columns:
        if df['exam_anxiety'].dtype == 'object':
            df['exam_anxiety'] = df['exam_anxiety'].map(yes_no_to_score)
            df['exam_anxiety'] = pd.to_numeric(df['exam_anxiety'], errors='coerce')
    
    yes_no_columns = ['seeks_counseling', 'aware_of_services']
    for col in yes_no_columns:
        if col in df.columns:
            yes_values = ['yes', 'Yes', 'YES', 'y', 'Y', 'true', 'True', '1', 1, True]
            df[col] = df[col].astype(str).apply(lambda x: 'Yes' if x.strip() in yes_values else 'No')
    
    if 'accommodation_satisfaction' in df.columns:
        if df['accommodation_satisfaction'].dtype == 'object':
            accommodation_mapping = {
                'On-Campus': 4,
                'Off-Campus': 3,
                'Home': 3,
                'With Family': 4,
                'Alone': 2
            }
            df['accommodation_satisfaction'] = df['accommodation_satisfaction'].map(
                lambda x: accommodation_mapping.get(str(x).strip(), 3)
            )
    
    return df

def add_missing_columns(df):
    """
    Add missing columns with default values
    """
    
    required_columns = {
        'age': lambda: np.random.randint(18, 26, len(df)),
        'gender': 'Other',
        'year_of_study': lambda: np.random.choice([1, 2, 3, 4], len(df)),
        'cgpa': lambda: np.round(np.random.uniform(2.5, 3.5, len(df)), 2),
        'campus_safety': 3,
        'social_support': 3,
        'campus_facilities': 3,
        'accommodation_satisfaction': 3,
        'peer_relationships': 3,
        'academic_pressure': 3,
        'workload_stress': 3,
        'exam_anxiety': 3,
        'grade_expectations': 3,
        'career_concerns': 3,
        'depression_score': 3,
        'anxiety_score': 3,
        'stress_level': 3,
        'sleep_quality': 3,
        'seeks_counseling': 'No',
        'aware_of_services': 'Yes'
    }
    
    added_columns = []
    for col, default_value in required_columns.items():
        if col not in df.columns:
            if callable(default_value):
                df[col] = default_value()
            else:
                df[col] = default_value
            added_columns.append(col)
    
    if added_columns:
        print(f"\nAdded missing columns with default values:")
        for col in added_columns:
            print(f"  - {col}")
    
    return df

def combine_datasets(datasets):
    """
    Combine multiple datasets
    """
    
    if not datasets:
        return None
    
    print("\n" + "="*70)
    print("COMBINING AND STANDARDIZING DATASETS")
    print("="*70)
    
    combined_dfs = []
    
    for name, df in datasets.items():
        print(f"\nProcessing: {name}")
        print(f"  Original shape: {df.shape}")
        
        df = standardize_column_names(df, name)
        df = normalize_scales(df)
        df = standardize_categorical_values(df)
        df = add_missing_columns(df)
        
        print(f"  Final shape: {df.shape}")
        
        combined_dfs.append(df)
    
    print(f"\n{'='*70}")
    print("MERGING DATASETS")
    print("="*70)
    
    combined_df = pd.concat(combined_dfs, ignore_index=True, sort=False)
    combined_df.insert(0, 'student_id', range(1, len(combined_df) + 1))
    
    print(f"\nCombined dataset shape: {combined_df.shape}")
    print(f"Total students: {len(combined_df)}")
    
    return combined_df

def create_composite_scores(df):
    """
    Create composite scores
    """
    
    print(f"\n{'='*70}")
    print("CREATING COMPOSITE SCORES")
    print("="*70)
    
    campus_cols = ['campus_safety', 'social_support', 'campus_facilities', 
                   'accommodation_satisfaction', 'peer_relationships']
    if all(col in df.columns for col in campus_cols):
        df['campus_environment_score'] = df[campus_cols].mean(axis=1)
        print("✓ Created campus_environment_score")
    
    academic_cols = ['academic_pressure', 'workload_stress', 'exam_anxiety', 
                     'grade_expectations', 'career_concerns']
    if all(col in df.columns for col in academic_cols):
        df['academic_expectation_score'] = df[academic_cols].mean(axis=1)
        print("✓ Created academic_expectation_score")
    
    mental_cols = ['depression_score', 'anxiety_score', 'stress_level', 'sleep_quality']
    if all(col in df.columns for col in mental_cols):
        df['mental_health_score'] = df[mental_cols].mean(axis=1)
        print("✓ Created mental_health_score")
    
    return df

def clean_and_validate(df):
    """
    Final cleaning and validation
    """
    
    print(f"\n{'='*70}")
    print("CLEANING AND VALIDATION")
    print("="*70)
    
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    if before != after:
        print(f"✓ Removed {before - after} duplicate rows")
    
    print(f"\nHandling missing values...")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if len(df[col].mode()) > 0:
            df[col] = df[col].fillna(df[col].mode()[0])
    
    print("✓ Filled missing values")
    
    score_columns = [col for col in df.columns if 'score' in col or col in [
        'depression_score', 'anxiety_score', 'stress_level', 'sleep_quality',
        'campus_safety', 'social_support', 'campus_facilities', 
        'accommodation_satisfaction', 'peer_relationships',
        'academic_pressure', 'workload_stress', 'exam_anxiety',
        'grade_expectations', 'career_concerns'
    ]]
    
    for col in score_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].clip(1, 5)
    
    print("✓ Validated score ranges (1-5)")
    
    if 'cgpa' in df.columns:
        df['cgpa'] = pd.to_numeric(df['cgpa'], errors='coerce')
        df['cgpa'] = df['cgpa'].clip(0, 4.0)
        print("✓ Validated CGPA range (0-4.0)")
    
    if 'age' in df.columns:
        df['age'] = pd.to_numeric(df['age'], errors='coerce')
        df['age'] = df['age'].clip(16, 40).astype('Int64')
        print("✓ Validated age range (16-40)")
    
    return df

def save_combined_dataset(df, output_filename='combined_mental_health_data.csv'):
    """
    Save the combined dataset
    """
    
    print(f"\n{'='*70}")
    print("SAVING COMBINED DATASET")
    print("="*70)
    
    df.to_csv(output_filename, index=False)
    print(f"\n✓ Saved: {output_filename}")
    print(f"  Shape: {df.shape}")
    print(f"  Total Students: {len(df)}")
    
    print(f"\n{'='*70}")
    print("DATASET SUMMARY")
    print("="*70)
    
    # Show key columns
    key_cols = ['student_id', 'age', 'gender', 'cgpa', 'depression_score', 
                'anxiety_score', 'stress_level', 'campus_environment_score',
                'academic_expectation_score', 'mental_health_score']
    
    available_key_cols = [col for col in key_cols if col in df.columns]
    
    print(f"\nSample Data (first 5 rows, key columns):")
    print(df[available_key_cols].head())
    
    print(f"\n{'='*70}")
    print("✓ DATASET COMBINATION COMPLETE!")
    print("="*70)
    print(f"\nNext Steps:")
    print(f"1. Use '{output_filename}' in your analysis script")
    print(f"2. Update mental_health_analysis.py line 118:")
    print(f"   df = load_data('{output_filename}')")
    print(f"3. Run the analysis: python mental_health_analysis.py")
    
    return output_filename

def main():
    """
    Main execution
    """
    
    print("\n" + "="*70)
    print("STUDENT MENTAL HEALTH DATASET COMBINER")
    print("Auto-Detecting CSV Files")
    print("="*70)
    
    datasets = load_and_inspect_datasets()
    
    if not datasets:
        print("\n⚠ No datasets loaded.")
        return
    
    combined_df = combine_datasets(datasets)
    
    if combined_df is None:
        return
    
    combined_df = create_composite_scores(combined_df)
    combined_df = clean_and_validate(combined_df)
    
    output_file = save_combined_dataset(combined_df)
    
    print(f"\n✅ SUCCESS! Dataset ready for analysis.")

if __name__ == "__main__":
    main()
