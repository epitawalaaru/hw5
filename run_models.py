import os
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler


from hw5.data.fingerprints import make_morgan_fingerprints, make_maccs_fingerprints

DATA_PATH = Path(__file__).parent / "hw5" / "data" / "Lipophilicity.csv"


def build_and_train_model(X_train: np.ndarray, y_train: np.ndarray, random_state: int = 0):

    y_scaler = StandardScaler()
    y_train_scaled = y_scaler.fit_transform(y_train.reshape(-1, 1)).ravel()

    model = MLPRegressor(
        hidden_layer_sizes=(100, 50),
        activation="relu",
        solver="adam",
        alpha=0.001,
        learning_rate="adaptive",
        max_iter=500,
        random_state=random_state,
    )
    model.fit(X_train, y_train_scaled)
    return model, y_scaler


def compute_rmse(model: MLPRegressor, y_scaler: StandardScaler, X_test: np.ndarray, y_test: np.ndarray) -> float:

    y_pred_scaled = model.predict(X_test)
    y_pred = y_scaler.inverse_transform(y_pred_scaled.reshape(-1, 1)).ravel()
    rmse = float(np.sqrt(mean_squared_error(y_test, y_pred)))
    return rmse


def main():

    df = pd.read_csv(DATA_PATH)

    smiles = df["smiles"].astype(str).to_list()
    y = df["exp"].astype(float).to_numpy()


    smiles_train, smiles_test, y_train, y_test = train_test_split(
        smiles, y, test_size=0.2, random_state=0
    )


    X_train_morgan = make_morgan_fingerprints(smiles_train, radius=3, n_bits=2048)
    X_test_morgan = make_morgan_fingerprints(smiles_test, radius=3, n_bits=2048)

    X_train_maccs = make_maccs_fingerprints(smiles_train)
    X_test_maccs = make_maccs_fingerprints(smiles_test)


    morgan_model, morgan_scaler = build_and_train_model(X_train_morgan, y_train, random_state=0)
    maccs_model, maccs_scaler = build_and_train_model(X_train_maccs, y_train, random_state=1)


    morgan_rmse = compute_rmse(morgan_model, morgan_scaler, X_test_morgan, y_test)
    maccs_rmse = compute_rmse(maccs_model, maccs_scaler, X_test_maccs, y_test)


    env_name = os.getenv("CONDA_DEFAULT_ENV", "UNKNOWN_ENV")

 
    print("=== Lipophilicity fingerprint models ===")
    print(f"Morgan RMSE: {morgan_rmse:.4f}")
    print(f"MACCS  RMSE: {maccs_rmse:.4f}")
    print()
    print(f"Conda environment: {env_name}")


if __name__ == "__main__":
    main()
