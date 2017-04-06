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

class DataFrameHelper:
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
        self.import_variable_definitions()


    def import_data(self):
        dtypes = dict()
        defined_columns = None
        
        if self.variables is not None:
            defined_columns = list(self.variables.keys())
        
            for column in defined_columns:
                dtypes[column] = self.variables[column]['type']
        
        self.df = pd.read_csv(self.dataset_path, low_memory=False, na_values=' ', dtype=dtypes)     
    
        if self.variables is not None:
            self.columns = defined_columns
            self.df = self.df[defined_columns]
            
            for column in defined_columns:
                if self.variables[column]['type'] == 'category':
                    self.df[column].cat.set_categories(new_categories=self.variables[column]['labels'], rename=True, inplace=True)            
        else:
            self.columns = self.df.columns


    def calc_frequency_tables(self) -> Tuple[str, str]:
        """Calculates the value distribution (frequencies and percentages) for specified columns of a given dataframe.
        If no columns are passed, the value distribution will be calculated for all colums of the dataframe.

        @author: Claudio Pose
        :return: 
        """
        
        # TODO: Refracter: Move this method in a seprate subclass (FrequencyTableAnalysis)

        if self.variables is not None:
            for column in self.variables:        
                self.freq[column] = self.df[column].value_counts(sort=self.variables[column]['sort'], dropna=self.variables[column]['dropna'])
                self.percent[column] = self.df[column].value_counts(sort=self.variables[column]['sort'], dropna=self.variables[column]['dropna'], normalize=True)
        
                print(type(self.freq))
                return self.freq, self.percent
            
    
    def import_variable_definitions(self) -> None:
        """TODO DOCSTRING
        :return: 
        """
        try:
            if self.variable_definition_path is not None:
                with open(self.variable_definition_path) as json_data:
                    self.variables = json.load(json_data)
            else:
                raise Exception
        except OSError:
            print("Variable definition file not found. Abstraction methods for handling the dataframe won't be available")
        except Exception:
            print("Variable definition file not specific. Abstraction methods for handling the dataframe won't be available")
    
    def export_variable_definitions(self) -> None:
        """TODO DOCSTRING
        :return: 
        """

        path = Path(self.variable_definition_path)
        if path.is_file():
            os.remove(self.variable_definition_path + '.old')  # delete old backup
            os.rename(self.variable_definition_path, self.variable_definition_path + '.old')  # mark last saved variable definition as "old"

        with open(self.variable_definition_path, 'w') as outfile:  # serialize current active variable definition
            json.dump(self.variables, outfile)