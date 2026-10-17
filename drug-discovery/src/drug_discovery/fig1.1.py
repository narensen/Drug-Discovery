from rdkit import Chem
from rdkit.Chem import (
    AllChem, Descriptors, Draw,
)

smiles_string = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"
mol = Chem.MolFromSmiles(smiles_string)

print("Number of atoms: ", mol.GetNumAtoms())
print("Number of bonds: ", mol.GetNumBonds())

img = Draw.MolsToGridImage(
    mols=[mol], molsPerRow=1, useSVG=True,)

print(img)