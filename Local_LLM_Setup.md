# Local LLM Instructions

## This will help you setup a local LLM using Ollama within your marimo notebook.

### Step 1: Install Ollama

*Pip:* `pip install ollama`

*Conda:* `conda install conda-forge::ollama`

*uv:* `uv add ollama`

*pixi:* `pixi add ollama`

### Step 2: Search for an Ollama model
a) Go to the following website https://www.ollama.com/search and pick a model that specializes in coding.

b) Activate your environment

c) Pull the model from Ollama with the `ollama pull` command.

- For this demo, I decided to go with Llama 3.1. To get that model, you would run this command `ollama pull llama3.1`. This will pull the appropriate model that can be handled by your hardware. Depending on your RAM, you might be able to install larger parameter models or stick with smaller models.

### Step 3: Run the Ollama Server
Run the ollama server with the following command `ollama serve`.

### Step 4: Configure AI settings within the notebook
After running the command `marimo edit marimo-demo.py`, Look for the cog icon at the top right of the notebook and then go under user settings. Within user settings, you will look for the AI setting ribbon. Change the following configuration options under the AI features tab:

**Provider:** `custom`

**Autocomplete Model:** 

This has a dropdown menu enter the following in the field provided at the bottom.
`ollama/llama3.1:latest`

**AI Edit Tooltip:** 
- [x] <-- Check the box

**Chat Model:** 

This has a dropdown menu enter the following in the field provided at the bottom.
`ollama/llama3.1:latest`

**Edit Model:**

This has a dropdown menu enter the following in the field provided at the bottom.
`ollama/llama3.1:latest`