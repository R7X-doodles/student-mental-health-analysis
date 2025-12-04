# 🧠 Student Mental Health Analysis

> **A comprehensive data science approach to understanding and improving campus wellness**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

**Author:** Rashika R (953624104122)  
**Institution:** Ramco Institute of Technology  
**Course:** CS3361 Data Science Laboratory  
**Date:** November 2025

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Findings](#key-findings)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [Recommendations](#recommendations)
- [Technologies](#technologies)
- [Dashboard](#dashboard)
- [Contact](#contact)

---

## 🔍 Overview

This project investigates the critical relationships between campus environment, academic expectations, and student mental health to provide evidence-based recommendations for establishing a comprehensive campus mental health center.

### Problem Statement

Current campus mental health support systems suffer from:
- ❌ Insufficient awareness about available services
- ❌ Limited counseling resources relative to student needs
- ❌ Lack of data-driven understanding of primary stressors
- ❌ Inadequate integration between academic and mental health support

### Objectives

1. Analyze relationships between campus environment and student mental health
2. Quantify the impact of academic expectations on psychological well-being
3. Identify service utilization gaps and barriers
4. Provide evidence-based recommendations for a campus mental health center
5. Develop an interactive dashboard for ongoing monitoring

---

## 🎯 Key Findings

### Critical Statistics

| Metric | Value | Implication |
|--------|-------|-------------|
| **High-Risk Students** | 35% (175/500) | 1 in 3 students needs immediate intervention |
| **Service Utilization Gap** | 70% | Only 30% seeking help despite high need |
| **Service Awareness Gap** | 40% | 200 students unaware of available services |
| **Academic Pressure Impact** | r = +0.52*** | Strongest predictor of poor mental health |
| **Campus Environment Effect** | r = -0.45*** | Strong protective factor |

*\*\*\* p < 0.001 (highly significant)*

### Top 5 Discoveries

1. **📊 Prevalence Crisis**: 35% of students in high-risk mental health categories
2. **🚨 Service Gap**: Massive 70% utilization gap despite high need
3. **📚 Academic Stress**: Workload stress is the #1 predictor (r = +0.58)
4. **🏛️ Environment Matters**: Campus quality significantly protects mental health
5. **👥 Peer Support**: Strongest protective factor (r = -0.51)

---

## 📁 Project Structure

```
student-mental-health-analysis/
│
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── LICENSE                            # MIT License
├── .gitignore                        # Git ignore file
│
├── 📂 data/
│   ├── README.md                     # Data dictionary
│   ├── raw/                          # Original datasets
│   │   └── student_mental_health.csv
│   └── processed/                    # Cleaned datasets
│       └── cleaned_data.csv
│
├── 📂 notebooks/
│   ├── 01_data_cleaning.ipynb       # Data preprocessing
│   ├── 02_exploratory_analysis.ipynb # EDA
│   ├── 03_statistical_analysis.ipynb # Correlations & tests
│   └── 04_visualizations.ipynb      # Generate plots
│
├── 📂 src/
│   ├── __init__.py
│   ├── mental_health_analyzer.py    # Main analysis class
│   ├── data_processing.py           # Data cleaning functions
│   ├── statistical_analysis.py      # Analysis functions
│   └── visualization.py             # Plotting functions
│
├── 📂 outputs/
│   ├── figures/                     # All visualizations
│   │   ├── 01_exploratory_data_analysis.png
│   │   ├── 02_correlation_analysis.png
│   │   ├── 03_advanced_visualizations.png
│   │   ├── 04_key_findings_summary.png
│   │   └── service_utilization_gap.png
│   └── reports/
│       ├── analysis_report.txt
│       └── final_report.pdf
│
├── 📂 dashboard/
│   ├── app.py                       # Streamlit dashboard
│   ├── config.py                    # Configuration
│   └── utils.py                     # Helper functions
│
└── 📂 docs/
    ├── project_report.pdf           # Full project report
    ├── presentation.pptx            # Review presentation
    └── methodology.md               # Detailed methodology
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/R7X-doodles/student-mental-health-analysis.git
cd student-mental-health-analysis

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Requirements

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
plotly>=5.17.0
streamlit>=1.28.0
scikit-learn>=1.2.0
```

---

## 💻 Usage

### Running the Analysis

```python
from src.mental_health_analyzer import MentalHealthAnalyzer

# Initialize analyzer
analyzer = MentalHealthAnalyzer()

# Load data
analyzer.load_data('data/raw/student_mental_health.csv')

# Preprocess
analyzer.preprocess_data()

# Run analyses
analyzer.correlation_analysis(method='pearson')
analyzer.hypothesis_testing()
analyzer.calculate_risk_categories()

# Generate visualizations
analyzer.visualize_correlation_heatmap()
analyzer.visualize_distributions()

# Create report
analyzer.generate_report()
```

### Running the Dashboard

```bash
streamlit run dashboard/app.py
```

Access at: `http://localhost:8501`

---

## 🔬 Methodology

### Data Collection

- **Sample Size**: 500 students
- **Data Sources**: Primary surveys + Kaggle datasets
- **Variables**: 20+ indicators across 5 categories

### Statistical Methods

#### Descriptive Statistics
- Central tendency (mean, median, mode)
- Dispersion (SD, variance)
- Distribution analysis (skewness, kurtosis)

#### Inferential Statistics
- **Pearson Correlation**: Linear relationships
- **Spearman Correlation**: Non-parametric associations
- **Independent t-tests**: Gender comparisons
- **ANOVA**: Year-wise differences
- **Chi-square tests**: Categorical associations

### Data Processing Pipeline

```
Raw Data → Cleaning → Feature Engineering → Statistical Analysis → Visualization
```

**Key Steps:**
1. Missing value imputation (median method)
2. Outlier detection (IQR method, threshold=1.5)
3. Composite score creation
4. Data validation

---

## 📊 Results

### Mental Health Distribution

- **Good (1-2)**: 20% of students
- **Moderate (2-3)**: 30% of students
- **Poor (3-4)**: 25% of students
- **Severe (4-5)**: 25% of students

### Strongest Correlations

| Factor | Correlation | p-value | Interpretation |
|--------|-------------|---------|----------------|
| Workload Stress | r = +0.58 | < 0.001 | Strong positive |
| Academic Pressure | r = +0.55 | < 0.001 | Strong positive |
| Peer Relationships | r = -0.51 | < 0.001 | Strong protective |
| Social Support | r = -0.48 | < 0.001 | Strong protective |
| Campus Environment | r = -0.45 | < 0.001 | Moderate protective |

### Hypothesis Testing

- **Gender**: Females report significantly higher anxiety (t=3.24, p=0.001)
- **Year**: 3rd/4th year students show highest stress (F=6.78, p<0.001)
- **CGPA**: Negative correlation with mental health problems (r=-0.28)

---

## 💡 Recommendations

### Immediate Actions (0-6 Months)

1. **Staffing**
   - Hire 2-3 professional counselors
   - Establish dedicated counseling space
   - Implement booking system

2. **Awareness Campaign**
   - Launch digital campaign
   - Distribute materials
   - Host Mental Health Awareness Week
   - **Target**: 90% awareness

3. **Needs Assessment**
   - Conduct surveys
   - Organize focus groups
   - Establish baseline metrics

### Short-term (6-12 Months)

1. **Mental Health Center**
   - Multi-room facility
   - Expanded staffing
   - Telemedicine capabilities

2. **Peer Support Program**
   - Train 20-30 peer counselors
   - Establish support groups
   - Buddy system for first-years

3. **Screening Programs**
   - Semester screenings
   - Early identification
   - Integration with health services

### Long-term (1-3 Years)

1. **Service Expansion**
   - Individual & group therapy
   - 24/7 crisis helpline
   - Psychiatric services

2. **Academic Integration**
   - Workload policy review
   - Mental health accommodations
   - Faculty training

3. **Continuous Monitoring**
   - Quarterly surveys
   - Effectiveness evaluation
   - Data-driven adjustments

### Expected Outcomes (3-Year Targets)

| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| High-risk students | 35% | 18% | -50% |
| Service utilization | 30% | 65% | +117% |
| Service awareness | 60% | 90% | +50% |
| Mental health score | 3.2/5 | 2.4/5 | -25% |

### Budget Estimate

**Annual Cost**: $480,000 - $850,000

- Personnel: $300K-500K
- Facility: $100K-200K
- Programs: $50K-100K
- Technology: $30K-50K

---

## 🛠️ Technologies

### Core Technologies

- **Python 3.8+**: Primary language
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **SciPy**: Statistical analysis

### Visualization

- **Matplotlib**: Static plots
- **Seaborn**: Statistical graphics
- **Plotly**: Interactive charts

### Web Framework

- **Streamlit**: Dashboard application

### Development Tools

- **Jupyter**: Notebooks for analysis
- **Git**: Version control
- **VS Code**: IDE

---

## 📱 Dashboard

The interactive dashboard provides five main sections:

### 1. Overview & Metrics
- Key statistics display
- Mental health distribution
- Service gap visualization

### 2. Correlation Explorer
- Interactive correlation matrix
- Significance testing
- Variable relationships

### 3. Trends & Comparisons
- Year-wise analysis
- Gender comparisons
- Demographic breakdowns

### 4. Factor Analysis
- Individual factor impacts
- Scatter plots with trends
- Distribution comparisons

### 5. Recommendations
- Evidence-based suggestions
- Implementation timeline
- Expected outcomes

### Dashboard Features

✅ Real-time filtering by demographics  
✅ Interactive visualizations  
✅ Downloadable reports  
✅ Mobile-responsive design  
✅ Export capabilities

---

## 📈 Visualizations

### Sample Outputs

All visualizations are available in `outputs/figures/`:

1. **Exploratory Data Analysis**: Distribution plots, demographics
2. **Correlation Heatmap**: Complete correlation matrix
3. **Service Gap**: Utilization gap visualization
4. **Academic Stress**: Regression analysis plots
5. **Advanced Analysis**: Box plots, violin plots, radar charts
6. **Key Findings**: Executive summary infographic

---

## 📄 Documentation

Complete documentation available in `/docs`:

- **Project Report** (32 pages): Comprehensive analysis
- **Methodology**: Detailed statistical methods
- **Data Dictionary**: Variable descriptions
- **Review Talking Points**: Presentation guide

---

## 🤝 Contributing

While this is an academic project, feedback and suggestions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📧 Contact

**Rashika R**

- 🎓 Roll No: 953624104122
- 🏛️ Institution: Ramco Institute of Technology
- 📚 Department: Computer Science and Engineering
- 📧 Email: rashikarajesh2007@gmail.com
- 💼 LinkedIn: [rashika-rajesh-kannan](https://www.linkedin.com/in/rashika-rajesh-kannan-56a168310/)
- 💻 GitHub: [@R7X-doodles](https://github.com/R7X-doodles)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Institution**: Ramco Institute of Technology
- **Department**: Computer Science and Engineering
- **Course**: CS3361 Data Science Laboratory
- **Project Guide**: [Faculty Name]
- **Data Sources**: Kaggle Student Mental Health Datasets
- **Inspiration**: Commitment to improving student wellbeing

---

## 📚 References

1. Auerbach, R. P., et al. (2018). Mental disorder comorbidity and suicidal thoughts. *International Journal of Methods in Psychiatric Research*.

2. Eisenberg, D., et al. (2017). Prevalence and correlates of depression, anxiety, and suicidality. *American Journal of Orthopsychiatry*.

3. Bedewy, D., & Gabriel, A. (2015). Academic stress among university students. *Health Psychology Open*.

4. WHO (2022). Mental Health in the Workplace.

5. ACHA (2023). National College Health Assessment.

---

## 🌟 Project Highlights

- ✅ Comprehensive statistical analysis
- ✅ Interactive dashboard
- ✅ Reproducible research pipeline
- ✅ Evidence-based recommendations
- ✅ Professional documentation
- ✅ Real-world impact potential

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ for student wellbeing

</div>