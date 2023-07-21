#some examples of nested dictionaries for complex data

dictionary_1 = {
    "key1": ["list"],
    "key2": {"dictionary 2": "Your value here"}
}

capitals = {
    "France": "Paris",
    "Germany": "berlin"
}

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a dictionary in a dictionary
travel_log["France"] = {"cities_visited": travel_log["France"], "total_visits": 12}
## print(travel_log)

#Nesting dictionary in lists
travel_log_2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

print(travel_log_2)