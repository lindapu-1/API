# Sustainability Action Management System

This system manages and tracks sustainability actions. The API supports creating, retrieving, updating, and deleting sustainability actions.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/lindapu-1/API.git
   cd api
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```

## Retrieve Information from a JSON File

If you have previous records stored in a JSON file, you should retrieve them to the database first by running:

```bash
python retreive_from_json.py
```

This script will read the JSON file and insert the data into the database. The script use ex_data.json as example.

## Running the Server

To run the server, use the following command:

```bash
python manage.py runserver
```

This will start the server and you can access the API at `http://localhost:8000/api/actions/`.

You can then use GET and POST requests to change the records on the webpage.

## Exporting Records to JSON

If you want to export the records to a JSON file as a copy, run:

```bash
python save_to_json.py
```

This will create a new JSON file with the current records.
