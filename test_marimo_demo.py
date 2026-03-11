from marimo_demo import vg_dataset
import pandas as pd
import marimo as mo

def test_vg_sales_data():
    vg_sales = vg_dataset(pd)
    assert len(vg_sales.columns) == 11
def test_vg_sales_agg():
    vg_sales_agg = mo.sql("""
        SELECT 
            Name, 
            SUM(NA_Sales) AS Total_NA_Sales, 
            SUM(EU_Sales) AS Total_EU_Sales, 
            SUM(JP_Sales) AS Total_JP_Sales, 
            SUM(Other_Sales) AS Total_Other_Sales, 
            SUM(Global_Sales) AS Total_Global_Sales
        FROM "./data/vgsales.csv"
        GROUP BY Name
        """, output = False)
    assert len(vg_sales_agg.columns) == 6
