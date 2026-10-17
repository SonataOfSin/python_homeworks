import json


def add_multiple_persons(count):
    file_name = "persons.json"


    with open(file_name, "r",) as file:
        persons_list = json.load(file)



#vigebt bolo chanaweris id, risi mixedvitac davamatebt axa id-ebs


    if persons_list:
        last_id = persons_list[-1]["id"]
    else:
        last_id = 0


#vekitxebit ramdenjerac gvaqvs mocemuli
    for _ in range(count):
        name = input("enter your name: ")
        age = int(input("enter your age: "))

        last_id += 1
        new_person = {
            "id": last_id,
            "name": name,
            "age": age
        }

        persons_list.append(new_person)



#sabolood vwert failshi

    with open(file_name, "w",) as file:
        json.dump(persons_list, file, indent=4)



# --- testireba ---
add_multiple_persons(2)