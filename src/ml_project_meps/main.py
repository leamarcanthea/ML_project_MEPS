import numpy as np
import pandas as pd
import os


################################################################################
################################ 1. Data Loading ###############################
################################################################################

bdd_stata = os.path.join(os.getcwd(), "data", "raw_data", "h256.dta")
df = pd.read_stata(bdd_stata, convert_categoricals=False)
print(df.head())

#Quick check to see if the DUPERSID column (people identifiers) is unique
df["DUPERSID"].is_unique # it is

print(list(df.columns)) # list of columns in the dataframe
