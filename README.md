HW5
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/REPLACE_WITH_OWNER_ACCOUNT/hw5/workflows/CI/badge.svg)](https://github.com/REPLACE_WITH_OWNER_ACCOUNT/hw5/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/HW5/branch/main/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/HW5/branch/main)


The goal of your package to run the code from HW 4, where the fingerprint-based models were trained on the lipophilicity dataset.

The code:

- Loads the Lipophilicity dataset (`Lipophilicity.csv`)
- Generates **Morgan** and **MACCS** fingerprints from SMILES using RDKit
- Trains separate `MLPRegressor` models for each fingerprint type
- Reports the test set RMSE for each model
- Prints the name of the currently active Conda environment



## Repository structure

The most important files for the assignment are:

- `environment.yml` – Conda environment specification (uses `conda-forge` and includes `rdkit`)
- `LICENSE` – License file for this repository
- `README.md` – This file
- `run_models.py` – Script that:
  - Imports fingerprint functions
  - Trains both models
  - Calculates RMSEs
  - Prints RMSEs and the Conda environment name
- `hw5/data/Lipophilicity.csv` – Lipophilicity dataset


## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/epitawalaaru/hw5.gitt
   cd hw5



## Create and activate the Conda environment

conda env create -f environment.yml
conda activate homework5



## From the repository root (the folder containing run_models.py), run:

python run_models.py




### Copyright

Copyright (c) 2025, Udena Arachchige


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.11.
