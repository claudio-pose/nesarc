from library import DataframeHelper
from typing import List


def print_frequency_tables(df_helper: DataframeHelper, columns: List[str] = None) -> None:
    """
    TODO DOCSTRING
    :param df_helper: 
    :param columns: 
    :return: 
    """
    df_helper.calc_frequency_tables()

    if columns is not None:
        if isinstance(columns, list):  # handle a list of columns
            for column in columns:
                print_single_variable(df_helper, column)
        else:
            print('Unsupported parameter' + str(type(columns)))
    else:  # default fallback, print all predefined variables
        for key in df_helper.columns:
            print_single_variable(df_helper, key)


def print_single_variable(df_helper: DataframeHelper, column: str) -> None:
    """
    TODO DOCSTRING
    :param df_helper: 
    :param column: 
    :return: 
    """

    if column not in df_helper.freq:  # Check whether the frequency table has been calculated
        print('Frequency table not found. Check if variable was predefined:' + column)
    else:  # print the frequencies and percentages for the given variable
        print(df_helper.variables[column]['description'])
        print(df_helper.freq[column])
        print(df_helper.percent[column])
        print('')
