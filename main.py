import random

suggested_destinations = ["Florence", "Prague", "Las Vegas", "Miami", "Munich"]
suggested_restaurants = ["Mercato Centrale", "Dvinis", "Delilah", "Klaw Miami", "Galleria", "Doner Kebab", "McDonalds" ]
suggested_transportation = ["Train", "Airplane", "Cruise Ship", "Car", "Spaceship", "Teleport"]
suggested_entertainment = ["Cirque de Soleil", "Art Gallery", "City Tour", "Beer Garden", "Sky diving"]


def pick_destination():
    return random.choice(suggested_destinations)

def pick_restaurant():
    return random.choice(suggested_restaurants)

def pick_transportation():
    return random.choice(suggested_transportation)

def pick_entertainment():
    return random.choice(suggested_entertainment)

def view_trip(destination, restaurant, transportation, entertainment):
    print("\nTrip Itinerary:")
    print(f"Destination: {destination}")
    print(f"Restaurant: {restaurant}")
    print(f"Transportation: {transportation}")
    print(f"Entertainment: {entertainment}")

def verify_trip():
    destination = pick_destination()
    restaurant = pick_restaurant()
    transportation = pick_transportation()
    entertainment = pick_entertainment()
    view_trip(destination, restaurant, transportation, entertainment)

    while True:
        confirm_trip = input("Do you want to go on this trip? (y) for yes or (n) for no: ")
        if confirm_trip.lower() == "y":
            print("Have a great trip!")
            view_trip(destination, restaurant, transportation, entertainment)
            break
        elif confirm_trip.lower() == "n":
            change_trip = input("What part of your trip would you like to change? ")
            change_trip = change_trip.lower()

            if change_trip == "destination":
                destination = pick_destination()
                view_trip(destination, restaurant, transportation, entertainment)
            elif change_trip == "restaurant":
                restaurant = pick_restaurant()
                view_trip(destination, restaurant, transportation, entertainment)
            elif change_trip == "transportation":
                transportation = pick_transportation()
                view_trip(destination, restaurant, transportation, entertainment)
            elif change_trip == "entertainment":
                entertainment = pick_entertainment()
                view_trip(destination, restaurant, transportation, entertainment)
            else:
                print("Sorry that is not a valid choice..")
                

        else:
            print("Sorry that is not a valid choice...")


verify_trip()
