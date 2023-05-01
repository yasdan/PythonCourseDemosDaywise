import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#from scipy import stats

def readsortdata():
    flights_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/flights/flights.csv"
    flights = pd.read_csv(flights_url)
    # flights['time_hour'] = pd.to_datetime(flights.time_hour, format = "%Y-%m-%d %H:%M")
    # flights.info()
    jan1 = flights.query('month == 1 & day == 1')
    # print(jan1)
    print(flights.sort_values(['year', 'month', 'day']))


#readsortdata()

base_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/"
table1 = pd.read_csv("{}table1/table1.csv".format(base_url))
print(table1)
print("next with rate")
ta=table1.assign(
    rate = lambda x: x.cases / x.population * 1000
)
print(ta)

def groupingAggregate():
    gr = (table1.
          groupby('year').
          agg(aggregated_cases=('cases', 'sum')).
          reset_index())
    print("grouping data")
    print(gr)


#groupingAggregate()

def chartcreat():
    plt.rcParams["figure.figsize"] = [12.50, 6.50]
    plt.rcParams["figure.autolayout"] = True
    # headers=['year','country' 'cases','population']
    table1.set_index(['country', 'population', 'year']).plot()
    plt.show()


#chartcreat()