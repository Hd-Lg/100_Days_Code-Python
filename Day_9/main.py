# To create a dic:
programming_dictionary = {
    "Bug": "An error in a program",
    "Function": "A piece of code",
}

# To retrieve a value in a dic:
programming_dictionary["Bug"]

# To add new item
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Wipe the dic
programming_dictionary = {}

# Edit item
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through dic
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille"],
        "total_visits": 12
    },
    "Germany": ["Berlin"]
}

travel_log = [

    {
        "country": "France",
        "cities_visited": ["Paris", "Lille"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visited": 5
    }
]
