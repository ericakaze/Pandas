###3#create a virtual environment first 
##py -3 -m venv pandas_venv 
### activate it pandas_venv/scripts/activate
### install pandas pip install pandas 

import pandas as pd 

# grades = pd.Series([87,100,94])

# print(grades)

# print(pd.Series(98,6, range(3)))

# print(grades[0])
# print(grades.count())
# print(grades.mean())
# print(grades.min())
# print(grades.max())
# print(grades.std())

# print(grades.describe())

# grades= pd.Series([87,100,94], index=['Wally', 'Eva', 'Sam'])

# grades=pd.Series({"Wally':87, 'Eva':100, 'Sam':94})

# print(grades['Eva'])

# print(grades.Wally) ## with the dot method, it becomes an object 

# print(grades.dtype) ## tells us the type of object 

# print(grades.values) ###gives an array of all the values in the series 

hardware = pd.Series(['Hammer', 'Saw', 'wrench'])

#print(hardware)

print(hardware.str.contains('a')

print(hardware.str.upper())