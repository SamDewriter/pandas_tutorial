import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df.to_csv('mydata.csv')

print("Data saved to mydata.csv")