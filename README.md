# Sales Data Analysis (Beginner Python Project)

## Project overview
This beginner project demonstrates how to read a CSV file, inspect and clean data, calculate revenue, summarize product performance, and visualize monthly sales using Python.

**Important:** `sales_data.csv` is a small illustrative sample dataset created for practice. Its results are not real business findings.

## Tools
- Python
- pandas
- matplotlib

## Dataset columns
- `Date`: date of the sample transaction
- `Product`: product name
- `Category`: product category
- `Quantity`: units sold
- `UnitPrice`: price per unit in Indian rupees
- `Region`: sample sales region

## How to run
1. Install Python 3.
2. Open a terminal in this project folder.
3. Install the libraries:

   ```bash
   python -m pip install pandas matplotlib
   ```

4. Run the script:

   ```bash
   python sales_analysis.py
   ```

5. Review the printed summaries and the files created in the `outputs` folder.

## Questions explored
- What is the total revenue in this sample dataset?
- Which products have the highest revenue?
- How does revenue vary by month?

## Project structure
```text
Sales-Data-Analysis/
├── sales_data.csv
├── sales_analysis.py
├── requirements.txt
└── README.md
```

## Learning outcomes
- Loading CSV data with pandas
- Checking missing values and duplicate rows
- Creating a calculated revenue column
- Grouping and resampling data
- Saving summary tables and charts

## Next improvements
- Practice writing SQL queries against a dataset.
- Build an Excel or Power BI dashboard.
- Use a larger, clearly documented dataset and compare results.
