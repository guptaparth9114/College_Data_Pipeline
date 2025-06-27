import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os


os.makedirs('../plots', exist_ok=True)


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaypee@123",
    database="college_db"
)


query1 = """
SELECT state, AVG(UG_fee) AS avg_ug_fee
FROM colleges
GROUP BY state
ORDER BY avg_ug_fee DESC;
"""
df_fee = pd.read_sql(query1, conn)


plt.figure(figsize=(12, 6))
plt.bar(df_fee['state'], df_fee['avg_ug_fee'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Average UG Fee by State")
plt.ylabel("Fee (₹)")
plt.xlabel("State")
plt.tight_layout()
plt.savefig('../plots/avg_ug_fee_by_state.png')  
plt.close()


query2 = """
SELECT name, Placement
FROM colleges
ORDER BY Placement DESC
LIMIT 5;
"""
df_place = pd.read_sql(query2, conn)


plt.figure(figsize=(10, 5))
plt.barh(df_place['name'], df_place['Placement'], color='seagreen')
plt.xlabel("Placement Rating")
plt.title("Top 5 Colleges by Placement")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('../plots/top_5_colleges_by_placement.png')  
plt.close()

conn.close()

print("✅ Plots generated and saved in 'plots/' folder.")
