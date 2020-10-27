import pandas as pd

# 리스트를 이용하여 한 행씩 추가해서 데이터프레임을 생성.
columns = ['KOSPI', 'KOSDAQ']
index = [2014, 2015, 2016, 2017, 2018]

rows = []
rows.append([1915, 542])
rows.append([1961, 682])
rows.append([2026, 631])
rows.append([2467, 798])
rows.append([2041, 675])

df = pd.DataFrame(rows, columns=columns, index=index)
print(df)