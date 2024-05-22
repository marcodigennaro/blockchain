# Block Chain

This repo demonstrate how to build a block chain app implementing basic functionalities to initiate the chain, mine and 
retrieve blocks, validate the chain. The app is wrapped into an API.

## Get Started

### Prerequisites

- python
- poetry 

```
pip install poetry  #Linux
```
or 
```
brew install poetry #Macos
```

### Get the code/Run tests/Launch API
```
# Navigate to your local folder
cd /your/local/folder

# Clone the WindML repository
git clone git@github.com:marcodigennaro/blockchain.git

# Enter the folder
cd blockchain/

# Create the python environment from the pyproject.toml file
poetry install

# Activate the python environment
source .venv/bin/activate

# Run tests 
poetry run pytest -v

# Start Jupyter Lab
jupyter-lab  

# Start the API
uvicorn api.api:app --reload
```

### Acknowledgements

- [rithmic](https://www.youtube.com/watch?v=G5M4bsxR-7E)

### Author

- [Marco Di Gennaro](https://github.com/marcodigennaro/CV/blob/main/MDG_CV.pdf)
- [GitHub](https://github.com/marcodigennaro)
- [Linkedin](https://www.linkedin.com/in/marcodig/)
- [Website](https://atomistic-modelling.com/)
