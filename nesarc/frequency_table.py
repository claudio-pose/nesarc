def print_frequency_tables(df_helper, columns = None):
    df_helper.calc_frequency_tables()

    if not columns == None:
        if type(columns) == type([]): # handle a list of columns
            for column in columns:
                print_single_variable(df_helper, column)
        elif type(columns) == type(''): # handle a single column
            print_single_variable(df_helper, columns)
        else:
            print('Unsporrted parameter' + str(type(columns)))
    else: # default fallback, print all predefined variables
        for key in df_helper.columns:
            print_single_variable(df_helper, key)
        
def print_single_variable(df_helper, column):
    if not column in df_helper.freq: # Check whether the frequency table has been calculated
        print('Frequency table not found for variable. Check if variable was predefined:' + column)
    else: # print the frequencies and percentages for the given variable
        print(df_helper.variables[column]['description'])
        print(df_helper.freq[column])
        print(df_helper.percent[column])
        print('')
