
from typing import Sequence

import numpy as np
from rdkit import Chem, DataStructs
from rdkit.Chem import MACCSkeys
from rdkit.Chem import AllChem


def _smiles_to_mols(smiles_list: Sequence[str]):

    mols = []
    for s in smiles_list:
        mol = Chem.MolFromSmiles(str(s))
        if mol is None:
            raise ValueError(f"Could not parse SMILES: {s!r}")
        mols.append(mol)
    return mols


def _fp_to_array(fp) -> np.ndarray:
    arr = np.zeros((fp.GetNumBits(),), dtype=np.int8)
    DataStructs.ConvertToNumpyArray(fp, arr)
    return arr


def make_morgan_fingerprints(
    smiles_list: Sequence[str],
    radius: int = 3,
    n_bits: int = 2048,
) -> np.ndarray:
    mols = _smiles_to_mols(smiles_list)

    fps = []
    for mol in mols:
        bv = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=n_bits)
        fps.append(_fp_to_array(bv))
    return np.vstack(fps)


def make_maccs_fingerprints(smiles_list: Sequence[str]) -> np.ndarray:

    mols = _smiles_to_mols(smiles_list)

    fps = []
    for mol in mols:
        bv = MACCSkeys.GenMACCSKeys(mol)  # 167 bits
        fps.append(_fp_to_array(bv))
    return np.vstack(fps)
