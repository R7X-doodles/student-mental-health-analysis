import os

# Update mental_health_analysis.py
with open('src/mental_health_analysis.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "df = load_data('combined_mental_health_data.csv')",
    "df = load_data('../data/processed/combined_mental_health_data.csv')"
)
content = content.replace(
    "plt.savefig('01_exploratory_data_analysis.png'",
    "plt.savefig('../outputs/visualizations/01_exploratory_data_analysis.png'"
)
content = content.replace(
    "plt.savefig('02_correlation_analysis.png'",
    "plt.savefig('../outputs/visualizations/02_correlation_analysis.png'"
)
content = content.replace(
    "plt.savefig('03_advanced_visualizations.png'",
    "plt.savefig('../outputs/visualizations/03_advanced_visualizations.png'"
)
content = content.replace(
    "plt.savefig('04_key_findings_summary.png'",
    "plt.savefig('../outputs/visualizations/04_key_findings_summary.png'"
)
content = content.replace(
    "output_file = 'processed_mental_health_data.csv'",
    "output_file = '../data/processed/processed_mental_health_data.csv'"
)

with open('src/mental_health_analysis.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated mental_health_analysis.py")

# Update dataset_combiner.py
with open('src/dataset_combiner.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "output_filename='combined_mental_health_data.csv'",
    "output_filename='../data/processed/combined_mental_health_data.csv'"
)

with open('src/dataset_combiner.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated dataset_combiner.py")

# Update dashboard/app.py
with open('dashboard/app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add DATA_PATH after imports
if "DATA_PATH = " not in content:
    content = content.replace(
        "import numpy as np",
        "import numpy as np\n\n# Data path\nDATA_PATH = '../data/processed/processed_mental_health_data.csv'"
    )

# Update load_data function
old_func = """@st.cache_data
def load_data():
    np.random.seed(42)"""

new_func = """@st.cache_data
def load_data():
    # Try to load real data first
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except FileNotFoundError:
        pass
    
    # Generate sample data
    np.random.seed(42)"""

content = content.replace(old_func, new_func)

with open('dashboard/app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated app.py")
print("\n✅ All files updated successfully!")