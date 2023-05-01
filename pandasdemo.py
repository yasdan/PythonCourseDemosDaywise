import pandas as pnd


def pandasDataFrame():
    mydataset = {'Books': ['Python for Beginners',
                           'C#.Net Programing', 'React UI Essentials'],
                 'Price': [500, 600, 400],
                 'Publihser': ['United Books', 'Pengwin', 'Rock feller']
                 }
    dfr = pnd.DataFrame(mydataset)
    print(dfr)


def seriesPandas():
    xdata = {'Raj': 789, 'Munna': 987, 'Vijay': 999, 'Kamal': 767}
    vdata = pnd.Series(xdata)
    print(vdata)


#pandasDataFrame()
seriesPandas()
