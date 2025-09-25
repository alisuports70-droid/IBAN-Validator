# IBAN Validator

A professional Python project to validate International Bank Account Numbers (IBANs) with both **single** and **batch validation**.

## Features
- Validates IBANs from multiple countries (DE, PK, FR, GB, etc.)
- Checks IBAN length, characters, checksum, and country code
- Batch validation via Streamlit web interface
- Professional unit tests with `pytest`

## How to Run

### 1. Run tests
```bash
pip install -r requirements.txt
pytest -v

git init
git add .
git commit -m "Initial commit - IBAN Validator project"
git branch -M main
git remote add origin https://github.com/alisuports70-droid/IBAN-Validator
git push -u origin main


