# -*- coding: utf-8 -*-
"""mylambdatatoo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gqu7Q5kOkcgbVBpD5Y9wACNw4Cd3F8ig
"""

pip install -i https://test.pypi.org/simple/ mylambdatatoo==0.0.6

import mylambdatatoo

mylambdatatoo?

mylambdatatoo.ds_utilities?

mylambdatatoo.my_string?

mylambdatatoo.my_string?

# Type:        str
# String form: This is my_sting from __init__.py
# Length:      33
# Docstring:  
# str(object='') -> str
# str(bytes_or_buffer[, encoding[, errors]]) -> str

# Create a new string object from the given object. If encoding or
# errors is specified, then the object must expose a data buffer
# that will be decoded using the given encoding and error handler.
# Otherwise, returns the result of object.__str__() (if defined)
# or repr(object).
# encoding defaults to sys.getdefaultencoding().
# errors defaults to 'strict'.

mylambdatatoo.MyReadyFrame?

import pandas as pd

df_shelter = pd.read_csv('https://raw.githubusercontent.com/urenajose/DS-Unit-2-Applied-Modeling/master/aac_shelter_outcomes.csv')

mylambdatatoo.MyReadyFrame(df_shelter,npnan=True)

dft = mylambdatatoo.MyReadyFrame(df_shelter)
z = mylambdatatoo.MyReadyFrame.null_counts(dft)
print(z)