# Neural network-based logP prediction for druglike small molecules

The authors use a two-step approach to build a model that accurately predicts the lipophilicity (LogP) of small molecules. First, they train the model on a large amount of low accuracy predicted LogP values and then they fine-tune the network using a small, accurate dataset of 244 druglike compounds. The model achieves an average root mean squared error of 0.988 and 0.715 against druglike molecules from Reaxys and PHYSPROP.

## Identifiers

* EOS model ID: `eos9ym3`
* Slug: `mrlogp`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: PRedicted LogP of small molecules

## References

* [Publication](https://www.mdpi.com/2227-9717/9/11/2029/htm)
* [Source Code](https://github.com/JustinYKC/MRlogP)
* Ersilia contributor: [leilayesufu](https://github.com/leilayesufu)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9ym3)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9ym3.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos9ym3) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://www.mdpi.com/2227-9717/9/11/2029/htm) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!