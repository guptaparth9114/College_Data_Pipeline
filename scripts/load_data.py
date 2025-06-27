import pandas as pd
import mysql.connector


df = pd.read_csv('../data/Indian_Engineering_Colleges_Dataset.csv')
df = df.drop(columns=['Unnamed: 0'])


def clean_fee(val):
    try:
        return int(str(val).replace(",", "").strip())
    except:
        return 0

df['UG_fee'] = df['UG_fee'].apply(clean_fee)
df['PG_fee'] = df['PG_fee'].apply(clean_fee)


float_columns = ['Rating', 'Academic', 'Accommodation', 'Faculty', 'Infrastructure', 'Placement', 'Social_Life']
for col in float_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaypee@123",
    database="college_db"
)
cursor = conn.cursor()


for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO colleges (
            name, state, ug_fee, pg_fee, rating,
            academic, accommodation, faculty, infrastructure, placement, social_life
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['College_Name'], row['State'], row['UG_fee'], row['PG_fee'], row['Rating'],
        row['Academic'], row['Accommodation'], row['Faculty'],
        row['Infrastructure'], row['Placement'], row['Social_Life']
    ))

conn.commit()
cursor.close()
conn.close()

print(" Data imported successfully.")
