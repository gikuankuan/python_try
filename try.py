import pandas as pd
pd.__version__

dic = {
    "col 1": [1, 2, 3], 
    "col 2": [10, 20, 30],
    "col 3": list('xyz'),
    "col 4": ['a', 'b', 'c'],
    "col 5": pd.Series(range(3))
}
df = pd.DataFrame(dic)
print(df)

#######

df = pd.read_csv('http://bit.ly/kaggletrain')
print(df.head())
df.info(memory_usage="deep")