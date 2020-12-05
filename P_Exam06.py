import matplotlib
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'D2Coding'
matplotlib.rcParams['axes.unicode_minus'] = False

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

print(sec.head(10))

print('==========================================')
print('==========================================')

tmp_msft = msft.drop(columns='Volume')
print(tmp_msft.tail(5))



print('==========================================')
print('==========================================')

DBF = pdr.get_data_yahoo('016610.KS', start='2018-05-04')
print(DBF.head(20))

print('==========================================')
print('==========================================')

print(sec['Close'])
print(sec['Close'].shift(1))

# 일간 변동률
sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
print(sec_dpc)


print('==========================================')
print('==========================================')

# iloc = integer location indexer를 사용하여 시리즈의
# 첫번째 데이터를 0으로 변경.
sec_dpc.iloc[0] = 0
print(sec_dpc.head())

sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0
plt.hist(sec_dpc, bins=18)
plt.grid(True)
print(plt.show())

