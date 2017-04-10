# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:27:56 2017

@author: Claudio Pose
"""

import copy
import numpy
import library as lib

if __name__ == "__main__":
    dfh_overall = lib.DataFrameHelper('C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Datasets\\NESARC\\nesarc_pds.csv',
                                      variable_definition_path='C:\\Users\\claud\\OneDrive\\Dokumente\\Weiterbildung\\Data Analysis\\Coursera\\Wesleyan University\\Data Analysis and Interpretation Specialization\\Source Code\\nesarc\\predefined_variables.json',
                                      limit_columns=True,
                                      nrows=100)

    dfh_overall.import_data()

    # Treat answers that fell into the category "Unknown" as missing data (NaN)
    dfh_overall.df.S12Q1  = dfh_overall.df.S12Q1.replace('Unknown', numpy.nan)
    dfh_overall.df.S12Q3D  = dfh_overall.df.S12Q3D.replace('Unknown', numpy.nan)
    dfh_overall.df.S12Q3I  = dfh_overall.df.S12Q3I.replace('Unknown', numpy.nan)
    dfh_overall.df.S12Q2A12 = dfh_overall.df.S12Q2A12.replace('Unknown', numpy.nan)
    dfh_overall.df.S11AQ1B13 = dfh_overall.df.S11AQ1B13.replace('Unknown', numpy.nan)
    dfh_overall.df.S11AQ1B20 = dfh_overall.df.S11AQ1B20.replace('Unknown', numpy.nan)
    dfh_overall.df.S11AQ1B23 = dfh_overall.df.S11AQ1B23.replace('Unknown', numpy.nan)
    dfh_overall.df.S11AQ1B24 = dfh_overall.df.S11AQ1B24.replace('Unknown', numpy.nan)
    dfh_overall.df.S11AQ1B21 = dfh_overall.df.S11AQ1B21.replace('Unknown', numpy.nan)

    # Print overall distribution of the variable S12Q2A12 (illegally raised money for gambling)
    frequencey_analysis = lib.FrequencyAnalysis(df_helper=dfh_overall)
    frequencey_analysis.print_frequency_tables(['S12Q2A12'])

    # Create subset of those who did at least one out of three illegal money raising methods before they were 15
    dfh_sub_illegal_childhood = copy.copy(dfh_overall)
    dfh_sub_illegal_childhood.df = dfh_overall.df.copy()

    dfh_sub_illegal_childhood.df = dfh_sub_illegal_childhood.df[(dfh_sub_illegal_childhood.df.S11AQ1B24 == 'Yes') &
                                                                (dfh_sub_illegal_childhood.df.S11AQ1A21 == 'Yes')]


    # Print distribution of the variable S12Q2A12 for the subset created above
    frequencey_analysis.df_helper = dfh_sub_illegal_childhood
    frequencey_analysis.print_frequency_tables(['S12Q2A12'])

    # Print overall distribution of the variable ANTISOCDX2(diagnosed personality disorder)
    frequencey_analysis.df_helper = dfh_overall
    frequencey_analysis.print_frequency_tables(['ANTISOCDX2'])

    # Create subset of those who illegally raised money to gamble (variable S12Q2A12 = Yes)
    dfh_sub_anti_social = copy.copy(dfh_overall)
    dfh_sub_anti_social.df = dfh_overall.df.copy()
    dfh_sub_anti_social.df = dfh_sub_anti_social.df[(dfh_sub_anti_social.df.S12Q2A12 == 'Yes')]

    # Print distribution of the variable ANTISOCDX2 (diagnosed personality disorder) for the subset created above
    frequencey_analysis.df_helper = dfh_sub_anti_social
    frequencey_analysis.print_frequency_tables(['ANTISOCDX2'])