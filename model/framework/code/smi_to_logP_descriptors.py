import openbabel
import argparse
from rdkit import Chem
from pathlib import Path
from rdkit import RDLogger
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.rdMolDescriptors import GetUSRCAT
from rdkonf6 import RDKonf
import pandas as pd
import numpy as np

print(RDKonf)

class MRLogPDescriptor_Generator:
    mrlogP_descriptor_length = 128 + 128 + 60
    rdkonf = RDKonf()

    def write_mrlogp_descriptor_csv(self, input_csv_filepath: Path, output_csv_filepath: Path):
        assert input_csv_filepath.exists(), f"Input CSV {input_csv_filepath} not found"
        assert not output_csv_filepath.exists(), f"Targeted output CSV file {output_csv_filepath} exists!"

        # Load SMILES from CSV using pandas
        df = pd.read_csv(input_csv_filepath)
        
        # Print the column names for reference
        print("Column Names:", df.columns.tolist())
        
        # Replace 'replace_this_with_correct_column_name' with 'smiles'
        smiles_column_name = 'smiles'
        smiles_data = df[smiles_column_name].astype(str)
        mols = [(smiles, f"Mol_{i}") for i, smiles in enumerate(smiles_data)]

        obConversion = openbabel.OBConversion()
        obConversion.SetInAndOutFormats("smi", "mdl")
        ob_mol = openbabel.OBMol()

        descriptor_file = open(output_csv_filepath, "w")
        descriptor_file.write("Name," + ",".join([f"ecfp4-{i}" for i in range(128)]) + "," +
                               ",".join([f"fp4-{i}" for i in range(128)]) + "," +
                               ",".join([f"usrcat-{i}" for i in range(60)]) + "\n")

        for mol in mols:
            # Create RDKit and OpenBabel molecules
            rdkit_mol = Chem.AddHs(self.rdkonf.smiles_to_3dmol(mol[0], mol[1]))
            obConversion.ReadString(ob_mol, mol[0])

            # Generate Morgan/ECFP4
            morgan_fingerprint = AllChem.GetMorganFingerprintAsBitVect(Chem.RemoveHs(rdkit_mol), 2, 128).ToBitString()
            # Generate USRCAT
            usrcat_descriptors = GetUSRCAT(rdkit_mol)
            # Generate FP4
            fp4fp = openbabel.vectorUnsignedInt()
            fingerprinter = openbabel.OBFingerprint.FindFingerprint("FP4")

            fingerprinter.GetFingerprint(ob_mol, fp4fp)
            openbabel.OBFingerprint.Fold(fingerprinter, fp4fp, 128)

            logP_descriptors = np.full((self.mrlogP_descriptor_length), np.nan)

            for i, v in enumerate(morgan_fingerprint):
                logP_descriptors[i] = float(v)

            fp4_p1 = [float(x) for x in list(format(fp4fp[0], '032b'))]
            fp4_p2 = [float(x) for x in list(format(fp4fp[1], '032b'))]
            fp4_p3 = [float(x) for x in list(format(fp4fp[2], '032b'))]
            fp4_p4 = [float(x) for x in list(format(fp4fp[3], '032b'))]
            logP_descriptors[128:256] = fp4_p1 + fp4_p2 + fp4_p3 + fp4_p4

            print("LEN = ", len(usrcat_descriptors))
            for i, v in enumerate(usrcat_descriptors):
                logP_descriptors[256 + i] = float(v)
            print("xxxxxxxxxxxxxxx", len(logP_descriptors[256:]))
            descriptor_file.write(rdkit_mol.GetProp("_Name") + "," +
                                  ",".join([str(int(d)) for d in logP_descriptors[0:256]]) + "," +
                                  ",".join([f"{d}" for d in logP_descriptors[256:]]) + "\n")
            print(logP_descriptors)


if __name__ == "__main__":
    RDLogger.DisableLog("rdApp.*")
    parser = argparse.ArgumentParser(
        description="Write MRLogP dataset from SMILES input."
    )
    parser.add_argument(
        "input_csv", help="CSV file containing molecules with SMILES to be included in descriptor generation."
    )
    parser.add_argument(
        "output_csv", help="CSV file to save MRLogP descriptors for molecules."
    )

    args = parser.parse_args()
    descriptor_generator = MRLogPDescriptor_Generator()

    descriptor_generator.write_mrlogp_descriptor_csv(Path(args.input_csv), Path(args.output_csv))
