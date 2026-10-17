class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"


import json

def serialize_person(person_obj):
    return f"Name: {person_obj.name}, Age: {person_obj.age}"
def deserialize_person(text_line):
    parts = text_line.split(",")
    name = parts[0].split(":")[1].strip()
    age = int(parts[1].split(":")[1].strip())

    return Person(name, age)


p1 = Person("Otar", 35)
file_name = "person_data.json"


#serializacia


serialized_data = serialize_person(p1)

with open(file_name, "w",) as file:
    file.write(serialized_data)


#deserializacia

with open(file_name, "r",) as file:
    read_line = file.readline()

restored_p1 = deserialize_person(read_line)
print(serialized_data)
print(restored_p1)