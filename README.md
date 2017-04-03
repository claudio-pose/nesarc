# nesarc

This code can be used to anaylse the dataset provided by the U.S. National Epidemiological Survey on Alcohol and Related Conditions (NESARC). It consists of a representative sample of the non-institutionalized population 18 years and older. The participants were also asked questions related to gambling.

# How to
- Setting up analysis/analysis.py
  - Set the variable "dataset_path" so that it points to the NESARC CSV file
  - Set the variable "variable_definition_path" so that it points to the file "predefined_variables.json"
2. Run analysis.py, since the entire dataset will be loaded into the computer's memory, this might take a couple of minutes

# Configuring predefined variables
Predefined variable are the basis for fast and easy analyses of the nesarc dataset. You can add or remove any variables of interest by editing the default configuration file "predefined_variables.json".

The key of each ditionary item in the configuration file serves as a unique identifier. These identifiers are equivalent to the column titles in the CSV dataset file. You can look up all possible variable identifiers and their meaning the in the official NESARC codebook.
