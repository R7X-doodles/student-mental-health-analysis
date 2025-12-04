@echo off
echo ================================================================
echo Student Mental Health Analysis - Repository Organization
echo ================================================================
echo.

REM Step 1: Create folder structure
echo [1/4] Creating folder structure...
if not exist "data" mkdir data
if not exist "data\raw" mkdir data\raw
if not exist "data\processed" mkdir data\processed
if not exist "dashboard" mkdir dashboard
if not exist "notebooks" mkdir notebooks
echo     - Created data/raw
echo     - Created data/processed
echo     - Created dashboard
echo     - Created notebooks
echo.

REM Step 2: Move CSV files
echo [2/4] Moving data files...
if exist "Student Mental health.csv" (
    move "Student Mental health.csv" data\raw\ >nul 2>&1
    echo     - Moved "Student Mental health.csv"
)
if exist "student_depression_dataset.csv" (
    move student_depression_dataset.csv data\raw\ >nul 2>&1
    echo     - Moved student_depression_dataset.csv
)
if exist "students_mental_health_survey.csv" (
    move students_mental_health_survey.csv data\raw\ >nul 2>&1
    echo     - Moved students_mental_health_survey.csv
)
if exist "combined_mental_health_data.csv" (
    move combined_mental_health_data.csv data\processed\ >nul 2>&1
    echo     - Moved combined_mental_health_data.csv
)
if exist "processed_mental_health_data.csv" (
    move processed_mental_health_data.csv data\processed\ >nul 2>&1
    echo     - Moved processed_mental_health_data.csv
)
echo.

REM Step 3: Clean up duplicate PNGs
echo [3/4] Cleaning up duplicate files...
del 01_exploratory_data_analysis.png >nul 2>&1
del 02_correlation_analysis.png >nul 2>&1
del 03_advanced_visualizations.png >nul 2>&1
del 04_key_findings_summary.png >nul 2>&1
echo     - Removed duplicate visualizations
echo.

REM Step 4: Move dashboard if it exists in src
if exist "src\dashboard.py" (
    move src\dashboard.py dashboard\app.py >nul 2>&1
    echo     - Moved dashboard to dashboard/app.py
)
echo.

REM Step 5: Update Python files using PowerShell
echo [4/4] Updating file paths in Python scripts...

REM Update mental_health_analysis.py
powershell -Command "(Get-Content 'src\mental_health_analysis.py') -replace \"df = load_data\('combined_mental_health_data.csv'\)\", \"df = load_data('../data/processed/combined_mental_health_data.csv')\" | Set-Content 'src\mental_health_analysis.py'"

powershell -Command "(Get-Content 'src\mental_health_analysis.py') -replace \"plt\.savefig\('01_exploratory_data_analysis\.png'\", \"plt.savefig('../outputs/visualizations/01_exploratory_data_analysis.png'\" | Set-Content 'src\mental_health_analysis.py'"

powershell -Command "(Get-Content 'src\mental_health_analysis.py') -replace \"plt\.savefig\('02_correlation_analysis\.png'\", \"plt.savefig('../outputs/visualizations/02_correlation_analysis.png'\" | Set-Content 'src\mental_health_analysis.py'"

powershell -Command "(Get-Content 'src\mental_health_analysis.py') -replace \"plt\.savefig\('03_advanced_visualizations\.png'\", \"plt.savefig('../outputs/visualizations/03_advanced_visualizations.png'\" | Set-Content 'src\mental_health_analysis.py'"

powershell -Command "(Get-Content 'src\mental_health_analysis.py') -replace \"plt\.savefig\('04_key_findings_summary\.png'\", \"plt.savefig('../outputs/visualizations/04_key_findings_summary.png'\" | Set-Content 'src\mental_health_analysis.py'"

powershell -Command "(Get-Content 'src\mental_health_analysis.py') -replace \"output_file = 'processed_mental_health_data\.csv'\", \"output_file = '../data/processed/processed_mental_health_data.csv'\" | Set-Content 'src\mental_health_analysis.py'"

echo     - Updated src/mental_health_analysis.py (6 paths)

REM Update dataset_combiner.py
powershell -Command "(Get-Content 'src\dataset_combiner.py') -replace \"output_filename='combined_mental_health_data\.csv'\", \"output_filename='../data/processed/combined_mental_health_data.csv'\" | Set-Content 'src\dataset_combiner.py'"

echo     - Updated src/dataset_combiner.py (1 path)

REM Update dashboard/app.py if it exists
if exist "dashboard\app.py" (
    powershell -Command "(Get-Content 'dashboard\app.py') -replace 'import numpy as np', 'import numpy as np`n`n# Data path`nDATA_PATH = ''../data/processed/processed_mental_health_data.csv''' | Set-Content 'dashboard\app.py'"
    
    powershell -Command "(Get-Content 'dashboard\app.py') -replace '@st\.cache_data\ndef load_data\(\):\s+np\.random\.seed', '@st.cache_data`ndef load_data():`n    # Try to load real data first`n    try:`n        df = pd.read_csv(DATA_PATH)`n        return df`n    except FileNotFoundError:`n        pass`n    `n    # Generate sample data`n    np.random.seed' | Set-Content 'dashboard\app.py'"
    
    echo     - Updated dashboard/app.py (2 changes)
)

echo.
echo ================================================================
echo ORGANIZATION COMPLETE!
echo ================================================================
echo.
echo Your repository is now properly organized:
echo.
echo   data/raw/              - Original CSV files
echo   data/processed/        - Processed data files
echo   outputs/visualizations/ - PNG visualizations
echo   dashboard/             - Dashboard application
echo.
echo Next steps:
echo   1. Test the analysis: cd src ^&^& python mental_health_analysis.py
echo   2. Test dashboard: streamlit run dashboard/app.py
echo   3. Commit changes: git add . ^&^& git commit -m "Repository organization"
echo   4. Push to GitHub: git push
echo.
echo ================================================================
pause