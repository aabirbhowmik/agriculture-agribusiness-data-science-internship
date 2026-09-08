# 🌾 Agriculture & Agribusiness Data Science Internship

Welcome to my project repository for the **Junior Data Science Analyst – Agriculture & Agribusiness** virtual internship.

This repository contains my weekly data science projects, analysis, documentation, and insights related to the agriculture and agribusiness domain.

---

## 🎯 Project Objective

The overall objective is to apply data science techniques to publicly available agricultural data to identify:

- Agricultural production trends
- Crop productivity patterns
- Regional differences
- Climate-related risks
- Market opportunities
- Potential agribusiness opportunities

The project follows a practical data science workflow:

**Data Collection → Data Cleaning → Exploratory Analysis → Statistical Analysis → Visualization → Business Insights**

---

## 📂 Repository Structure

```text
agriculture-agribusiness-data-science-internship/
│
├── README.md
│
├── Week-01/
│   ├── README.md
│   ├── Week_1_Agriculture_Data_Science_Project_Strategy.docx
│   │
│   ├── data/
│   │   ├── README.md
│   │   ├── des_normal_estimates_major_crops.csv
│   │   └── des_normal_estimates_change_summary.csv
│   │
│   ├── notebooks/
│   │   └── Week_1_Agriculture_Data_Exploration.ipynb
│   │
│   └── outputs/
│       ├── README.md
│       ├── crop_production_trends.png
│       ├── foodgrain_production_trend.png
│       ├── production_change.png
│       └── yield_change.png
│
└── Future weeks...
```
## 📅 Weekly Progress
| Week   | Task                                    | Status      |
| ------ | --------------------------------------- | ----------- |
| Week 1 | Data Exploration & Strategy Formulation | ✅ Completed |
| Week 2 | Coming Soon                             | ⏳           |
| Week 3 | Coming Soon                             | ⏳           |
| Week 4 | Coming Soon                             | ⏳           |

## 📊 Week 1 – Data Exploration & Strategy Formulation
### Business Question

Which crops show the strongest production and productivity trends, and where are there potential agribusiness opportunities or risks?

### Dataset

The initial analysis uses agricultural statistics published by the Government of India – Department of Agriculture & Farmers Welfare (DES).

The analysis focuses on:

Crop
Area
Production
Yield
Five-year normal-estimate periods
Crops Analyzed
🌾 Rice
🌾 Wheat
🌽 Maize
🫘 Gram
🥜 Groundnut
🌱 Rapeseed & Mustard
🌱 Soybean
🔎 Initial Insights

The initial exploratory analysis indicates:

Total foodgrain production increased from 285.71 million tonnes in the earliest normal period to 329.22 million tonnes in the latest normal period.
Rice production increased from 114.45 Mt to 135.52 Mt.
Wheat production increased from 102.46 Mt to 111.82 Mt.
Maize production increased from 27.78 Mt to 36.91 Mt.
Groundnut production increased from 8.35 Mt to 10.56 Mt.
Rapeseed & mustard production increased from 8.68 Mt to 12.15 Mt.
Soybean production increased from 12.15 Mt to 13.78 Mt.
Yield improvements were observed for most of the selected crops.

These findings are descriptive and do not establish causal relationships.

## 📈 Analysis Performed

The Week 1 analysis includes:

Data inspection
Data profiling
Production trend analysis
Yield comparison
Production change analysis
Identification of potential opportunity areas
Initial agribusiness interpretation
Key Outputs

📈 Crop production trends
📊 Production change comparison
🌱 Yield change comparison
🌾 Total foodgrain production trend

The charts are available in:

Week-01/outputs/

## 🧠 Methodology

The project follows a staged analytical approach:

Data Acquisition
Data Cleaning
Data Validation
Exploratory Data Analysis
Trend Analysis
Productivity Analysis
Climate & Market Integration
Business Interpretation

Machine learning will only be considered after sufficient data quality and temporal consistency have been established.

## 💼 Agribusiness Applications

The analysis can potentially support:

Procurement planning
Agricultural input demand planning
Food processing opportunities
Storage and logistics planning
Crop diversification analysis
Market intelligence
Climate risk assessment
🛠️ Tools & Technologies
Python
Pandas
NumPy
Matplotlib
Jupyter Notebook
Git & GitHub
Microsoft Excel
Power BI (planned/optional)

## 📚 Data Sources

The project prioritizes official public agricultural data sources.

Government of India – DES
Department of Agriculture & Farmers Welfare
Agricultural Statistics at a Glance
Official DES Publications
Agriculture Dashboard
DES Agriculture Dashboard

## 📌 Week 2 – Data Collection, Preparation & Cleaning

### 🎯 Objective

Week 2 focused on developing a systematic and reproducible approach for collecting, preparing, cleaning, and validating agricultural data for the India-focused agribusiness intelligence project.

The goal was to establish a reliable data pipeline that can later combine crop production, productivity, climate, and agricultural market information for deeper analysis.

### 📊 Data Sources Identified

The following public data sources were evaluated for their relevance to the project:

- **Directorate of Economics & Statistics (DES), Government of India** – Area, Production & Yield (APY) data at state, district, crop, season, and year levels.
- **India Open Government Data (data.gov.in)** – District-wise and season-wise agricultural production statistics.
- **Agmarknet** – Agricultural market arrivals and price information.
- **FAOSTAT** – National crop production, harvested area, and yield data for cross-validation.
- **Rainfall & Climate Data** – Planned for integration to study the relationship between weather conditions and agricultural productivity.

### 🧹 Data Cleaning & Preparation

A structured data-cleaning pipeline was developed covering:

- Schema and data-type validation
- Missing-value profiling
- Duplicate detection
- Crop-name standardization
- Unit validation and normalization
- Negative-value and range checks
- Outlier identification
- Geographic and categorical standardization
- Production–area–yield consistency checks
- Derived feature creation
- Final dataset validation

The workflow follows:

**Raw Data → Profiling → Cleaning → Standardization → Validation → Transformation → Processed Dataset**

### 🔍 Feature Engineering

Several analytical features were planned and implemented, including:

- Production Growth %
- Yield Growth %
- Area Growth %
- Yield Gap
- Crop Production Share
- Rainfall Deviation %
- Market Price Volatility

These features will support future analysis of agricultural productivity, supply growth, climate exposure, and agribusiness opportunities.

### 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Requests
- BeautifulSoup
- OpenPyXL
- Jupyter Notebook
- VS Code
- Microsoft Excel
- Git & GitHub

### 📁 Week 2 Deliverables

The Week 2 folder contains:

```text
Week-02/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   ├── processed/
│   └── reference/
├── notebooks/
│   └── Week_2_Data_Collection_and_Cleaning.ipynb
├── scripts/
│   └── generate_quality_report.py
├── outputs/
│   └── quality_reports/
└── docs/
    ├── data_dictionary.csv
    ├── source_register.csv
    └── Week_2_Data_Collection_Preparation_Cleaning_Plan.docx

## 👨‍💻 Author
```
Aabir Bhowmik
Junior Data Science Analyst – Agriculture & Agribusiness
```
