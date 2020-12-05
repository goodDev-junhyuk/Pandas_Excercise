import matplotlib
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'D2Coding'
matplotlib.rcParams['axes.unicode_minus'] = False

yf.pdr_override()

KorFinance = pdr.get_data_yahoo('071050.KS', start='2019-05-04')
SKH = pdr.get_data_yahoo('000660.KS', start='2019-05-04')

import matplotlib.pyplot as plt

plt.plot(KorFinance.index, KorFinance.Close, 'b', label='한국금융지주')
plt.plot(SKH.index, SKH.Close, 'r--', label='SK하이닉스')
plt.legend(loc='best')
print(plt.show())





