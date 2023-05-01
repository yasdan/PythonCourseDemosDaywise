import  pandas as pd
import numpy as np

df = pd.DataFrame({'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                  'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                    'three': pd.Series(np.random.randn(2), index=['a', 'b'])
                       })
def row_columwisefunctionapplication():
    global df
    # row - column wise function application

    print(df)
    ap=df.apply(np.mean)
    print('After applying mean to columns')
    print(ap)
    apx= df.apply(np.mean,axis=1)
    print('After applying mean axis')
    print(apx)
    difr=df.apply(lambda x:x.max()-x.min())

    print('After applying max-min')
    print(difr)
    cms= df.apply(np.cumsum)
    print('After applying cumsum')
    print(cms)
    print("Renaming column")
    rn=df.rename(columns={"one":"first"})
    print(rn)
row_columwisefunctionapplication()


def apply_applymap():
    mp = df['one'].map(lambda x: len(str(x)))
    print("using map ()")
    print(mp)
    amp = df.applymap(lambda x: len(str(x)))
    print("Using applymap()")
    print(amp)
    print("sum with skipna")
    print(df.sum(0, skipna=False))
    print(df.sum(1,skipna=True))

#apply_applymap()

def methodsonSeries_DataFrame():
    mn= df.mean(0)
    print(mn)
    mx= df.mean(1)
    print(mx)

#methodsonSeries_DataFrame()
