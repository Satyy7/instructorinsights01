import csv
import psycopg2
from psycopg2 import sql
from decouple import config


conn = psycopg2.connect(dbname=config('DB_NAME'), user=config('DB_USER'), password=config('DB_PASSWORD'), host=config('DB_HOST'))

cur = conn.cursor()

with open('./csv/cleaned_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        insert_query = sql.SQL(
            "INSERT INTO professors (name, rating, rating_count, department, would_take_again) VALUES (%s, %s, %s, %s, %s)"
        )
        
        name = row['Name']
        rating = float(row['Rating']) 
        rating_count = row['Rating Count'] 
        department = row['Department']
        would_take_again = row['Would Take Again %'] 
        
        cur.execute(insert_query, (name, rating, rating_count, department, would_take_again))
        
    conn.commit()

cur.close()
conn.close()

print("Data loaded successfully")
