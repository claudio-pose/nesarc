# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:27:56 2017

@author: Claudio Pose
"""

import pandas as pd
import json
from pathlib import Path
import os.path
import os

class DataframeHelper:
    df = None
    columns = None
    freq = dict()
    percent = dict()
    dataset_path = None
    variable_definition_path = None
    
    def __init__(self, dataset_path, variable_definition_path):
        self.dataset_path = dataset_path
        self.variable_definition_path = variable_definition_path
        
        self.read_variable_definitions()
                
        self.df = pd.read_csv(dataset_path, low_memory=False)     

        if variable_definition_path is None:
            self.columns = self.df.columns
        else:
            self.columns = self.variables.keys()
   
        self.convert_colums_to_numeric()
        
    """
    Converts all specified columns of a given dataframe into numeric values.
    If no columns are passed, all columns of the dataframe will be converted.
    
    @author: Claudio Pose
    """
    def convert_colums_to_numeric(self):
        for c in self.columns:
            self.df[c] = pd.to_numeric(self.df[c], errors='coerce')
    
    """
    Calulates the value distribution (frequencies and percentages) for specified columns of a given dataframe.
    If no columns are passed, the value distribution will be calculated for all colums of the dataframe.
    
    @author: Claudio Pose
    """
    def calc_frequency_tables(self):
        for column in self.columns:        
            self.freq[column] = self.df[column].value_counts(sort=self.variables[column]['sort'], dropna=self.variables[column]['dropna'])
            self.percent[column] = self.df[column].value_counts(sort=self.variables[column]['sort'], dropna=self.variables[column]['dropna'], normalize=True)
        
        return (self.freq, self.percent)
    
    def read_variable_definitions(self):
        with open(self.variable_definition_path) as json_data:
            self.variables = json.load(json_data)
    
    def write_variable_definitions(self):
        path = Path(self.variable_definition_path)
        if path.is_file():
            os.remove( self.variable_definition_path + '.old') # delete old backup
            os.rename(self.variable_definition_path, self.variable_definition_path + '.old') # create new backup

        with open(self.variable_definition_path, 'w') as outfile: 
            json.dump(self.variables, outfile)    