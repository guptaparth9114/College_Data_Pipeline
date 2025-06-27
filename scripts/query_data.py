import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaypee@123",
    database="college_db"
)

# Query 1: Top 5 Colleges by Placement (using 'Placement' column)
query1 = """
SELECT name, Placement
FROM colleges
ORDER BY Placement DESC
LIMIT 5;
"""
df1 = pd.read_sql(query1, conn)
print("\n🔝 Top 5 Colleges by Placement:\n")
print(df1)

# Query 2: Average UG Fee by State
query2 = """
SELECT state, AVG(UG_fee) AS avg_ug_fee
FROM colleges
GROUP BY state
ORDER BY avg_ug_fee DESC;
"""
df2 = pd.read_sql(query2, conn)
print("\n💸 Average UG Fee by State:\n")
print(df2)

# Query 3: Number of Colleges by State (since no 'program_offered')
query3 = """
SELECT state, COUNT(*) AS num_colleges
FROM colleges
GROUP BY state
ORDER BY num_colleges DESC;
"""
df3 = pd.read_sq_
