import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    return mo, np, pd, plt


@app.cell
def _(mo):
    A = mo.ui.slider(start = -10, stop = 10, value = 1, step = 0.25, label = "A", show_value = True)
    omega = mo.ui.slider(start = 0, stop = 10, value = 1, step = 0.25, label = r"$\omega$", show_value = True)
    phi = mo.ui.slider(start = -10, stop = 10, value = 0, step = 0.25, label = r"$\phi$", show_value = True)
    B = mo.ui.slider(start = -10, stop = 10, value = 0, step = 0.25, label = "B", show_value = True)
    return A, B, omega, phi


@app.cell
def _(A, B, mo, omega, phi):
    mo.vstack([A, omega, phi, B])
    return


@app.cell
def _(A, B, mo, omega, phi):
    mo.md(
        f"""
    The amplitude is {A.value} \n
    The angular frequency is {omega.value} \n
    The phase shift is {phi.value} \n
    The intercept is {B.value} \n
    """
    )
    return


@app.cell
def _(A, B, np, omega, phi):
    t = np.arange(0, 20, 0.06)
    y = A.value * np.cos(omega.value * t + phi.value) + B.value
    return t, y


@app.cell
def _(plt, t, y):
    plt.figure(figsize=(10,6))
    plt.plot(t, y)
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("Response")
    plt.grid(True)
    plt.show()
    return


@app.cell
def _(pd):
    vg_sales = pd.read_csv("./data/vgsales.csv")
    vg_sales
    return (vg_sales,)


@app.cell
def _(mo, vg_sales):
    vg_sales_agg = mo.sql(
        f"""
        SELECT 
            Name, 
            SUM(NA_Sales) AS Total_NA_Sales, 
            SUM(EU_Sales) AS Total_EU_Sales, 
            SUM(JP_Sales) AS Total_JP_Sales, 
            SUM(Other_Sales) AS Total_Other_Sales, 
            SUM(Global_Sales) AS Total_Global_Sales
        FROM vg_sales
        GROUP BY Name
        """
    )
    return


@app.cell
def _(pd, vg_sales):
    vg_sales["Category of Global Sales"] = pd.cut(vg_sales["Global_Sales"], bins = 5, labels = ["Very Low", "Low", "Medium", "High", "Very High"])
    vg_sales
    return


if __name__ == "__main__":
    app.run()
