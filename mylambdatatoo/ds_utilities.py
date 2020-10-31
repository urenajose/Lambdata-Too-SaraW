"""
A collection of data science utility functions.

The function null_counts counts various forms of null values in a dataframe.

The MyReadyFrame class is used to examine and clean dataframes.
"""

import warnings

import pandas as pd
import numpy as np




class MyReadyFrame():
    """
    Param is a dataframe, can have both catagorical and numeric data
    """
    def __init__(self):
        """
        A somewhat strange class, defined only to examine dataframes.
        """

    def null_counts(self, npnan=True, zero=True, qmark=True, missing=True):
        """
        Param (self = dataframe, npnan=True(default),zero=True(default),
        qmark=True(default), missing=True(default)).

        Function returns a dataframe of counts for specified null values and 0,
        includes a total column.
        """

        self.npnan = npnan
        self.zero = zero
        self.qmark = qmark
        self.missing = missing

        # surpress warning comparing pd objects to np.nan
        warnings.simplefilter(action='ignore', category=FutureWarning)
        self = self.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        columns = list(self.columns)
        options = [npnan, zero, qmark, missing]
        null_name = ['NaN', 0, '?', 'Missing']
        keeper = []
        index = []

        for j in range(4):
            if options[j] is True:
                index.append(null_name[j])
                n_c = []
            for i in columns:
                null_function = [
                                self[i].isnull().sum(),
                                (sum(self[i] == '0') + sum(self[i] == 0)),
                                sum(self[i] == '?'),
                                sum(self[i] == '')
                                ]
                nan_count = null_function[j]
                n_c.append(nan_count)
            keeper.append(n_c)

        null_count = pd.DataFrame(data=keeper, index=index, columns=columns)
        null_count['TOTAL'] = null_count.sum(axis=1)
        return null_count

    def clean_frame(self):
        """
        Param is a dataframe, can have both catagorical and numeric data

        Method returns the dataframe with leading and trailing zeros removed;
        '?','', and empty cells replaced with NaN, dtype changed to float
        if possible.
        """

        self = self.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        self = self.applymap(lambda x: np.nan if isinstance(x, str) and x == '' or
                         x is None or x == '?' else x)
        self.apply(pd.to_numeric, errors='ignore')
        return self


if __name__ == '__main__':

    # Setup DataFrame to test MyReadyFrame methods

    data = ([[1, '', 1, 4, np.nan, 6, '0', 2],
            [2, 2, 1, 0, 1, 6, 6, 2],
            ['0', 'x', '? ', 'x', '  ', 0, 'x'],
            [np.nan, '?', '? ', 'c ', ' x', ' 0 ', ],
            [.4, .5, .35, ' ?', np.nan, .55, ],
            [5, .55, 0, .5, .2, .4, .0, .6]])

    names = ['int_a', 'int_b', 'str_a', 'str_b', 'fl_a', 'fl_b']

    dft = pd.DataFrame(data, index=names).T

    print(dft,'\n')

# Simple Test for null_counts function,
    z = MyReadyFrame.null_counts(dft)
    print(z,'\n')

# Simple Test for clean_frame method
    dfc = MyReadyFrame.clean_frame(dft)
    print(dfc,'\n')

    z2 = MyReadyFrame.null_counts(dft)
    print(z2,'\n')
