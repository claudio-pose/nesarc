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


class DataFrameHelper:
    """
    TODO DOCSTRING
    """

    df = None
    columns = None
    dataset_path = None
    variable_definition_path = None
    variables = None
    dataset_path = None
    variable_definition_path = None
    
    def __init__(self, dataset_path: str, *args, **kwargs):
        """
        TODO DOCSTRING
        :param args: 
        :param kwargs: 
        """

        self.dataset_path = dataset_path
        self.variable_definition_path = kwargs.get('variable_definition_path', None)
        self.import_variable_definitions()

    def import_data(self):
        """
        TODO: DOCSTRING
        :return: 
        """

        dtypes = dict()
        defined_columns = None
        
        if self.variables is not None:
            defined_columns = list(self.variables.keys())
        
            for column in defined_columns:
                dtypes[column] = self.variables[column]['type']

        if self.dataset_path is not None:
            self.df = pd.read_csv(self.dataset_path, low_memory=False, na_values=' ', dtype=dtypes)
        else:
            raise TypeError("dataset_path is undefined")

        if self.variables is not None:
            self.columns = defined_columns
            self.df = self.df[defined_columns]
            
            for column in defined_columns:
                if self.variables[column]['type'] == 'category':
                    self.df[column].cat.set_categories(new_categories=self.variables[column]['labels'], rename=True, inplace=True)            
        else:
            self.columns = self.df.columns
    
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
            # delete old backup
            os.remove(self.variable_definition_path.join('.old'))

            # mark last saved variable definition as "old"
            os.rename(self.variable_definition_path, self.variable_definition_path('.old'))

        # serialize current active variable definition
        with open(self.variable_definition_path, 'w') as outfile:
            json.dump(self.variables, outfile)