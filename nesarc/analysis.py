# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:27:56 2017

@author: Claudio Pose
"""

import copy
from library import DataFrameHelper
from library import FrequencyAnalysis

if __name__ == "__main__":
    df_helper = DataFrameHelper(dataset_path = 'C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Datasets\\NESARC\\nesarc_pds.csv',
                                variable_definition_path = 'C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Source Code\\nesarc\\predefined_variables.json')

    df_helper.import_data()

    fr_analysis = FrequencyAnalysis(df_helper=df_helper)
    # overall distribution
    fr_analysis.print_frequency_tables(['S12Q2A12'])    
    
    # create subset
    df_helper.df = df_helper.df[(df_helper.df.S12Q2A12 == 'Yes')]    
    fr_analysis.print_frequency_tables(['S12Q2A12'])    
    #fr_analysis.print_frequency_tables(df_helper, ['S12Q2A12'])

    #sub_gambler = copy.copy(df_helper)
    #sub_gambler.df = df_helper.df.copy()
    #sub_gambler.df = sub_gambler.df[(sub_gambler.df['S12Q2A12'] == 1)]
    