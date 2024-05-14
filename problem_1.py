# Pandas DataFrame with Two-dimensional List

# Create Pandas Dataframe from 2D List using pd.DataFrame()

import pandas as pd  
lst = [['Geek', 25], ['is', 30], 
       ['for', 26], ['Geeksforgeeks', 22]] 
df = pd.DataFrame(lst, columns =['Tag', 'number']) 
print(df )


# Create Pandas Dataframe from 2D List using pd.DataFrame.from_records()

import pandas as pd
data = [['Geek1', 28, 'Analyst'],
        ['Geek2', 35, 'Manager'],
        ['Geek3', 29, 'Developer']]
columns = ['Name', 'Age', 'Occupation']
df = pd.DataFrame.from_records(data, columns=columns)
print(df)

#Create Pandas Dataframe from 2D List using pd.DataFrame.from_dict()

import pandas as pd
data = [['Geek1', 26, 'Scientist'],
        ['Geek2', 31, 'Researcher'],
        ['Geek3', 24, 'Engineer']]
columns = ['Name', 'Age', 'Occupation']
df = pd.DataFrame.from_dict(dict(zip(columns, zip(*data))))
print(df)

#Create Pandas Dataframe from 2D List using Specifying Data Types

import pandas as pd
data = [['Geek1', 'Reacher', 25],
        ['Geek2', 'Pete', 30],
        ['Geek3', 'Wilson', 26],
        ['Geek4', 'Williams', 22]]
columns = ['FName', 'LName', 'Age']
df = pd.DataFrame(data, columns=columns)
print(df)