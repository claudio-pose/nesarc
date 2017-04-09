# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:27:56 2017

@author: Claudio Pose
"""

import copy
from library import DataFrameHelper
from library import FrequencyAnalysis

if __name__ == "__main__":
    #
    dfh_overall = DataFrameHelper('C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Datasets\\NESARC\\nesarc_pds.csv',
                                   variable_definition_path='C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Source Code\\nesarc\\predefined_variables.json')

    dfh_overall.import_data()

    # Print overall distribution of the variable S12Q2A12 (illegally raised money for gambling)
    fra_overall = FrequencyAnalysis(df_helper=dfh_overall)
    fra_overall.print_frequency_tables(['S12Q2A12'])

    # Create subset of those who did at least one out of three illegal money raising methods before they were 15
    dfh_sub_illegal_childhood = copy.copy(dfh_overall)
    dfh_sub_illegal_childhood.df = dfh_overall.df.copy()

    dfh_sub_illegal_childhood.df = dfh_sub_illegal_childhood.df[(dfh_sub_illegal_childhood.df.S11AQ1B23 == 'Yes') |
                                                                (dfh_sub_illegal_childhood.df.S11AQ1B24 == 'Yes') |
                                                                (dfh_sub_illegal_childhood.df.S11AQ1B21 == 'Yes')]

    # Print distribution of the variable S12Q2A12 for the subset created above
    fra_dfh_sub_illegal_childhood = FrequencyAnalysis(df_helper=dfh_sub_illegal_childhood)


    # Print overall distribution of the variable ANTISOCDX2 diagnosed personality disorder)
    fra_overall.print_frequency_tables(['ANTISOCDX2'])

    # Create subset of those who illegally raised money to gamble (variable S12Q2A12 = Yes)
    dfh_sub_anti_social = copy.copy(dfh_overall)
    dfh_sub_anti_social.df = dfh_overall.df.copy()
    dfh_sub_anti_social.df = dfh_sub_anti_social.df[(dfh_sub_anti_social.df.S12Q2A12 == 'Yes')]

    # Print distribution of the variable ANTISOCDX2 (diagnosed personality disorder) for the subset created above
    fra_dfh_sub_anti_social = FrequencyAnalysis(df_helper=dfh_sub_anti_social)
    fra_dfh_sub_anti_social.print_frequency_tables(['ANTISOCDX2'])
