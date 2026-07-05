# Campus Placement Data Analyzer

A Python data pipeline that analyzes campus placement trends 
and generates automated insights with visualizations.

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- PDF Export (matplotlib PdfPages)

## What It Does
- Cleans and processes 215 student placement records
- Generates 10 automated insights from raw data
- Produces 5 visualizations (pie, bar, scatter charts)
- Exports a professional PDF report

## Key Insights Generated
- Overall placement rate: 68.84%
- Students with work experience placed at 86.49% vs 59.57% without
- Best paying specialisation: Mkt&Fin
- Best paying degree type: Sci&Tech
- Highest salary offered: Rs 9,40,000

## How to Run
```bash
pip install pandas numpy matplotlib seaborn
python analyse.py
```