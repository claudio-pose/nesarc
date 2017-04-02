# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:27:56 2017

@author: Claudio Pose
"""

import library
import frequency_table


if __name__ == "__main__":
    dataset_path = 'C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Datasets\\NESARC\\nesarc_pds.csv'
    variable_definition_path = 'C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Source Code\\nesarc\\predefined_variables.json'

    df_helper = library.DataframeHelper(dataset_path, variable_definition_path)

    frequency_table.print_frequency_tables(df_helper, ['S12Q3D', 'S12Q3I'])
