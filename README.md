# About

This repository demonstrates some of the capabilities of the `marimo` library, which is a git friendly notebook format that also has built-in support for reproducible environments.

## Features

- Git-friendly notebook format
- Built-in support for reproducible environments
- Easy to share and collaborate through [molab](https://molab.marimo.io/notebooks)
- Can run as a standalone script or as an application

## Getting Started
To get started, clone this repository and open it in your editor of choice. Make sure you have `marimo` installed. You can install it via pip:

```bash
pip install marimo
```

Or via conda:

```bash
conda install -c conda-forge marimo
```

Or via uv: 

```bash
uv add marimo
```

Or via pixi:

```bash
pixi add marimo
```

Marimo has two modes: `edit` mode and `run` mode.

In `edit` mode, you can modify the notebook and its environment. In `run` mode, you can see the notebook as an application.

For `edit` mode, run the following command in the terminal:

```bash
marimo edit marimo-demo.py
```

For `run` mode, run the following command in the terminal:

```bash
marimo run marimo-demo.py
```

Marimo can also be run in an isolated sandboxed environment with the following command below. For more details, see the [documentation](https://docs.marimo.io/guides/package_management/notebooks_in_projects/).

```bash
marimo edit --sandbox marimo-demo.py
```