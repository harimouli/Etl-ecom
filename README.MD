# 🛒 ETL E-commerce Data Pipeline

## 📌 Overview

This project is a simple ETL (Extract, Transform, Load) pipeline where I worked with e-commerce data to understand how raw data is cleaned and prepared for analysis.

The main goal was to learn how data flows from raw input to a usable format.

---

## 🚀 Tech Stack

- Python
- Pandas

---

## 🔄 ETL Pipeline Flow

### 1. Extract

- Loaded raw data from a CSV file (`data.csv`)
- This file contains sample e-commerce transaction data

### 2. Transform

- Handled missing values
- Removed duplicate records
- Cleaned and formatted columns
- Ensured data is consistent and ready for use

### 3. Load

- Saved the cleaned data into a new file (`output.csv`)
- This data can now be used for analysis or reporting

---

## 📂 Project Structure

    ETL-ECOMDATA/
    │
    ├── data.csv # Raw input data
    ├── etl.py # ETL script
    ├── output.csv # Cleaned data
    └── README.md # Documentation

---

## 🧠 What I Learned

- Basics of ETL process
- How to clean and preprocess data
- Handling null values and duplicates
- Writing simple data pipelines using Python

---

## ▶️ How to Run

1. Install dependencies:

```bash
    pip install pandas
Run the script:
    python etl.py
Use Cases
Preparing data for analysis
Learning data pipeline basics
Understanding real-world data cleaning
```
