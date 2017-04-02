# nesarc

This code can be used to anaylse the dataset provided by the U.S. National Epidemiological Survey on Alcohol and Related Conditions (NESARC). It consists of a representative sample of the non-institutionalized population 18 years and older. The participants were also asked questions related to gambling.

# How to
- Setting up analysis/analysis.py
  - Set the variable dataset_path so that it points to the NESARC CSV file
  - Set the variable variable_definition_path so that it points to the file predefined_variables.json
2. Run analysis.py, since the entire dataset will be loaded into the computer's memory, this might take a couple of minutes.

# Configuring predefined variables
Predefined variables serve as a codebook and make it easier to analyse later on. You can add or remove any variables to the configuration by editing the file predefined_variables.json. The key of the dictionary items serve as a unique identifier for each variable. You can lookup all possible identifiers  and their meaning the in the official NESARC codebook.
