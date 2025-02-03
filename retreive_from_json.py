import json
import sqlite3

# Load data from sustainabilityaction.json
with open('ex_data.json', 'r') as infile:
    data = json.load(infile)

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Insert or update the api_sustainabilityaction table based on the data from the JSON file
for item in data:
    # Check if the record exists
    cursor.execute("SELECT COUNT(*) FROM api_sustainabilityaction WHERE id = ?", (item['id'],))
    exists = cursor.fetchone()[0]

    if exists:
        # Update the existing record
        cursor.execute("""
            UPDATE api_sustainabilityaction
            SET action = ?, date = ?, points = ?
            WHERE id = ?
        """, (item['action'], item['date'], item['points'], item['id']))
    else:
        # Insert a new record
        cursor.execute("""
            INSERT INTO api_sustainabilityaction (id, action, date, points)
            VALUES (?, ?, ?, ?)
        """, (item['id'], item['action'], item['date'], item['points']))

# Commit the changes and close the database connection
conn.commit()
conn.close()

print("api_sustainabilityaction table updated successfully.")