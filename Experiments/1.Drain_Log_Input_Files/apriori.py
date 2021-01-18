import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

store_data = pd.read_csv('HDFS_2k.log_structured.csv', header=None)

store_data.head(10)

print store_data.head(10)
