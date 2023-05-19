import random

suggested_destinations = ["Florence", "Prague", "Las Vegas", "Miami", "Munich"]
suggested_restaurants = ["Mercato Centrale", "Dvinis", "Delilah", "Klaw Miami", "Galleria" ]
suggested_transportation = ["Train", "Airplane", "Cruise Ship", "Car", "Spaceship"]
suggested_entertainment = ["Cirque de Soleil", "Art Gallery", "City Tour", "Beer Garden", "Sky diving"]

def pick_destination():
    return random.choice(suggested_destinations)

def pick_restaurant():
    return random.choice(suggested_restaurants)

def pick_transportation():
    return random.choice(suggested_transportation)

def pick_entertainment():
    return random.choice(suggested_entertainment)

print(f"Destination: {pick_destination()}")
print(f"Restaurant: {pick_restaurant()}")
print(f"Transportation: {pick_transportation()}")
print(f"Entertainment: {pick_entertainment()}")