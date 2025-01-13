import pandas
def main():
    #read in and store weather training data
    df = pandas.read_csv('Weather Training Data.csv')
    print(df)

if __name__ == "__main__":
    main()