# 🧠 Student Mental Health Analysis

<div align="center">

![Mental Health Banner](https://img.shields.io/badge/Mental_Health-Analytics-blue?style=for-the-badge)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

**A data-driven approach to understanding and improving campus mental wellness**

[🚀 Quick Start](#-quick-start) • [📊 Dashboard](#-interactive-dashboard) • [📈 Results](#-key-findings) • [📖 Documentation](#-documentation)

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Findings](#-key-findings)
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Methodology](#-methodology)
- [Results & Visualizations](#-results--visualizations)
- [Interactive Dashboard](#-interactive-dashboard)
- [Recommendations](#-recommendations)
- [Technologies](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

### The Challenge

Mental health challenges among university students have reached critical levels, with inadequate support systems and limited understanding of primary stressors affecting academic performance and wellbeing.

### Our Solution

This comprehensive data science project analyzes 500+ student records to uncover patterns, identify risk factors, and provide evidence-based recommendations for establishing an effective campus mental health center.

### Project Information

- 👤 **Author:** Rashika R
- 🎓 **Roll Number:** 953624104122
- 🏛️ **Institution:** Ramco Institute of Technology
- 📚 **Course:** CS3361 Data Science Laboratory
- 📅 **Date:** November 2025

---

## 🔍 Key Findings

<div align="center">

### Critical Statistics at a Glance

| 📊 Metric | 📈 Value | 💡 Implication |
|-----------|----------|----------------|
| **High-Risk Students** | **35%** (175/500) | 1 in 3 students needs immediate support |
| **Service Gap** | **70%** | Massive underutilization of mental health services |
| **Awareness Gap** | **40%** | 200 students unaware of available resources |
| **Academic Pressure** | **r = +0.52*** | Strongest predictor of mental distress |
| **Campus Environment** | **r = -0.45*** | Significant protective factor |

*\*\*\* p < 0.001 (highly statistically significant)*

</div>

### 🎯 Top 5 Discoveries

1. **📊 Mental Health Crisis**
   - 35% of students in high-risk categories
   - 50% report moderate to severe symptoms
   - Only 30% currently seeking help

2. **🚨 Service Utilization Gap**
   - 70% gap between need and service usage
   - Primary barriers: awareness, stigma, accessibility
   - Opportunity for immediate intervention

3. **📚 Academic Stress Dominance**
   - Workload stress: strongest predictor (r = +0.58, p < 0.001)
   - Academic pressure affects 80% of students
   - Exam stress peaks in 3rd/4th year students

4. **🏛️ Environment Impact**
   - Campus quality significantly protects mental health (r = -0.45)
   - Recreational facilities reduce stress by 23%
   - Green spaces correlate with better wellbeing

5. **👥 Peer Support Power**
   - Strongest protective factor identified (r = -0.51)
   - Students with strong peer networks: 40% lower risk
   - Social isolation: major risk multiplier

---

## ✨ Features

### 📊 Comprehensive Analysis
- ✅ Statistical analysis of 20+ mental health indicators
- ✅ Correlation studies across 5 key categories
- ✅ Hypothesis testing (t-tests, ANOVA, chi-square)
- ✅ Risk categorization and predictive insights

### 📈 Rich Visualizations
- ✅ Interactive correlation heatmaps
- ✅ Distribution analysis plots
- ✅ Comparative demographic analysis
- ✅ Trend identification charts
- ✅ Factor impact visualizations

### 🖥️ Interactive Dashboard
- ✅ Real-time data filtering
- ✅ Dynamic visualizations
- ✅ Demographic breakdowns
- ✅ Export capabilities
- ✅ Mobile-responsive design

### 📝 Evidence-Based Recommendations
- ✅ Short, medium, and long-term action plans
- ✅ Budget estimates and ROI projections
- ✅ Implementation timelines
- ✅ Success metrics and KPIs

---

## 🚀 Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip package manager
- Git

### Step 1: Clone Repository

```bash
git clone https://github.com/R7X-doodles/student-mental-health-analysis.git
cd student-mental-health-analysis
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Dependencies

```txt
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
plotly>=5.17.0
streamlit>=1.28.0
scikit-learn>=1.2.0
jupyter>=1.0.0
openpyxl>=3.1.0
```

---

## 🎬 Quick Start

### Option 1: Run Complete Analysis

```python
from src.mental_health_analyzer import MentalHealthAnalyzer

# Initialize analyzer
analyzer = MentalHealthAnalyzer()

# Load and process data
analyzer.load_data('data/raw/student_mental_health.csv')
analyzer.preprocess_data()

# Run statistical analyses
analyzer.correlation_analysis(method='pearson')
analyzer.hypothesis_testing()
analyzer.calculate_risk_categories()

# Generate visualizations
analyzer.generate_all_visualizations()

# Create comprehensive report
analyzer.generate_report(output_path='outputs/reports/')
```

### Option 2: Launch Interactive Dashboard

```bash
streamlit run dashboard/app.py
```

Then open your browser to: `http://localhost:8501`

### Option 3: Explore Jupyter Notebooks

```bash
jupyter notebook notebooks/
```

Navigate to:
1. `01_data_cleaning.ipynb` - Data preprocessing
2. `02_exploratory_analysis.ipynb` - EDA
3. `03_statistical_analysis.ipynb` - Statistical tests
4. `04_visualizations.ipynb` - Generate all plots

---

## 📁 Project Structure

```
student-mental-health-analysis/
│
├── 📄 README.md                          # You are here
├── 📄 requirements.txt                   # Python dependencies
├── 📄 LICENSE                            # MIT License
├── 📄 .gitignore                        # Git ignore rules
│
├── 📂 data/
│   ├── 📄 README.md                     # Data dictionary & descriptions
│   ├── 📂 raw/                          # Original datasets
│   │   └── student_mental_health.csv    # Primary dataset (500 records)
│   └── 📂 processed/                    # Cleaned & processed data
│       ├── cleaned_data.csv
│       └── feature_engineered.csv
│
├── 📂 notebooks/                         # Jupyter notebooks for analysis
│   ├── 01_data_cleaning.ipynb           # Data preprocessing & cleaning
│   ├── 02_exploratory_analysis.ipynb    # EDA with visualizations
│   ├── 03_statistical_analysis.ipynb    # Hypothesis testing & correlations
│   └── 04_visualizations.ipynb          # Generate publication-ready plots
│
├── 📂 src/                               # Source code modules
│   ├── __init__.py
│   ├── mental_health_analyzer.py        # Main analysis class
│   ├── data_processing.py               # Data cleaning utilities
│   ├── statistical_analysis.py          # Statistical test functions
│   └── visualization.py                 # Plotting functions
│
├── 📂 outputs/                           # Generated outputs
│   ├── 📂 figures/                      # All visualizations (PNG, PDF)
│   │   ├── 01_exploratory_data_analysis.png
│   │   ├── 02_correlation_analysis.png
│   │   ├── 03_advanced_visualizations.png
│   │   ├── 04_key_findings_summary.png
│   │   └── service_utilization_gap.png
│   └── 📂 reports/                      # Analysis reports
│       ├── analysis_report.txt
│       ├── statistical_summary.pdf
│       └── final_report.pdf
│
├── 📂 dashboard/                         # Interactive Streamlit dashboard
│   ├── app.py                           # Main dashboard application
│   ├── config.py                        # Configuration settings
│   └── utils.py                         # Helper functions
│
├── 📂 docs/                              # Documentation
│   ├── project_report.pdf               # Complete 32-page report
│   ├── presentation.pptx                # Project presentation
│   ├── methodology.md                   # Detailed methodology
│   └── data_dictionary.md               # Variable descriptions
│
└── 📂 tests/                             # Unit tests
    ├── test_data_processing.py
    ├── test_statistical_analysis.py
    └── test_visualization.py
```

---

## 🔬 Methodology

### Research Design

**Type:** Quantitative cross-sectional study  
**Sample Size:** 500 students  
**Sampling Method:** Stratified random sampling  
**Data Collection:** Online surveys + Kaggle datasets

### Variables Analyzed

#### 1. **Demographics** (5 variables)
- Age, Gender, Academic Year, Department, CGPA

#### 2. **Mental Health Indicators** (6 variables)
- Anxiety levels, Depression symptoms, Stress levels
- Sleep quality, Emotional wellbeing, General mental health

#### 3. **Academic Factors** (4 variables)
- Academic pressure, Workload stress, Exam anxiety, Performance expectations

#### 4. **Campus Environment** (3 variables)
- Campus quality, Recreational facilities, Living conditions

#### 5. **Support Systems** (2 variables)
- Peer relationships, Social support network

### Statistical Methods

#### Descriptive Statistics
- **Central Tendency:** Mean, Median, Mode
- **Dispersion:** Standard Deviation, Variance, Range
- **Distribution:** Skewness, Kurtosis

#### Inferential Statistics
- **Pearson Correlation:** Linear relationships between continuous variables
- **Spearman Correlation:** Non-parametric rank correlations
- **Independent t-tests:** Gender-based comparisons
- **One-way ANOVA:** Year-wise differences in mental health
- **Chi-square tests:** Categorical variable associations
- **Linear Regression:** Predictive modeling

### Data Processing Pipeline

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐     ┌──────────────┐
│  Raw Data   │────▶│   Cleaning   │────▶│    Feature      │────▶│  Statistical │
│  (500 rows) │     │  & Validation│     │   Engineering   │     │   Analysis   │
└─────────────┘     └──────────────┘     └─────────────────┘     └──────────────┘
                            │                      │                       │
                            ▼                      ▼                       ▼
                    ┌──────────────┐     ┌─────────────────┐     ┌──────────────┐
                    │   Outlier    │     │   Composite     │     │Visualization │
                    │   Detection  │     │     Scores      │     │  & Reporting │
                    └──────────────┘     └─────────────────┘     └──────────────┘
```

**Key Processing Steps:**
1. Missing value handling (median imputation for continuous, mode for categorical)
2. Outlier detection using IQR method (threshold = 1.5)
3. Feature scaling and normalization
4. Composite score creation for multi-item constructs
5. Data validation and quality checks

---

## 📊 Results & Visualizations

### Mental Health Distribution

<div align="center">

| Category | Score Range | Percentage | Count | Status |
|----------|-------------|------------|-------|--------|
| 🟢 **Good** | 1.0 - 2.0 | 20% | 100 | Low risk |
| 🟡 **Moderate** | 2.0 - 3.0 | 30% | 150 | Monitor |
| 🟠 **Poor** | 3.0 - 4.0 | 25% | 125 | Intervention needed |
| 🔴 **Severe** | 4.0 - 5.0 | 25% | 125 | Urgent support required |

</div>

### Correlation Analysis Results

**Strongest Positive Correlations (Risk Factors)**

| Factor | Correlation | p-value | Effect Size | Interpretation |
|--------|-------------|---------|-------------|----------------|
| 📚 Workload Stress | r = **+0.58** | < 0.001 | Large | Major predictor |
| 📖 Academic Pressure | r = **+0.55** | < 0.001 | Large | Critical factor |
| 😰 Exam Anxiety | r = **+0.49** | < 0.001 | Medium | Significant impact |
| 😴 Sleep Problems | r = **+0.42** | < 0.001 | Medium | Important indicator |

**Strongest Negative Correlations (Protective Factors)**

| Factor | Correlation | p-value | Effect Size | Interpretation |
|--------|-------------|---------|-------------|----------------|
| 👥 Peer Relationships | r = **-0.51** | < 0.001 | Large | Strongest protector |
| 🤝 Social Support | r = **-0.48** | < 0.001 | Medium | Critical buffer |
| 🏛️ Campus Environment | r = **-0.45** | < 0.001 | Medium | Significant factor |
| 🎮 Recreational Activities | r = **-0.38** | < 0.001 | Medium | Important outlet |

### Hypothesis Testing Results

#### Gender Differences
- **Anxiety:** Females significantly higher (t = 3.24, **p = 0.001**, Cohen's d = 0.41)
- **Depression:** Females significantly higher (t = 2.87, **p = 0.004**, Cohen's d = 0.36)
- **Overall Mental Health:** Females report poorer health (t = 2.95, **p = 0.003**)

#### Year-wise Analysis (ANOVA)
- **F-statistic:** 6.78
- **p-value:** < 0.001
- **Finding:** 3rd and 4th year students show highest stress levels
- **Post-hoc:** 3rd year significantly different from 1st year (p < 0.001)

#### CGPA Correlation
- **Correlation:** r = -0.28 (p < 0.001)
- **Interpretation:** Lower mental health associated with lower CGPA
- **Note:** Bidirectional relationship possible

### Available Visualizations

All visualizations are publication-ready and available in `outputs/figures/`:

1. **📊 Exploratory Data Analysis** (`01_exploratory_data_analysis.png`)
   - Distribution plots for all mental health indicators
   - Demographic breakdowns
   - Summary statistics panels

2. **🔥 Correlation Heatmap** (`02_correlation_analysis.png`)
   - Complete correlation matrix
   - Significance markers
   - Color-coded strength indicators

3. **📈 Advanced Visualizations** (`03_advanced_visualizations.png`)
   - Box plots for group comparisons
   - Violin plots for distribution analysis
   - Scatter plots with regression lines
   - Radar charts for factor profiles

4. **⚠️ Service Gap Analysis** (`service_utilization_gap.png`)
   - Current vs. optimal utilization
   - Barrier identification
   - Opportunity quantification

5. **🎯 Key Findings Summary** (`04_key_findings_summary.png`)
   - Executive dashboard
   - Top insights infographic
   - Action priority matrix

---

## 🖥️ Interactive Dashboard

### Access the Dashboard

```bash
streamlit run dashboard/app.py
```

### Dashboard Sections

#### 1. 📊 Overview & Key Metrics
- Real-time statistics display
- High-risk student identification
- Service gap visualization
- Quick insights panel

#### 2. 🔍 Correlation Explorer
- Interactive correlation matrix
- Hover for detailed statistics
- Filter by significance levels
- Export correlation data

#### 3. 📈 Trends & Comparisons
- Year-wise trend analysis
- Gender-based comparisons
- Department breakdowns
- Temporal patterns

#### 4. 🎯 Factor Analysis
- Individual factor impact visualization
- Scatter plots with trend lines
- Distribution comparisons
- Risk factor ranking

#### 5. 💡 Recommendations
- Evidence-based action items
- Implementation timeline
- Budget estimates
- Expected outcomes dashboard

### Dashboard Features

✅ **Real-time Filtering:** Filter by gender, year, department, CGPA  
✅ **Interactive Charts:** Hover, zoom, pan, download  
✅ **Export Options:** PNG, SVG, PDF, CSV formats  
✅ **Mobile Responsive:** Works on all devices  
✅ **Custom Reports:** Generate personalized analysis  
✅ **Data Privacy:** All data anonymized and aggregated

---

## 💡 Recommendations

### 🚨 Immediate Actions (0-6 Months)

#### 1. Emergency Response Team
- **Action:** Establish crisis intervention protocol
- **Target:** < 24-hour response time
- **Cost:** $50,000 - $80,000
- **Impact:** Immediate safety net for high-risk students

#### 2. Awareness Campaign
- **Launch:** Campus-wide mental health awareness initiative
- **Components:**
  - Digital campaign (social media, email, website)
  - Physical materials (posters, brochures, flyers)
  - Mental Health Awareness Week
  - Student ambassador program
- **Target:** 90% awareness by end of semester
- **Cost:** $15,000 - $25,000

#### 3. Counselor Hiring
- **Action:** Hire 2-3 licensed mental health professionals
- **Ratio Goal:** 1:250 counselor-to-student ratio
- **Space:** Dedicated counseling offices
- **Cost:** $120,000 - $180,000/year

### 📅 Short-term Initiatives (6-12 Months)

#### 1. Mental Health Center Establishment
- **Facility:** Multi-room counseling center
- **Services:**
  - Individual counseling (drop-in + appointments)
  - Group therapy sessions
  - Workshops and psychoeducation
  - Relaxation/meditation space
- **Staffing:** 4-5 counselors + admin support
- **Cost:** $200,000 - $350,000 (setup + annual)

#### 2. Peer Support Program
- **Train:** 20-30 peer counselors
- **Establish:** Support groups for common issues
  - Anxiety management
  - Stress reduction
  - Academic pressure coping
  - Social connection building
- **Buddy System:** Pair first-year students with trained peers
- **Cost:** $30,000 - $50,000

#### 3. Screening & Early Intervention
- **Implement:** Semester-based mental health screenings
- **Tools:** Validated assessment instruments (PHQ-9, GAD-7)
- **Follow-up:** Automated referral system
- **Integration:** Link with academic advising
- **Cost:** $40,000 - $60,000

### 🎯 Long-term Strategy (1-3 Years)

#### 1. Comprehensive Service Expansion
- **Individual Therapy:** 1000+ sessions/semester capacity
- **Group Therapy:** 15+ specialized groups
- **Crisis Hotline:** 24/7 phone/text support
- **Psychiatric Services:** On-campus psychiatrist (part-time)
- **Workshops:** 50+ annual sessions on various topics
- **Cost:** $400,000 - $600,000/year

#### 2. Academic Policy Integration
- **Review:** Course workload distribution policies
- **Implement:** Mental health accommodation system
- **Train:** Faculty on mental health awareness (100% participation)
- **Adjust:** Exam scheduling to reduce stress clustering
- **Create:** Academic flexibility options for struggling students
- **Cost:** $80,000 - $120,000

#### 3. Continuous Monitoring System
- **Quarterly Surveys:** Track mental health trends
- **Dashboard:** Real-time monitoring system
- **Evaluation:** Service effectiveness assessment
- **Adjustment:** Data-driven program modifications
- **Research:** Partner with researchers for ongoing studies
- **Cost:** $50,000 - $80,000/year

### 📊 Expected Outcomes (3-Year Targets)

| Metric | Baseline | Year 1 Target | Year 2 Target | Year 3 Target | Total Improvement |
|--------|----------|---------------|---------------|---------------|-------------------|
| High-risk students | 35% | 28% | 23% | 18% | **-49%** |
| Service utilization | 30% | 45% | 55% | 65% | **+117%** |
| Service awareness | 60% | 75% | 85% | 90% | **+50%** |
| Avg mental health score | 3.2/5 | 2.9/5 | 2.6/5 | 2.4/5 | **-25%** |
| Student satisfaction | 65% | 72% | 80% | 85% | **+31%** |
| Dropout rate | 8% | 7% | 6% | 5% | **-38%** |

### 💰 Budget Estimate

#### Annual Operating Costs (Steady State)

| Category | Low Estimate | High Estimate | Notes |
|----------|--------------|---------------|-------|
| **Personnel** | $300,000 | $500,000 | Counselors, psychiatrist, admin |
| **Facility** | $100,000 | $200,000 | Rent, utilities, maintenance |
| **Programs** | $50,000 | $100,000 | Workshops, groups, events |
| **Technology** | $30,000 | $50,000 | Software, telehealth, systems |
| **Marketing** | $20,000 | $40,000 | Awareness, outreach |
| **Training** | $15,000 | $25,000 | Staff development, peer training |
| **Contingency** | $25,000 | $50,000 | Unexpected needs |
| **TOTAL** | **$540,000** | **$965,000** | **Average: $752,500/year** |

#### Return on Investment (ROI)

**Cost Savings from Intervention:**
- Reduced dropout rate: $400,000/year (estimated)
- Improved academic performance: $200,000/year (scholarships retained)
- Crisis prevention: $150,000/year (hospitalizations avoided)

**Total Annual Benefit:** $750,000  
**Net ROI:** Break-even to positive after Year 2

---

## 🛠️ Technologies Used

### Core Languages & Frameworks

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)

### Data Visualization

![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

### Web Framework & Tools

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

### Detailed Technology Stack

| Category | Technologies | Purpose |
|----------|-------------|---------|
| **Language** | Python 3.8+ | Primary programming language |
| **Data Manipulation** | Pandas, NumPy | Data processing and analysis |
| **Statistics** | SciPy, Statsmodels | Statistical testing and modeling |
| **Machine Learning** | Scikit-learn | Predictive modeling |
| **Visualization** | Matplotlib, Seaborn, Plotly | Static and interactive charts |
| **Dashboard** | Streamlit | Interactive web application |
| **Notebooks** | Jupyter | Exploratory analysis |
| **Version Control** | Git, GitHub | Code management |
| **Documentation** | Markdown, LaTeX | Project documentation |

---

## 🤝 Contributing

Contributions are welcome! While this is primarily an academic project, improvements and suggestions are appreciated.

### How to Contribute

1. **Fork the repository**
   ```bash
   git clone https://github.com/R7X-doodles/student-mental-health-analysis.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make your changes**
   - Follow existing code style
   - Add comments and documentation
   - Test your changes

4. **Commit your changes**
   ```bash
   git commit -m "Add: Brief description of your changes"
   ```

5. **Push to your branch**
   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Open a Pull Request**
   - Describe your changes clearly
   - Reference any related issues

### Contribution Guidelines

- ✅ Follow PEP 8 style guide for Python code
- ✅ Add docstrings to all functions
- ✅ Include unit tests for new features
- ✅ Update documentation as needed
- ✅ Ensure all tests pass before submitting

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Rashika R

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📧 Contact

### Rashika R

- 🎓 **Roll Number:** 953624104122
- 🏛️ **Institution:** Ramco Institute of Technology
- 📚 **Department:** Computer Science and Engineering
- 📧 **Email:** [rashikarajesh2007@gmail.com](mailto:rashikarajesh2007@gmail.com)
- 💼 **LinkedIn:** [rashika-rajesh-kannan](https://www.linkedin.com/in/rashika-rajesh-kannan-56a168310/)
- 💻 **GitHub:** [@R7X-doodles](https://github.com/R7X-doodles)

### Support & Feedback

- **📝 Report Issues:** [GitHub Issues](https://github.com/R7X-doodles/student-mental-health-analysis/issues)
- **💬 Discussions:** [GitHub Discussions](https://github.com/R7X-doodles/student-mental-health-analysis/discussions)
- **⭐ Star this repo:** If you find it helpful!
- **🔄 Fork & Share:** Help spread awareness

---

## 🙏 Acknowledgments

### Institution
- **Ramco Institute of Technology** - For providing the platform and resources
- **Department of Computer Science and Engineering** - For academic support
- **CS3361 Data Science Laboratory** - Course framework

### Data & Resources
- **Kaggle Community** - For providing mental health datasets
- **Research Community** - For published studies and frameworks
- **Open Source Community** - For tools and libraries

### Guidance & Support
- **Project Guide** - For mentorship and feedback
- **Faculty Members** - For academic guidance
- **Peer Reviewers** - For valuable suggestions

---

## 📚 References

### Academic Papers

1. Auerbach, R. P., et al. (2018). "Mental disorder comorbidity and suicidal thoughts and behaviors in the World Health Organization World Mental Health Surveys." *International Journal of Methods in Psychiatric Research*, 27(2), e1569.

2. Eisenberg, D., et al. (2017). "Prevalence and correlates of depression, anxiety, and suicidality among university students." *American Journal of Orthopsychiatry*, 77(4), 534-542.

3. Bedewy, D., & Gabriel, A. (2015). "Examining perceptions of academic stress and its sources among university students: The Perception of Academic Stress Scale." *Health Psychology Open*, 2(2).

4. Conley, C. S., et al. (2015). "A meta-analysis of indicated mental health prevention programs for at-risk higher education students." *Journal of Counseling Psychology*, 62(2), 321-338.

### Reports & Guidelines

5. World Health Organization (2022). "Mental Health in the Workplace."

6. American College Health Association (2023). "National College Health Assessment: Reference Group Executive Summary."

7. National Institute of Mental Health (2023). "College Students and Mental Health."

### Datasets

8. Kaggle - Student Mental Health Dataset (2023)

9. Kaggle - University Student Depression Dataset (2024)

---

## 📊 Project Metrics

![GitHub repo size](https://img.shields.io/github/repo-size/R7X-doodles/student-mental-health-analysis)
![GitHub last commit](https://img.shields.io/github/last-commit/R7X-doodles/student-mental-health-analysis)
![GitHub issues](https://img.shields.io/github/issues/R7X-doodles/student-mental-health-analysis)
![GitHub stars](https://img.shields.io/github/stars/R7X-doodles/student-mental-health-analysis)

---

## 🌟 Project Highlights

<div align="center">

### What Makes This Project Stand Out?

| Feature | Description |
|---------|-------------|
| 📊 **Comprehensive Analysis** | 500+ student records, 20+ variables, multiple statistical methods |
| 🎯 **Evidence-Based** | All recommendations backed by rigorous statistical analysis |
| 🖥️ **Interactive Dashboard** | Real-time exploration with Streamlit |
| 📈 **Publication-Ready Viz** | High-quality, professional visualizations |
| 🔬 **Reproducible Research** | Complete pipeline from raw data to insights |
| 💡 **Actionable Insights** | Clear recommendations with implementation timelines |
| 🎓 **Academic Rigor** | Follows scientific methodology and best practices |
| 🌐 **Real-World Impact** | Designed to improve actual student wellbeing |

</div>

---

## 🎓 Academic Context

### Course Information
- **Course Code:** CS3361
- **Course Name:** Data Science Laboratory
- **Credits:** 2
- **Semester:** VII (November 2025)
- **Project Type:** Major Course Project

### Learning Outcomes Demonstrated
✅ Data collection and preprocessing  
✅ Exploratory Data Analysis (EDA)  
✅ Statistical hypothesis testing  
✅ Correlation and regression analysis  
✅ Data visualization techniques  
✅ Dashboard development  
✅ Technical report writing  
✅ Research methodology application  

---

## 🔄 Workflow Overview

```mermaid
graph TD
    A[📥 Data Collection] --> B[🧹 Data Cleaning]
    B --> C[🔍 Exploratory Analysis]
    C --> D[📊 Statistical Testing]
    D --> E[📈 Visualization]
    E --> F[🖥️ Dashboard Development]
    F --> G[📝 Report Generation]
    G --> H[💡 Recommendations]
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#f0e1ff
    style D fill:#e1ffe1
    style E fill:#ffe1e1
    style F fill:#e1ffff
    style G fill:#ffe1f5
    style H fill:#f5ffe1
```

---

## 📸 Visualizations & Results Preview

<div align="center">

### 🎨 Key Visualizations

*Click on any image to view full resolution*

</div>

### 1️⃣ Exploratory Data Analysis

<div align="center">

[![EDA Visualization](outputs/figures/01_exploratory_data_analysis.png)](outputs/figures/01_exploratory_data_analysis.png)

**Comprehensive overview of mental health distributions, demographic breakdowns, and summary statistics**

</div>

---

### 2️⃣ Correlation Analysis

<div align="center">

[![Correlation Heatmap](outputs/figures/02_correlation_analysis.png)](outputs/figures/02_correlation_analysis.png)

**Statistical relationships between all mental health factors with significance markers (*, **, ***)**

</div>

**Key Correlations Identified:**
- 🔴 **Strong Positive:** Workload Stress (r=+0.58), Academic Pressure (r=+0.55)
- 🟢 **Strong Protective:** Peer Support (r=-0.51), Social Networks (r=-0.48)

---

### 3️⃣ Advanced Statistical Visualizations

<div align="center">

[![Advanced Analysis](outputs/figures/03_advanced_visualizations.png)](outputs/figures/03_advanced_visualizations.png)

**Box plots, violin plots, scatter analysis, and distribution comparisons across demographics**

</div>

---

### 4️⃣ Key Findings Summary

<div align="center">

[![Key Findings](outputs/figures/04_key_findings_summary.png)](outputs/figures/04_key_findings_summary.png)

**Executive summary dashboard with critical metrics and insights**

</div>

**Critical Findings Highlighted:**
- ⚠️ 35% of students in high-risk category
- 📊 70% service utilization gap
- 📚 Academic stress as primary risk factor

---

### 5️⃣ Service Utilization Gap Analysis

<div align="center">

[![Service Gap](outputs/figures/service_utilization_gap.png)](outputs/figures/service_utilization_gap.png)

**Visualization of the gap between mental health needs and service usage**

</div>

---

### 📊 Dashboard Interface Preview

**Interactive Streamlit Dashboard Features:**

```
┌────────────────────────────────────────────────────────────────┐
│  🧠 Student Mental Health Analysis Dashboard                   │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  📊 Real-Time Key Metrics                                      │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌──────────┐│
│  │ High Risk   │ │ Service Gap │ │ Awareness   │ │Avg Score ││
│  │    35%      │ │    70%      │ │    60%      │ │  3.2/5   ││
│  │  175/500    │ │ Only 30%    │ │ 300/500     │ │  ⚠️      ││
│  └─────────────┘ └─────────────┘ └─────────────┘ └──────────┘│
│                                                                 │
│  📈 Interactive Visualizations                                 │
│  ├─ Correlation Explorer (hover for details)                   │
│  ├─ Demographic Breakdowns (filterable)                        │
│  ├─ Trend Analysis (time-series)                               │
│  └─ Factor Impact Analysis (sortable)                          │
│                                                                 │
│  🎯 Dynamic Filters                                            │
│  Gender: [All ▼] Year: [All ▼] Dept: [All ▼] CGPA: [All ▼]  │
│                                                                 │
│  📥 Export Options                                             │
│  [📊 Download Chart] [📄 Generate Report] [💾 Export Data]    │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

**Try it yourself:** `streamlit run dashboard/app.py`

---

### 📁 All Visualizations Available

Browse the complete collection in the [`outputs/visulizations/`](outputs/visualizations/) directory:

| Visualization | Description | Format |
|---------------|-------------|--------|
| `01_exploratory_data_analysis.png` | Complete EDA with distributions | PNG, 300 DPI |
| `02_correlation_analysis.png` | Full correlation matrix with p-values | PNG, 300 DPI |
| `03_advanced_visualizations.png` | Statistical plots and comparisons | PNG, 300 DPI |
| `04_key_findings_summary.png` | Executive summary infographic | PNG, 300 DPI |
| `service_utilization_gap.png` | Service gap analysis | PNG, 300 DPI |

**Publication Ready:** All figures are high-resolution (300 DPI) and suitable for academic papers, presentations, and reports.

---

## 🚀 Advanced Usage

### Custom Analysis

```python
from src.mental_health_analyzer import MentalHealthAnalyzer
import pandas as pd

# Initialize with custom parameters
analyzer = MentalHealthAnalyzer(
    correlation_method='spearman',
    significance_level=0.01,
    outlier_threshold=2.0
)

# Load data
data = pd.read_csv('data/raw/student_mental_health.csv')
analyzer.load_data(data)

# Run specific analyses
results = analyzer.run_analysis(
    include=['correlation', 'hypothesis_testing', 'regression'],
    export_format='pdf',
    output_dir='outputs/custom_analysis/'
)

# Generate custom visualizations
analyzer.create_custom_plot(
    x='academic_pressure',
    y='mental_health_score',
    hue='gender',
    kind='scatter',
    regression=True
)
```

### Batch Processing

```python
# Analyze multiple datasets
datasets = ['dataset1.csv', 'dataset2.csv', 'dataset3.csv']

for dataset in datasets:
    analyzer = MentalHealthAnalyzer()
    analyzer.load_data(f'data/raw/{dataset}')
    analyzer.run_complete_analysis()
    analyzer.export_results(f'outputs/{dataset}_results/')
```

### API Usage (Dashboard)

```python
# Access dashboard programmatically
from dashboard.utils import get_analysis_results

# Get filtered results
results = get_analysis_results(
    filters={
        'gender': 'Female',
        'year': [3, 4],
        'cgpa_min': 3.0
    }
)

# Export to various formats
results.export_to_excel('filtered_analysis.xlsx')
results.export_to_json('filtered_analysis.json')
```

---

## 📋 Data Dictionary

### Mental Health Indicators

| Variable | Type | Scale | Description |
|----------|------|-------|-------------|
| `mental_health_score` | Continuous | 1-5 | Overall mental health rating (1=excellent, 5=poor) |
| `anxiety_level` | Continuous | 1-5 | Self-reported anxiety (1=minimal, 5=severe) |
| `depression_score` | Continuous | 1-5 | Depression symptoms (1=minimal, 5=severe) |
| `stress_level` | Continuous | 1-5 | Perceived stress (1=low, 5=high) |
| `sleep_quality` | Continuous | 1-5 | Sleep satisfaction (1=excellent, 5=poor) |
| `emotional_wellbeing` | Continuous | 1-5 | Emotional state (1=positive, 5=negative) |

### Academic Factors

| Variable | Type | Scale | Description |
|----------|------|-------|-------------|
| `academic_pressure` | Continuous | 1-5 | Perceived academic pressure |
| `workload_stress` | Continuous | 1-5 | Stress from course workload |
| `exam_anxiety` | Continuous | 1-5 | Test-related anxiety |
| `performance_expectations` | Continuous | 1-5 | Self/external expectations |

### Demographics

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| `age` | Integer | 18-25 | Student age in years |
| `gender` | Categorical | Male/Female/Other | Gender identity |
| `year` | Categorical | 1/2/3/4 | Academic year |
| `department` | Categorical | CSE/ECE/MECH/etc. | Department enrolled |
| `cgpa` | Continuous | 0.0-10.0 | Cumulative GPA |

### Support & Environment

| Variable | Type | Scale | Description |
|----------|------|-------|-------------|
| `peer_relationships` | Continuous | 1-5 | Quality of peer connections |
| `social_support` | Continuous | 1-5 | Perceived support network |
| `campus_environment` | Continuous | 1-5 | Campus quality rating |
| `recreational_facilities` | Continuous | 1-5 | Access to recreation |

### Service Utilization

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| `service_awareness` | Binary | Yes/No | Aware of mental health services |
| `service_usage` | Binary | Yes/No | Used mental health services |
| `service_satisfaction` | Continuous | 1-5 | Satisfaction with services |

---

## 🧪 Testing

### Run Unit Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_statistical_analysis.py

# Run with coverage report
python -m pytest --cov=src tests/
 |

---

## 🐛 Troubleshooting

### Common Issues

**Issue 1: Module Import Errors**
```bash
# Solution: Ensure you're in the project root and virtual environment is activated
cd student-mental-health-analysis
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

**Issue 2: Dashboard Won't Start**
```bash
# Solution: Check if port 8501 is available
streamlit run dashboard/app.py --server.port 8502
```

**Issue 3: Matplotlib Display Issues**
```python
# Add to top of notebook
%matplotlib inline
import matplotlib
matplotlib.use('Agg')  # For non-GUI backends
```

**Issue 4: Memory Errors with Large Datasets**
```python
# Solution: Use chunking
analyzer.load_data('data.csv', chunksize=1000)
```

---

## 🔐 Data Privacy & Ethics

### Ethical Considerations

✅ **Anonymization:** All personal identifiers removed  
✅ **Consent:** Data collected with informed consent  
✅ **Confidentiality:** Individual responses kept confidential  
✅ **Aggregation:** Results reported at group level only  
✅ **Storage:** Secure data storage practices  
✅ **Usage:** Data used solely for research purposes  

### Data Security

- No personally identifiable information (PII) in datasets
- Secure storage with access controls
- Compliance with institutional review board (IRB) guidelines
- Data retention policy: 5 years post-publication

---

## 📅 Project Timeline

### Development Phases

```
Phase 1: Planning & Data Collection (Week 1-2)
├── Problem identification
├── Literature review
├── Data collection strategy
└── IRB approval

Phase 2: Data Preparation (Week 3-4)
├── Data cleaning
├── Feature engineering
├── Quality validation
└── Documentation

Phase 3: Analysis (Week 5-7)
├── Exploratory analysis
├── Statistical testing
├── Correlation analysis
└── Regression modeling

Phase 4: Visualization & Dashboard (Week 8-9)
├── Create visualizations
├── Dashboard development
├── Testing & refinement
└── Documentation

Phase 5: Report & Presentation (Week 10-11)
├── Write comprehensive report
├── Create presentation
├── Prepare demonstration
└── Final review

Phase 6: Deployment & Documentation (Week 12)
├── GitHub repository setup
├── README creation
├── Code documentation
└── Project submission
```

---

## 🎯 Future Enhancements

### Planned Features

- [ ] **Machine Learning Models**
  - Predictive models for mental health risk
  - Classification algorithms for risk categories
  - Time-series forecasting

- [ ] **Enhanced Dashboard**
  - User authentication
  - Personalized recommendations
  - Mobile app version
  - Real-time data updates

- [ ] **Additional Analyses**
  - Network analysis of social support
  - Sentiment analysis of open-ended responses
  - Geospatial analysis of campus hotspots
  - Longitudinal trend analysis

- [ ] **Integration Features**
  - API for institutional systems
  - Integration with student information systems
  - Automated reporting to administrators
  - Alert system for high-risk students

- [ ] **Expanded Data Collection**
  - Mobile app for continuous monitoring
  - Wearable device integration
  - Social media sentiment analysis
  - Academic performance tracking

### Version Roadmap

**v2.0** (Q1 2026)
- Machine learning integration
- Enhanced dashboard features
- Mobile application

**v3.0** (Q3 2026)
- Real-time monitoring system
- Predictive analytics
- Integration APIs

---

## 💬 FAQ

**Q: Can I use this project for my own research?**  
A: Yes! This project is open-source under MIT License. Please cite appropriately.

**Q: How do I adapt this for my institution?**  
A: Fork the repository, replace the dataset with your data, and run the analysis pipeline. The code is designed to be modular and adaptable.

**Q: What sample size do I need?**  
A: Minimum 200-300 students for reliable statistical analysis. Larger samples provide more robust insights.

**Q: Can I add more variables?**  
A: Absolutely! The analyzer is designed to handle additional variables. Just ensure proper data formatting.

**Q: How do I interpret correlation coefficients?**  
A: 
- 0.0-0.3: Weak correlation
- 0.3-0.5: Moderate correlation
- 0.5-0.7: Strong correlation
- 0.7-1.0: Very strong correlation

**Q: Is the dashboard mobile-friendly?**  
A: Yes, the Streamlit dashboard is responsive and works on mobile devices.

**Q: How often should surveys be conducted?**  
A: We recommend semester-based surveys (2-3 times per year) for trend monitoring.

---

## 📞 Support

### Get Help

- 📧 **Email:** rashikarajesh2007@gmail.com
- 💬 **Discussions:** [GitHub Discussions](https://github.com/R7X-doodles/student-mental-health-analysis/discussions)
- 🐛 **Bug Reports:** [GitHub Issues](https://github.com/R7X-doodles/student-mental-health-analysis/issues)
- 📖 **Documentation:** [Wiki](https://github.com/R7X-doodles/student-mental-health-analysis/wiki)

### Response Time

- Feature requests: 1-2 weeks
- General questions: 3-5 days

---

## 🏆 Recognition & Impact

### Potential Applications

- 🎓 **Academic Institutions:** Mental health program development
- 🏥 **Healthcare:** Student mental health research
- 📊 **Policy Making:** Evidence-based policy decisions
- 🔬 **Research:** Foundation for further studies
- 💼 **Counseling Centers:** Resource allocation planning

### Skills Demonstrated

✅ Data Science & Analytics  
✅ Statistical Analysis  
✅ Python Programming  
✅ Data Visualization  
✅ Dashboard Development  
✅ Research Methodology  
✅ Technical Writing  
✅ Project Management  

---

## 📜 Citation

If you use this project in your research, please cite:

```bibtex
@misc{rashika2025mentalhealth,
  author = {Rashika R},
  title = {Student Mental Health Analysis: A Data Science Approach},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/R7X-doodles/student-mental-health-analysis}},
  note = {Course Project: CS3361 Data Science Laboratory, Ramco Institute of Technology}
}
```

---

## ⚖️ Disclaimer

This project is for educational and research purposes. The findings and recommendations should be:
- Reviewed by mental health professionals
- Adapted to local contexts
- Validated with institutional policies
- Implemented with proper oversight

**This is not a substitute for professional mental health care or clinical diagnosis.**

---

<div align="center">

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=R7X-doodles/student-mental-health-analysis&type=Date)](https://star-history.com/#R7X-doodles/student-mental-health-analysis&Date)

---

### 💝 Show Your Support

If this project helped you or you found it interesting, please consider:

⭐ **Starring the repository**  
🔄 **Sharing with others**  
🐛 **Reporting issues**  
💡 **Suggesting improvements**  
🤝 **Contributing code**

---

### 📢 Stay Updated

Watch this repository to get notifications about:
- 🆕 New features and updates
- 🐛 Bug fixes
- 📊 New visualizations
- 📝 Documentation improvements

---

**Made with ❤️ for student wellbeing**

*Improving mental health, one data point at a time*

---

**Last Updated:** December 2025  
**Version:** 1.0.0  
**Status:** ✅ Active Development

</div>
