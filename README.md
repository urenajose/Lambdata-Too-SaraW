# Lambdata-Too-SaraW
Data science utilities version 2

MyReadyFrame class is used to examine dataframes for various
null values, and replace values with NaN.

## Installation

To access Lambdata-Too-SaraW
pip install -i https://test.pypi.org/simple/ mylambdatatoo==0.0.6

## Usage

```
from mylambdatatoo.ds_utilities import MyReadyFrame

Param df = dataframe, can have both catagorical and numeric data

dft = MyReadyFrame(df)
    z = MyReadyFrame.null_counts(dft)
    print(z)


returns new dataframe with count of null values per column
```

```
from mylambdatatoo.ds_utilities import MyReadyFrame

Param df = dataframe, can have both catagorical and numeric data

dft = MyReadyFrame(df)
z = MyReadyFrame.clean_frame(df)
print(z)

returns dataframe with spaces removed and missing values
replaced with np.nan, column dtypes set to float if possible
```


