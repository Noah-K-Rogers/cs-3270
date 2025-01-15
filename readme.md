# Module 1 

Module 1 for cs 3270

## Work environment

#### Expectation
Set up a work environment and dataset to be used throughout the project
#### Execution 
I used VS Code with copilot and linked it to [my github](https://github.com/Noah-K-Rogers/cs-3270)\
I am using the [Australian weather data](https://www.kaggle.com/datasets/arunavakrchakraborty/australia-weather-data?resource=download) from kaggle


## Code

#### Expectation
import data from csv and store it in a python data structure
#### Execution
Using the pandas module I imported the Australian weather training dataset into a pandas dataframe for use in later modules. This was done within a function to make it easier to reuse the code if needed and in the case of other datasets such as the test data to test any models.

### import_data(csv_file)
This function reads in a csv file and returns a pandas dataframe\
param csv_file: the csv file to be read in (string)\
return: pandas dataframe