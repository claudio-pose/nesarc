# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:27:56 2017

@author: Claudio Pose
"""

import copy
import library
import frequency_table

if __name__ == "__main__":
    dataset_path = 'C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Datasets\\NESARC\\nesarc_pds.csv'
    variable_definition_path = 'C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Source Code\\nesarc\\predefined_variables.json'

    df_helper = library.DataframeHelper(dataset_path, variable_definition_path)
    df_helper.import_data()
    
    print(df_helper.df.dtypes)
    print(df_helper.df.S12Q2A12)
    
    frequency_table.print_frequency_tables(df_helper, ['S12Q2A12'])
    
    print("Rows before:" + str(len(df_helper.df.S12Q2A12)))

    df_helper.df = df_helper.df[(df_helper.df['S12Q2A12'] == 1)]
    
    print(df_helper.df.S12Q2A12)
    print("Rows after:" + str(len(df_helper.df.S12Q2A12)))
    
    
    
    
    #frequency_table.print_frequency_tables(df_helper, ['S12Q2A12'])

    #sub_gambler = copy.copy(df_helper)
    #sub_gambler.df = df_helper.df.copy()
    #sub_gambler.df = sub_gambler.df[(sub_gambler.df['S12Q2A12'] == 1)]
    
    
    
    #frequency_table.print_frequency_tables(sub_gambler, ['S12Q2A12'])

    #anti_social_k = copy.copy(df_helper)
    #anti_social_k.df = df_helper.df.copy()
    #frequency_table.print_frequency_tables(anti_social_k, ['S12Q2A12'])
    
    #print(sub_gambler.df.S12Q2A12)