# Main script to take input, query database, and evaluate fuzzy scores

import sqlite3
from membership_func import get_fuzzy_simulator


num_people = int(input("Enter the number of people who need shelter: "))
distance_level = input("How far can you travel? (near / medium / far): ").strip().lower()
accessibility_required = input("What accessibility scenario they can afford to have? (easy/moderate/difficult): ").strip().lower()
elevation_input = input("What's the elevation level at your location? (low / medium / high): ").strip().lower()
proximity_input = input("How close are you to a water body? (very close / moderate / far): ").strip().lower()
medical_input = input("What kind of medical help do you need? (none / basic / advanced): ").strip().lower()

distance_map = {
    "near": 3,
    "medium": 10,
    "far": 18
}
max_distance = distance_map.get(distance_level, 10)  

elevation_map = {"low": 2, "medium": 5, "high": 8}
proximity_map = {"very close": 2, "moderate": 5, "far": 8}
medical_map = {"none": 2, "basic": 5, "advanced": 8}

elevation_num = elevation_map.get(elevation_input, 5)
proximity_num = proximity_map.get(proximity_input, 5)
medical_num = medical_map.get(medical_input, 5)

conn = sqlite3.connect("shelter.db")
c = conn.cursor()

query = """
SELECT name, capacity, available_beds, distance, accessibility FROM shelters
WHERE available_beds >= ?
AND distance <= ?
AND LOWER(accessibility) = ?
"""

c.execute(query, (num_people, max_distance, accessibility_required))
matching_shelters = c.fetchall()
conn.close()

if matching_shelters:
    print("\nMatching shelters:")
    for s in matching_shelters:
        name, cap, bed, dis, access = s
        print(f"Name: {name}, Capacity: {cap}, Available Beds: {bed}, Distance: {dis} km, Accessibility: {access}")
else:
    print("\nNo shelters match your criteria.")


if matching_shelters:
    print("\nMatching shelters (acc. to fuzzy logic):\n")
    access_map = {
        "difficult": 2,
        "moderate": 5,
        "easy": 8
    }

    best_shelter = None
    best_score = -1



    for shelter in matching_shelters:
          name, cap, bed, dis, access = shelter
    access_num = access_map.get(access.lower(), 5)

    try:
        score = get_fuzzy_simulator(
            cap, 
            dis, 
            access_num, 
            elevation_num, 
            proximity_num, 
            medical_num
        )

        print(f"--- {name} ---")
        print(f"Capacity: {cap}, Distance: {dis}, Accessibility: {access}")
        print(f"Suitability Score: {score:.2f}\n")

        if score > best_score:
            best_score = score
            best_shelter = name

    except Exception as e:
        print(f"Error evaluating {name}: {e}")


    if best_shelter:
        print(f" Best match: {best_shelter} with score {best_score:.2f}")
    else:
        print(" No suitable shelter found after fuzzy evaluation.")
else:
    print("\nNo shelters match your criteria.")
