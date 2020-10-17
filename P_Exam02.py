import pandas as pd

s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])
print(s)

print("-----------------------------")

s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8])
s.index.name = 'MY_IDX'
print(s)

print("-----------------------------")

s.name = "MY_SERIES"
print(s)

print("-----------------------------")


s[5.9] = 5.5
print(s)

print("-----------------------------")

ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
s = s.append(ser)
print(s)

