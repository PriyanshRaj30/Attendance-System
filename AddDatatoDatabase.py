from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['attendance_system']  # Replace with your database name
students_collection = db['students']  # Replace with your collection name

# Data to be inserted
data = {
    "321654": {
        "name": "Murtaza Hassan",
        "major": "Robotics",
        "starting_year": 2017,
        "total_attendance": 7,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "852741": {
        "name": "Emly Blunt",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "123": {
        "name": "Priyansh Raj",
        "major": "CS",
        "starting_year": 2020,
        "total_attendance": 0,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

# Insert data into MongoDB
for key, value in data.items():
    # Use upsert=True to insert or update the document
    students_collection.update_one({'_id': key}, {'$set': value}, upsert=True)

print("Data successfully stored in MongoDB.")