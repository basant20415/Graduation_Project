import sqlite3

conn = sqlite3.connect('damages.db')
cursor = conn.cursor()

cursor.executescript('''
DROP TABLE IF EXISTS road_damage;

CREATE TABLE road_damage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL,
    longitude REAL,
    type TEXT,
    description TEXT,
    UNIQUE(latitude, longitude, type)
);
''')

conn.commit()
conn.close()

print("✅ Database created successfully.")