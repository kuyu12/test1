# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import simplegit

# Read recipe inputs
dataset = dataiku.Dataset("dataset")
dataset_df = dataset.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

tt_df = dataset_df # For this sample code, simply copy input to output


# Write recipe outputs
tt = dataiku.Dataset("tt")
tt.write_with_schema(tt_df)
