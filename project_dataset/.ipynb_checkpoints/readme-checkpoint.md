![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Business Challenge: Cohort Analysis for Ironhack Payments - Black Rangers(Marta, Mirko, Lukas)

## Introduction

The goal of this project is to gain insight of user behavior reaching out to IronHack Payments, a company specialised in offering cash advance solution.
Success of this project is reached by cohort analysis


## Project Overview

The project aims at answering questions such as:

- What is the cohort with the highest revenue and how does this evolve with time?
- What is the IR (Incidence Rate) for each cohort?

On top of this a new KPI has been launched: **Retention Rate**.
This aims at showing the rate of customers who are repeated customers after their first request.


### Data Analysis Tools

The team has developed their analysis via Python

### Exploratory Data Analysis (EDA)

Explanatory analysis has been completed at the beginning of the notebook to get to know the different datasets provided.
df_cash stems from the csv file 'cash request' and df_fees from the csv file 'fees'.

### Data Quality Analysis

Once the team has become comfortable with the data, data cleaning has been completed by removing NaN values were needed.
Also date information has been transformed to datetime for better data manipulation.

### Deliverables

Once the data has been organized efficiently the cohorts were established by aggregation.
The team has made sure to establish cohort columns in the dataset by extracting date information from the created_at column and making sure this was filtered by the minimun date (to capture the first customer request) and that also the duplicate user_ids were removed by keeping the first entry.

Once the cohorts were defined data visualization graphs have been created to complete the tasks.
   

### Resources
- project notebook for codes used
- slide presentation

Marta, Mirko, Lukas