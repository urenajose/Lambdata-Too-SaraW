"""A collection of data science utility functions."""

import warnings
import pandas as pd
import numpy as np

class MyReadyFrame():
    """The MyReadyFrame class is used to examine and clean dataframes."""

    def __init__(self, frame, npnan=True, zero=True, qmark=True, missing=True):
        """
        Param 'frame' is a dataframe which can have both catagorical and numeric
        data. Other attributes describe possible null values in the frame.

        Class exists to examine and clean dataframes.
        """
        self.frame = frame
        self.npnan = npnan
        self.zero = zero
        self.qmark = qmark
        self.missing = missing

    def null_counts(self):
        """
        Param MyReadyFrame object, status of npnan, zero, qmark, and missing
        determine which null values are counted.

        Method returns a dataframe of counts for specified null values and 0,
        includes a total column.
        """
        # surpress warning comparing pd objects to np.nan
        warnings.simplefilter(action='ignore', category=FutureWarning)
        df_null = self.frame.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        columns = list(df_null.columns)
        options = [self.npnan, self.zero, self.qmark, self.missing]
        null_name = ['NaN', 0, '?', 'Missing']
        keeper = []
        index = []

        for j in range(4):
            if options[j] is True:
                index.append(null_name[j])
                n_c = []
            for i in columns:
                null_function = [
                                df_null[i].isnull().sum(),
                                (sum(df_null[i] == '0') + sum(df_null[i] == 0)),
                                sum(df_null[i] == '?'),
                                sum(df_null[i] == '')
                                ]
                nan_count = null_function[j]
                n_c.append(nan_count)
            keeper.append(n_c)

        null_count = pd.DataFrame(data=keeper, index=index, columns=columns)
        null_count['TOTAL'] = null_count.sum(axis=1)
        return null_count

    def clean_frame(self):
        """
        Param MyReadyFrame object.

        Method returns the dataframe with leading and trailing zeros removed;
        '?','', and empty cells replaced with NaN, dtype changed to float if possible.
        """
        self.frame = (self.frame).applymap(lambda x: x.strip() if isinstance(x, str) else x)
        self.frame = (self.frame).applymap(lambda x: np.nan if isinstance(x, str) and x == '' or
                         x is None or x == '?' else x)
        self.frame.apply(pd.to_numeric, errors='ignore')
        return self.frame


if __name__ == '__main__':

    # Setup DataFrame to test MyReadyFrame methods
    data = ([[1, '', 1, 4, np.nan, 6, '0', 2],
            [2, 2, 1, 0, 1, 6, 6, 2],
            ['0', 'x', '? ', 'x', '  ', 0, 'x'],
            [np.nan, '?', '? ', 'c ', ' x', ' 0 ', ],
            [.4, .5, .35, ' ?', np.nan, .55, ],
            [5, .55, 0, .5, .2, .4, .0, .6]])

    names = ['int_a', 'int_b', 'str_a', 'str_b', 'fl_a', 'fl_b']

    df = pd.DataFrame(data, index=names).T

# Make class variable
    dft = MyReadyFrame(df)
    print(dft.frame,'\n')

# Simple Test for null_counts function,
    z = MyReadyFrame.null_counts(dft)
    print(z,'\n')

# Simple Test for clean_frame method
    dfc = MyReadyFrame.clean_frame(dft)
    print(dfc,'\n')

    z2 = MyReadyFrame.null_counts(dft)
    print(z2,'\n')
