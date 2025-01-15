'''
This script reads in a csv file and returns a pandas dataframe
'''

import pandas
def load_csv(csv_file):
    '''
    This function reads in a csv file and returns a pandas dataframe
    param csv_file: the csv file to be read in (string)
    return: pandas dataframe
    '''
    df = pandas.read_csv(csv_file)
    return df

def main():
    # Test the import_data function
    df = load_csv("Weather Training Data.csv")
    print(df)

if __name__ == "__main__":
    main()