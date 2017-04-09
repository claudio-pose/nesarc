# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:27:56 2017

@author: Claudio Pose
"""

from library import Analysis
from typing import List
from typing import Tuple


class FrequencyAnalysis(Analysis):
    """
    TODO: DOCSTRING
    """
    freq = dict()
    percent = dict()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def calc_frequency_tables(self) -> Tuple[str, str]:
        """Calculates the value distribution (frequencies and percentages) for specified columns of a given dataframe.
        If no columns are passed, the value distribution will be calculated for all columns of the dataframe.

        @author: Claudio Pose
        :return: 
        """

        if self.df_helper.variables is not None:
            for column in self.df_helper.variables.keys():
                self.freq[column] = self.df_helper.df[column].value_counts(sort=self.df_helper.variables[column]['sort'],
                                                                           dropna=self.df_helper.variables[column]['dropna'])

                self.percent[column] = self.df_helper.df[column].value_counts(sort=self.df_helper.variables[column]['sort'],
                                                                              dropna=self.df_helper.variables[column]['dropna'],
                                                                              normalize=True)
        else:
            print("Method not support when no variable definition is available")

    def print_frequency_tables(self, columns: List[str] = None) -> None:
        """
        TODO DOCSTRING
        :param df_helper: 
        :param columns: 
        :return: 
        """
        self.calc_frequency_tables()

        if self.df_helper.variables is not None:
            if isinstance(columns, list):  # handle a list of columns
                for column in columns:
                    self._print_single_variable(column)
            else:
                print('Unsupported parameter type %s' % (type(columns), ))
        else:
            print("Method not support when no variable definition is available")

    def _print_single_variable(self, column: str) -> None:
        """
        TODO DOCSTRING
        :param column: 
        :return: 
        """

        if column not in self.freq:  # Check whether the frequency table has been calculated
            print("Frequency table for variable '%s' not found. Check if the variable was defined in the variable definition" % (column, ))
        else:  # print the frequencies and percentages for the given variable
            print('---------------------------------')
            print(self.df_helper.variables[column]['description'])
            print('---------------------------------')
            print('\nFREQUENCIES')
            print(self.freq[column])
            print('\nPERCENTAGES')
            print(self.percent[column])
            print('')
