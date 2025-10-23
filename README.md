# MRlogP: neural network-based logP prediction for druglike small molecules

The authors use a two-step approach to build a model that accurately predicts the lipophilicity (LogP) of small molecules. First, they train the model on a large amount of low accuracy predicted LogP values and then they fine-tune the network using a small, accurate dataset of 244 druglike compounds. The model achieves an average root mean squared error of 0.988 and 0.715 against druglike molecules from Reaxys and PHYSPROP.

This model was incorporated on 2023-12-12.


## Information
### Identifiers
- **Ersilia Identifier:** `eos9ym3`
- **Slug:** `mrlogp`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Any`
- **Tags:** `Lipophilicity`, `LogP`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Predicted LogP of small molecules

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| logp | float | low | Predicted logP value of the compound |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9ym3](https://hub.docker.com/r/ersiliaos/eos9ym3)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9ym3.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9ym3.zip)

### Resource Consumption
- **Model Size (Mb):** `45`
- **Environment Size (Mb):** `2467`
- **Image Size (Mb):** `2479.8`

**Computational Performance (seconds):**
- 10 inputs: `41.08`
- 100 inputs: `1418.48`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/JustinYKC/MRlogP](https://github.com/JustinYKC/MRlogP)
- **Publication**: [https://www.mdpi.com/2227-9717/9/11/2029/htm](https://www.mdpi.com/2227-9717/9/11/2029/htm)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [leilayesufu](https://github.com/leilayesufu)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9ym3
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9ym3
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
