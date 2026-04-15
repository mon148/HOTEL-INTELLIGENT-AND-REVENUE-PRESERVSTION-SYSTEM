@echo off
echo ===
echo 🏨 Hotel Intelligence System - Automated Setup
echo ===

:: Create Virtual Environment
echo [1/3] Creating Virtual Environment...
python -m venv .venv

::Install Requirements
echo [2/3] Installing Dependencies (This may take a minute)...
.\.venv\Scripts\pip install -r requirements.txt

::Run the App
echo [3/3] Launching Dashboard...
echo ---------------------------------------------------------
.\.venv\Scripts\streamlit run web.py

pause