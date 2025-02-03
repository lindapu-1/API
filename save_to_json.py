import json
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Load the existing data from the database
cursor.execute("SELECT id, action, date, points FROM api_sustainabilityaction")  # Replace 'your_table_name' with the actual table name
data = cursor.fetchall()

# Transform the data
transformed_data = []
for item in data:
    transformed_data.append({
        "id": item[0],  # Assuming 'pk' is the first column
        "action": item[1],  # Assuming 'action' is the second column
        "date": item[2],  # Assuming 'date' is the third column
        "points": item[3]  # Assuming 'points' is the fourth column
    })

# Write the transformed data to a new JSON file
with open('ex_data.json', 'w') as outfile:
       json.dump(transformed_data, outfile, indent=4)

print("Data transformed and saved to ex_data.json")

# Close the database connection
