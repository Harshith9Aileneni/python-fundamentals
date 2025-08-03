import json


persons = [{"name" : "harsh", "age": 25, "city": "unknown"},
{"name" : "harsh", "age": 25, "city": "unknown"},
{"name" : "harsh", "age": 25, "city": "unknown"}
]



with open("persons.json", "w") as file:
    json.dump(persons, file)

with open("persons.json","r") as file:
    loaded_person=json.load(file)
    print(loaded_person)
    for person in persons:
        print(f"name : {person['name']}, age : {person['age']}")
