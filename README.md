# 🎓 College Data Pipeline – From Kaggle to Visualization

A mini data analytics project that builds a complete pipeline to collect, clean, store, query, and visualize data related to Indian engineering colleges using Python, MySQL, Pandas, and Matplotlib.

---

## 📌 Objective

To demonstrate a full data pipeline by:
- Collecting a dummy college dataset
- Importing and cleaning the data
- Storing it in a MySQL database
- Running queries to answer common analytical questions
- Visualizing results through plots

---

## 📁 Project Structure


---

## ⚙️ Technologies Used

- **Python 3.12**
- **MySQL 8.x**
- **Pandas**
- **Matplotlib**
- **MySQL Connector**

---

## 📊 Dataset Description

The dataset includes:
- College Name, State
- UG/PG Tuition Fees
- Ratings on: Academic, Accommodation, Faculty, Infrastructure, Placement, Social Life

---

## ✅ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/your-username/College_Data_Pipeline.git
cd College_Data_Pipeline

### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt

### 3. Install Dependencies

pip install pandas matplotlib mysql-connector-python

### 3. Setup MYSQL Database

mysql -u root -p
mysql> CREATE DATABASE college_db;
mysql> USE college_db;
mysql> SOURCE db/create_tables.sql;

### 4.Load Data into MySQL

python scripts/load_data.py

### 5.Query Examples

python scripts/query_data.py

### 6.Visualizations

python scripts/plot_data.py

### Author

Parth Gupta
