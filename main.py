import numpy as np
import pandas as pd
# Loading the files into Python
cash_request = pd.read_csv("C:\\Users\\dusan\\Documents\\GitHub\\Ironhack\\project-1-ironhack-payments-2-en\\project-1-ironhack-payments-2-en\\project_dataset\\extract - cash request - data analyst.csv")
fees_request = pd.read_csv("C:\\Users\\dusan\\Documents\\GitHub\\Ironhack\\project-1-ironhack-payments-2-en\\project-1-ironhack-payments-2-en\\project_dataset\\extract - fees - data analyst - .csv")

# Turning datasets into Data Frames
cash = pd.DataFrame(cash_request)
fees = pd.DataFrame(fees_request)

#Displaying the first 10 Rows of the data sets to understand it better
cash.head(10)
fees.head(10)

#Displaying basic infos about the data to understand it better
cash.info()
cash.shape
fees.info()
fees.shape

#Searching for Null values since the info told us that there are nullvalues
cash["category"].isnull()