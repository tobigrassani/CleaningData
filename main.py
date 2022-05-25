# Here we will clean datasets
# We will work with the "Student Mental Health" dataset from Kaggle

# Importing libraries

import pandas as pd
import numpy as np
import seaborn as sns

# Reading dataset

dataset = pd.read_csv("Student Mental health.csv")
print(dataset.head(10))

# Analyzing dataset