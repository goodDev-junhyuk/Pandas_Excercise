import pandas as pd

df = pd.DataFrame({'KOPSI' : [1915, 1961, 2026, 2467, 2041],
                   'KOSDAQ' : [542, 682, 631, 798, 675]},
                   index=[2014, 2015, 2016, 2017, 2018])

print(df)
print("--------------------------------------")
print("--------------------------------------")


print(df.describe())
print("--------------------------------------")
print("--------------------------------------")

print(df.info())
print("--------------------------------------")
print("--------------------------------------")

kospi = pd.Series([1915, 1961, 2026, 2467, 2041],
                  index=[2014, 2015, 2016, 2017, 2018], name='KOPSI')
print(kospi)

print("--------------------------------------")
print("--------------------------------------")

kosdaq = pd.Series([542, 682, 631, 798, 675],
                   index=[2014, 2015, 2016, 2017, 2018], name='KOSDAQ')
print(kosdaq)

print("--------------------------------------")
print("--------------------------------------")

print(kosdaq)

df = pd.DataFrame({kospi.name: kospi, kosdaq.name: kosdaq})
print(df)


columns = ['KOSPI', 'KOSDAQ']
index = [2014, 2015, 2016, 2017, 2018, 2019]
rows = []

rows.append([1915, 542])
rows.append([1961, 682])
rows.append([2026, 631])
rows.append([2467, 798])
rows.append([2041, 675])

df = pd.DataFrame(rows, columns=columns, index=index)
print(df)