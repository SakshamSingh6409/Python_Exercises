import pandas as pd

data = [100, 200, 300, 400, 500]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(series)
print(series.loc["c"])