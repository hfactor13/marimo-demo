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
    A = mo.ui.slider(start = -10, stop = 10, value = 1, step = 0.25, label = "A", show_value = True, include_input = True)
    omega = mo.ui.slider(start = 0, stop = 10, value = 1, step = 0.25, label = r"$\omega$", show_value = True, include_input = True)
    phi = mo.ui.slider(start = -10, stop = 10, value = 0, step = 0.25, label = r"$\phi$", show_value = True, include_input = True)
    B = mo.ui.slider(start = -10, stop = 10, value = 0, step = 0.25, label = "B", show_value = True, include_input = True)
    C = mo.ui.slider(start = 0, stop = 5, value = 0, step = 0.1, label = "C", show_value = True, include_input = True)
    return A, B, C, omega, phi


@app.cell
def _(mo):
    mo.md(r"""## Sliders for the response plot below""")
    return


@app.cell
def _(A, B, C, mo, omega, phi):
    mo.vstack([A, omega, phi, B, C])
    return


@app.cell
def _(A, B, C, mo, omega, phi):
    mo.md(
        f"""
    The **amplitude** is {A.value} \n
    The **angular frequency** is {omega.value} \n
    The **phase shift** is {phi.value} \n
    The **intercept** is {B.value} \n
    The **exponential decay parameter** is {C.value}
    """
    )
    return


@app.cell
def _(A, B, C, np, omega, phi):
    t = np.arange(0, 20, 0.06)
    y = np.exp(-C.value*t) * A.value * np.cos(omega.value * t + phi.value) + B.value
    return t, y


@app.cell
def _(mo):
    color_radio_opt = mo.ui.radio(value = "blue", options = ["red", "green", "blue"], label = "Choose a plot color")
    color_radio_opt
    return (color_radio_opt,)


@app.cell
def _(color_radio_opt, plt, t, y):
    fig = plt.figure(figsize=(10,6))
    ax = fig.gca()
    ax.plot(t, y, color = color_radio_opt.value)
    ax.set_xlabel("$t$")
    ax.set_ylabel("$y$")
    ax.set_title("Response")
    ax.grid(True)
    fig
    return


@app.cell
def _(mo):
    mo.md(r"""## Example dataset with video game sales from [Kaggle](https://www.kaggle.com/code/upadorprofzs/eda-video-game-sales/input)""")
    return


@app.cell
def _(pd):
    vg_sales = pd.read_csv("./data/vgsales.csv")
    vg_sales
    return (vg_sales,)


@app.cell
def _(mo):
    mo.md(r"""## SQL Aggregation""")
    return


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
def _(mo):
    mo.md(r"""## Chart View""")
    return


@app.cell
def _(pd, vg_sales):
    vg_sales["Category of Global Sales"] = pd.cut(vg_sales["Global_Sales"], bins = 5, labels = ["Very Low", "Low", "Medium", "High", "Very High"])
    vg_sales
    return


@app.cell
def _(mo):
    mo.md(r"""## If you like marimo, be sure to follow their YouTube channel [here](https://www.youtube.com/@marimo-team) and contribute to the project on their [GitHub](https://github.com/marimo-team/marimo). For more learning materials on marimo, visit this [repo](https://github.com/marimo-team/learn).""")
    return


if __name__ == "__main__":
    app.run()
