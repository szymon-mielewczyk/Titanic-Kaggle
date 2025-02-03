# Data Processing and Machine Learning Models

## Overview

This repository contains scripts and notebooks for preprocessing data and implementing various machine learning models, including neural networks, regression, and tree-based models. The project includes handling missing values, extracting numerical features, and performing hyperparameter optimization using Bayesian search.

## Competition Source

The dataset used in this project is sourced from the Kaggle Titanic competition: [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data).

## Preprocessing Steps

- Extracting numerical features from data
- Dropping unnecessary IDs and names
- Encoding categorical characters into integers
- Transforming cabin values into cabin letter and cabin number
- Handling missing values

## Implemented Methods

- Basic data preprocessing
- Neural network implementation
- Filling missing values
- Bayesian search for hyperparameter tuning

## Files and Notebooks

### Exploratory Data Analysis

- **EDA.ipynb** - Exploratory data analysis with raw and preprocessed data

### Preprocessing

- **prepare\_data.py** - Data preprocessing basic schema

### Neural Networks

- **neural\_network.ipynb** - Basic neural network implementation

### Null Value Imputation

- **null\_filling\_age.ipynb** - Predicting missing age values
- **null\_filling\_cabin\_char.ipynb** - Predicting missing cabin letter values
- **null\_filling\_cabin\_number.ipynb** - Predicting missing cabin number values

### Regression Models

- **regression-pytorch.ipynb** - Regression using PyTorch
- **regression-sklearn.ipynb** - Regression using Scikit-learn

### Classification Models

- **svc-sklearn.ipynb** - Support Vector Classification (SVC) using Scikit-learn
- **tree-sklearn.ipynb** - Decision tree classifier using Scikit-learn
- **xgboost.ipynb** - XGBoost classifier with predicted null values

## Data Download

Download the Titanic dataset from the Kaggle competition and place it under the `data` directory.

## XGBoost Workflow

To run the XGBoost model, follow these steps:

1. Process the training dataset (`train.csv`) sequentially:
   - Run **null_filling_cabin_char.ipynb** → Output: `filled_null_cabin_chars.csv`
   - Run **null_filling_cabin_number.ipynb** → Output: `filled_null_cabin_numbers.csv`
   - Run **null_filling_age.ipynb** → Output: `filled_null_age.csv`

2. Repeat the same steps for the test dataset (`test.csv`), modifying the output filenames:
   - **null_filling_cabin_char.ipynb** → `filled_null_cabin_chars_test.csv`
   - **null_filling_cabin_number.ipynb** → `filled_null_cabin_numbers_test.csv`
   - **null_filling_age.ipynb** (Input: `filled_null_cabin_numbers_test.csv`) → `filled_null_age_test.csv`

Although there may be a data splitting error due to the different size in train.csv and test.csv files, change the values ​​that sum to the length of the data set

### Required Libraries

```
pandas
torch
mlflow
numpy
matplotlib
sklearn
skorch
xgboost
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/szymon-mielewczyk/Titanic-Kaggle.git
   ```
2. Navigate to the directory:

3. Execute notebooks as needed for model training and evaluation.
