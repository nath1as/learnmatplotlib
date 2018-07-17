import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def graph_data(stock):
    stock_price_url = 'http://chartapi.financie.yahoo.com/instrument/1.0/' \
                       + stock + '/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock.data.append(line)
    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y%m%d') })


def bytespdate2num(structure):
    return structure

# %Y full year 2015
# %y partial year 15
# %m  number month
# %d number day
# %H hours
# %M minutes
# %S seconds
# %m-%d-%Y 12-06-2015


plt.xlabel('x')
plt.ylabel('y')

plt.title('Interesting Graph\nCheck it out')
plt.legend()

plt.show()
