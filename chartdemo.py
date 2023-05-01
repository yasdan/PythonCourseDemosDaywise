import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def chartdemo1():
    global x, y
    x = np.array([12, 13, 42, 23, 34])
    y = np.array(['a', 'b', 'c', 'd', 'e'])
    plt.title("Data about ABC..")
    plt.xlabel("names")
    plt.ylabel("Values")
    plt.plot(x,y)
    plt.grid()
    #plt.bar(y, x)
    plt.show()

#chartdemo1()

def chartsyling():
    global points
    points = np.array([24, 112, 45, 89, 98, 45, 78, 56, 89, 100])
    plt.plot(points, ls='dashed', c='blue', marker='D')
    plt.show()

#chartsyling()

def piediagram():
    produce = np.array([2223400, 1244000, 7345000, 9999678])
    labl = np.array(['Grapes', 'Pears', 'Banana', 'Manago'])
    plt.pie(produce, labels=labl)
    plt.show()


piediagram()