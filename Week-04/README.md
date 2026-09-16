# Week 4 – Predictive Analysis and Model Evaluation

## 🎯 Objective

Week 4 focused on designing a predictive analysis framework for forecasting agricultural outcomes in India.

The objective was to identify suitable forecasting targets, design predictive models, define appropriate evaluation metrics, and establish a robust validation process for future agribusiness forecasting.

The work builds on the data exploration from Week 1, data preparation and cleaning from Week 2, and analytical framework developed in Week 3.

---

## 🌾 Project Focus

The primary forecasting targets identified for the project are:

- **Crop Production** – forecasting future agricultural output.
- **Crop Yield** – forecasting productivity in kg/ha.
- **Market Prices** – forecasting commodity price trends.
- **Market Arrivals** – estimating future supply reaching agricultural markets.

Crop production and yield are the primary targets because they directly support agricultural supply, procurement, productivity, and resource-planning decisions.

---

## 📊 Real Project Data

The predictive framework uses the project's existing agricultural reference dataset developed from Directorate of Economics & Statistics (DES) data.

The current dataset contains:

- Major Indian crops
- Cultivated area
- Agricultural production
- Crop yield
- Three overlapping five-year reference periods
- 27 crop-level records

### Example

Rice production in the project dataset:

| Reference Period | Production (Mt) | Yield (kg/ha) |
|---|---:|---:|
| 2016-17 to 2020-21 | 114.45 | 2,607 |
| 2019-20 to 2023-24 | 129.26 | 2,793 |
| 2020-21 to 2024-25 | 135.52 | 2,835 |

These real project figures demonstrate the type of agricultural data that will feed the predictive pipeline.

However, the current dataset is not large enough to support a reliable final machine-learning model. The next implementation stage will expand the dataset to annual state- and district-level observations.

---

## 🔬 Predictive Models

The following models are proposed for comparison:

### 1. Naive Forecasting Baseline

The previous year's value will be used as a simple benchmark.

A machine-learning model should demonstrate improvement over this baseline before being considered useful.

### 2. Linear Regression

Used as an interpretable statistical baseline for understanding relationships between agricultural variables.

### 3. Decision Tree

Used to capture non-linear relationships and interactions between agricultural and environmental variables.

### 4. Random Forest

An ensemble of decision trees that can handle non-linear relationships and multiple interacting predictors.

### 5. Gradient Boosting

A sequential ensemble method that can provide strong performance on structured/tabular agricultural data when properly tuned.

---

## 🧠 Feature Engineering

Potential predictive features include:

- Previous-year production
- Previous-year yield
- Previous-year market price
- Area growth %
- Production growth %
- Yield growth %
- Rainfall deviation %
- Rolling production averages
- Rolling yield averages
- Market-price volatility
- Crop
- State/district
- Season

Special attention will be given to **data leakage**. Features containing information from the future will not be allowed to enter the training data.

---

## 📈 Model Evaluation Metrics

The predictive models will be evaluated using multiple metrics:

| Metric | Purpose |
|---|---|
| MAE | Measures average absolute prediction error |
| RMSE | Gives greater weight to large prediction errors |
| R² | Measures explained variation in the target |
| MAPE | Expresses error as a percentage |
| sMAPE | Provides an alternative percentage-based error measure |

Model performance will be compared against the naive baseline.

No model will be selected using a single metric alone.

---

## 🧪 Model Validation

Because agricultural forecasting involves time-dependent data, random data splitting can cause future information to leak into the training process.

The proposed validation approach therefore uses chronological splitting:

```text
Historical Data
      ↓
Training Set
      ↓
Validation Set
      ↓
Hyperparameter Tuning
      ↓
Final Model
      ↓
Untouched Test Set
      ↓
Performance Evaluation
```
## 🔍 Quality Checks

Before model training, the following checks will be performed:

Missing-value detection
Duplicate detection
Unit consistency
Invalid or negative values
Crop-name standardization
State/district consistency
Date and year validation
Production-area-yield consistency
Outlier investigation
Target leakage detection
Feature distribution checks
Temporal ordering validation
Data drift monitoring

Preprocessing operations such as scaling and imputation will be fitted only on training data during cross-validation.

## 📋 Predictive Analysis Workflow

The complete proposed workflow is:
```
Agricultural Data
        ↓
Data Collection & Integration
        ↓
Data Validation & Cleaning
        ↓
Feature Engineering
        ↓
Chronological Data Splitting
        ↓
Baseline Model
        ↓
Candidate Models
        ↓
Model Training & Tuning
        ↓
Cross-Validation
        ↓
MAE / RMSE / R² / MAPE
        ↓
Error Analysis
        ↓
Final Forecast
        ↓
Agribusiness Insights
        ↓
Monitoring & Improvement
```
## ⚠️ Dataset Limitation

The current project dataset contains 27 crop-level records across three overlapping reference periods.

This is useful for demonstrating the predictive framework and validating the data structure, but it is not sufficient for training a robust machine-learning forecasting system.

Therefore, the project does not report fabricated model accuracy, MAE, RMSE, or R² values.

The next stage will expand the dataset using annual state- and district-level observations and integrate climate and market variables before final model training.

## ⏱️ Estimated Effort
| Activity                           |  Hours |
| ---------------------------------- | -----: |
| Dataset expansion and validation   |      6 |
| Feature engineering                |      5 |
| Baseline and candidate models      |      6 |
| Time-series cross-validation       |      5 |
| Metrics and error analysis         |      4 |
| Interpretation and recommendations |      3 |
| Documentation and reproducibility  |      4 |
| **Total**                          | **33** |
