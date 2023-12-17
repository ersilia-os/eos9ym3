# imports
import os
import csv
import sys
from rdkit import Chem
from rdkit.Chem.Descriptors import MolWt
from openbabel import openbabel
import subprocess
import pickle
from mrlogp import MRlogP

print(MRlogP)
# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# checkpoints directory
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))
ckpt_file= os.path.abspath(os.path.join(root, "..", "..", "checkpoints", "mrlogp_model.hdf5"))

# Add the path to the second script
smi_to_descriptors = os.path.abspath(os.path.join(root, "..", "..", "framework", "code", "smi_to_logP_descriptors.py"))

# Function to run the script for descriptor generation
def run_descriptor_generation(input_csv, output_csv):
    subprocess.run(["python", smi_to_descriptors, input_csv, output_csv])

# Run the descriptor generation script
descriptor_output = "descriptors_temp.csv"
run_descriptor_generation(input_file, descriptor_output)

print(descriptor_output)
descriptor_output = os.path.abspath(os.path.join(root, "..", "..", "framework", "code", "descriptors_temp.csv"))

# Initialize MRlogP
mrlogp = MRlogP()

# read descriptors from the generated CSV file
with open(descriptor_output, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    descriptors_list = [r for r in reader]


# run model
outputs = mrlogp.predict_logp(query_csv_file=descriptor_output, model_path=ckpt_file)

# check input and output have the same length
input_len = len(descriptors_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])  # header
    for o in outputs:
        writer.writerow([o])

# # Remove temporary descriptor file
# os.remove(descriptor_output)

# print("Model Outputs:")
# print(outputs)
