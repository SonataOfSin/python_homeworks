persons = [
    ('Kelly', 'Simpson', 26), ('Erika', 'Stephens', 24), ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49), ('Christine', 'Gordon', 23), ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36), ('Cindy', 'Escobar', 41), ('Cindy', 'White', 33), 
    ('Joel', 'Hall', 43), ('Steven', 'Winters', 28), ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32), ('Alex', 'White', 42), ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43), ('Traci', 'Wells', 38), ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29), ('Kevin', 'Willis', 57), ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43), ('Thomas', 'Mason', 37)
]


while True:
    print("-" * 30) 
    first_name = input("enter name (for end type stop): ").strip()
    if first_name.lower() == "stop":
        print("end of program")
        break
    name_exists = False
    for p in persons:
        if p[0].lower() == first_name.lower():
            name_exists = True
            break 
    if not name_exists:
        print("such name is not is list.")
        continue 
    last_name = input(f"name '{first_name}' is found. enter surname (or 'stop' to end): ").strip()
    if last_name.lower() == "stop":
        print("end of program")
        break
    person_found = None
    for p in persons:
        if p[0].lower() == first_name.lower() and p[1].lower() == last_name.lower():
            person_found = p
            break
    if person_found:
        print(f"found: {person_found[0]} {person_found[1]} - age: {person_found[2]} years old.")
    else:
        print("no such surname for this name was found.")