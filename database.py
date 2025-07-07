# Creates and fills the extended shelter database for flood

import sqlite3

conn = sqlite3.connect('shelter.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS shelters")

c.execute("""
    CREATE TABLE shelters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        capacity INTEGER,
        available_beds INTEGER,
        distance REAL,
        accessibility TEXT,
        elevation_level TEXT,
        proximity_to_water TEXT,
        medical_facility TEXT
    )
""")

shelters_data = [
    ('Shelter A', 100, 30, 2.5, 'easy',     'high',   'moderate', 'advanced'),
    ('Shelter B', 80, 5, 5.0, 'moderate',   'medium', 'very close', 'basic'),
    ('Shelter C', 60, 10, 1.0, 'difficult', 'low',    'very close', 'none'),
    ('Shelter D', 120, 50, 3.0, 'easy',     'high',   'far',        'advanced'),
    ('Shelter E', 90, 20, 6.5, 'moderate',  'medium', 'moderate',   'basic'),
    ('Shelter F', 70, 0, 4.5, 'difficult',  'low',    'very close', 'none'),
    ('Shelter G', 85, 15, 2.0, 'moderate',  'medium', 'moderate',   'basic'),
    ('Shelter H', 110, 40, 3.8, 'easy',     'high',   'far',        'advanced'),
    ('Shelter I', 95, 25, 7.0, 'difficult', 'medium', 'far',        'basic'),
    ('Shelter J', 75, 18, 1.5, 'moderate',  'medium', 'moderate',   'basic'),
    ('Shelter K', 65, 22, 2.2, 'easy',      'medium', 'moderate',   'basic'),
    ('Shelter L', 55, 5, 6.2, 'difficult',  'low',    'very close', 'none'),
    ('Shelter M', 105, 35, 4.0, 'moderate', 'high',   'moderate',   'advanced'),
    ('Shelter N', 60, 8, 8.0, 'moderate',   'medium', 'far',        'basic'),
    ('Shelter O', 130, 60, 3.5, 'easy',     'high',   'far',        'advanced'),
    ('Shelter P', 40, 15, 9.0, 'difficult', 'low',    'very close', 'none'),
    ('Shelter Q', 90, 25, 5.5, 'moderate',  'medium', 'moderate',   'basic'),
    ('Shelter R', 100, 30, 1.8, 'easy',     'high',   'moderate',   'advanced'),
    ('Shelter S', 80, 12, 4.8, 'moderate',  'medium', 'very close', 'basic'),
    ('Shelter T', 95, 27, 6.0, 'difficult', 'medium', 'far',        'basic'),
    ('Shelter U', 50, 50, 10.0, 'easy',     'medium', 'far',        'none'),
    ('Shelter V', 120, 5, 0.5, 'difficult', 'low',    'very close', 'none'),
    ('Shelter W', 75, 18, 7.2, 'moderate',  'low',    'moderate',   'basic'),
    ('Shelter X', 90, 20, 3.3, 'easy',      'high',   'moderate',   'advanced'),
    ('Shelter Y', 110, 0, 5.5, 'moderate',  'medium', 'far',        'none'),
    ('Shelter Z', 60, 40, 2.0, 'difficult', 'medium', 'moderate',   'basic'),
]

c.executemany("""
    INSERT INTO shelters 
    (name, capacity, available_beds, distance, accessibility, elevation_level, proximity_to_water, medical_facility)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", shelters_data)

conn.commit()
conn.close()

print("Done")


