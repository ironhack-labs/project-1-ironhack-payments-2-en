# Cohort Analysis for Ironhack Payments (Project 1)

## Introduction

IronHack Payments, a forward-thinking financial services company, has been offering innovative cash advance solutions since its inception in 2020. With a commitment to providing money advancements for free and transparent pricing, IronHack Payments has garnered a substantial user base. As part of their continuous effort to enhance their services and understand user behavior, IronHack Payments has commissioned a cohort analysis project.

This project will be focused on the analysis of data provided by Ironhack Payments. The main objective is to analyze user cohorts defined by the month of creation of their first cash advance. The monthly evolution of key metrics for these cohorts is tracked, enabling IronHack Payments to gain valuable insights into user behavior and the performance of their financial services.

The file main.ipynb provides a more detailed walkthrough of the analysis.

## Installation

To run this project locally, follow these instructions:

1. **Clone the repo:**

```bash
git clone https://github.com/martaverfer/project-1-ironhack-payments-2-en.git; \
cd jupyter_notebooks
```

2. **Virtual environment:**

Create the virtual environment: 
```bash
python3 -m venv venv
```

Activate the virtual environment:

- For Windows: 
```bash
venv\Scripts\activate
```

- For Linux/Mac: 
```bash
source venv/bin/activate
```

To switch back to normal terminal usage or activate another virtual environment to work with another project run:
```deactivate```

3. **Install dependencies:**

```bash
pip install --upgrade pip; \
pip install -r requirements.txt
```

## Cohort analysis report

The data analysis report is presented as an interactive web page. 
To generate and open it run this command (virtual environment should be activated):

```bash
cd python_scripts; \
streamlit run main.py
```

This script will execute the analysis steps and produce the results.

## Data Sources

The dataset used for this analysis can be found in this repository:
- [extract-cash request](<project_dataset/extract - cash request - data analyst.csv>)
- [extract-fees-data analyst](<project_dataset/extract - fees - data analyst - .csv>)
- [Lexique - Data Analyst](<project_dataset/Lexique - Data Analyst.xlsx>)

## Additional content

- [Presentation](https://docs.google.com/presentation/d/1Dyra_VNvsXpuOuGQpgS10yfB4yp7ZI9L1NXkTc_QoeE/edit?usp=sharing)

