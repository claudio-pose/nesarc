# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:27:56 2017

@author: Claudio Pose
"""

import pandas as pd
import json
import os.path
import os
from pathlib import Path
from typing import Tuple

class DataframeHelper:
    """
    TODO DOCSTRING
    """

    df = None
    columns = None
    freq = dict()
    percent = dict()
    dataset_path = None
    variable_definition_path = None
    variables = None
    dataset_path = None
    variable_definition_path = None
    
    def __init__(self, dataset_path: str, variable_definition_path: str):
        """
        TODO DOCSTRING
        :param dataset_path: 
        :param variable_definition_path: 
        """

        self.dataset_path = dataset_path
        self.variable_definition_path = variable_definition_path
        self.read_variable_definitions()


    def import_data(self):
        self.df = pd.read_csv(self.dataset_path, low_memory=False)     
    
        if self.variable_definition_path is None:
            self.columns = self.df.columns
        else:
            self.columns = list(self.variables.keys())
       
        self.convert_colums()
        self.df = self.df[self.columns]

    
    def convert_colums(self) -> None:
        """
        TODO DOCTYPE

        @author: Claudio Pose
        :return: 
        """

        for column in self.columns:
            if self.variables[column]['type'] == 'category':
                self.df[column] = self.df[column].astype('category')
                
                self.df[column].cat.set_categories(new_categories=self.variables[column]['labels'], rename=True, inplace=True)
                    
            elif self.variables[column]['type'] == 'float':
                self.df[column] = pd.to_numeric(self.df[column], errors='coerce')
            else:
                print('Unknown variable type')

    def calc_frequency_tables(self) -> Tuple[str, str]:
        """Calculates the value distribution (frequencies and percentages) for specified columns of a given dataframe.
        If no columns are passed, the value distribution will be calculated for all colums of the dataframe.

        @author: Claudio Pose
        :return: 
        """

        for column in self.columns:        
            self.freq[column] = self.df[column].value_counts(sort=self.variables[column]['sort'], dropna=self.variables[column]['dropna'])
            self.percent[column] = self.df[column].value_counts(sort=self.variables[column]['sort'], dropna=self.variables[column]['dropna'], normalize=True)

        print(type(self.freq))
        return self.freq, self.percent
    
    def read_variable_definitions(self) -> None:
        """TODO DOCSTRING
        :return: 
        """

        with open(self.variable_definition_path) as json_data:
            self.variables = json.load(json_data)
    
    def write_variable_definitions(self) -> None:
        """TODO DOCSTRING
        :return: 
        """

        path = Path(self.variable_definition_path)
        if path.is_file():
            os.remove(self.variable_definition_path + '.old')  # delete old backup
            os.rename(self.variable_definition_path, self.variable_definition_path + '.old')  # mark last saved variable definition as "old"

        with open(self.variable_definition_path, 'w') as outfile:  # serialize current active variable definition
            json.dump(self.variables, outfile)