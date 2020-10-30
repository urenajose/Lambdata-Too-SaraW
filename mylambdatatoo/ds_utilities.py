import pandas as pd
import numpy as np
import warnings

class My_Ready_Frame():
    def __init__(self, df):
        self.df = df
    """
    Param df = dataframe, can have both catagorical and numeric data
    """

    def clean_frame(self):
        
        """
        Param is a dataframe, can have both catagorical and numeric data

        Method returns the dataframe with leading and trailing zeros removed;
        '?','', and empty cells replaced with NaN, dtype changed to float
        if possible.
        """

        df = self.applymap(lambda x: x.strip() if type(x) == str else x)
        df = df.applymap(lambda x: np.nan if type(x) == str and x == '' or
                        x == None or x == '?' else x)
        df = df.apply(pd.to_numeric, errors='ignore')
        return (df)




    def null_counts(self, npnan, zero, qmark, missing):

        """
        Param (df = dataframe, npnan=True(default),zero=True(default),
        qmark=True(default), missing=True(default)).

        Method returns a dataframe of counts for specified null values and 0,
        default is all.
        """

  # surpress warning comparing pd objects to np.nan
  warnings.simplefilter(action='ignore', category=FutureWarning)
  dfn = df.applymap(lambda x: x.strip() if type(x) == str else x)
  columns = list(df.columns)
  options = [npnan, zero, qmark, missing]
  null_name = ['NaN', 0, '?', 'Missing']
  keeper = []
  index = []

  for p in range(4):
    if options[p] == True:
      index.append(null_name[p])
      n_c = []
      for i in columns:
        null_function = [
                         dfn[i].isnull().sum(),
                         (sum(dfn[i] == '0')+sum(dfn[i] == 0)),
                         sum(dfn[i] == '?'),
                         (sum(dfn[i] == '')+sum(dfn[i] == None))
                         ]
        nan_count = null_function[p]
        n_c.append(nan_count)
      keeper.append(n_c)

  null_count = pd.DataFrame(data=keeper, index=index, columns=columns)
  return (null_count)



if __name__ == '__main__':

# Setup DataFrame to test My_Ready_Frame methods

    data = ([[1, '', 1, 4, np.nan, 6, '0', 2],
            [2, 2, 1, 0, 1, 6, 6, 2],
            ['0', 'x', '? ', 'x', '  ', 0, 'x'],
            [np.nan, '?', '? ', 'c ', ' x', ' 0 ', ],
            [.4, .5, .35, ' ?', np.nan, .55, ],
            [5, .55, 0, .5, .2, .4, .0, .6]
            ])

    names = ['int_a', 'int_b', 'str_a', 'str_b', 'fl_a', 'fl_b']

    df = pd.DataFrame(data, index=names).T

    print(df)

#Simple Test for null_counts method
    z = My_Ready_Frame.null_counts(df, True, True, True, True)
    print(z)
    print('')

#Simple Test for clean_frame method
    q = My_Ready_Frame.clean_frame(df)
    print(q)
    print('')
