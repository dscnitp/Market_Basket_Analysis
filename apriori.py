# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
#As theres no title in the column, so we need to specify header=none
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
#creating a list of transactions
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
    
# Now we need to train  Apriori on the dataset and visualise the dataset
