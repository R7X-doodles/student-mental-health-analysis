@echo off
echo ========================================
echo Organizing Repository...
echo ========================================

REM Create folders
mkdir data\raw 2>nul
mkdir data\processed 2>nul
mkdir dashboard 2>nul
mkdir notebooks 2>nul

REM Move CSV files to data/raw
echo Moving raw data files...
move "Student Mental health.csv" data\raw\ 2>nul
move student_depression_dataset.csv data\raw\ 2>nul
move students_mental_health_survey.csv data\raw\ 2>nul

REM Move processed data
echo Moving processed files...
move combined_mental_health_data.csv data\processed\ 2>nul
move processed_mental_health_data.csv data\processed\ 2>nul

REM Remove duplicate PNGs from root
echo Cleaning duplicate files...
del 01_exploratory_data_analysis.png 2>nul
del 02_correlation_analysis.png 2>nul
del 03_advanced_visualizations.png 2>nul
del 04_key_findings_summary.png 2>nul

REM Move dashboard
echo Moving dashboard...
move src\dashboard.py dashboard\app.py 2>nul

REM Clean up docs
del UPLOAD_CHECKLIST.md 2>nul
del SETUP.md 2>nul
move PROJECT_SUMMARY.md docs\ 2>nul

echo.
echo ========================================
echo ✅ Organization Complete!
echo ========================================
echo.
echo Next: Update file paths in your code
pause