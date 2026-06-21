#first homework

def process_text(user_text):
    uppercase_count = sum(1 for char in user_text if char.isupper())
    upper_text = user_text.upper()    
    return uppercase_count, upper_text
input_txt = input("enter text: ")
uppercase_count, upper_text = process_text(input_txt)
print(f"uppercase count: {uppercase_count}")
print(f"uppercased sentence: {upper_text}")


#second homework

def camel_to_snake(camel_str):
    result = []   
    for index, char in enumerate(camel_str):
        if char.isupper() and index > 0:
            result.append('_' + char.lower())
        else:
            result.append(char.lower())
    return "".join(result)
test_cases = ["firstName", "name", "preferredFirstName", "lastName"]
for case in test_cases:
    print(f"{case} -> {camel_to_snake(case)}")
