from typing import List, Dict, Any

from faker import Faker

fake = Faker()


def generate_student(student_id: int) -> Dict[str, Any]:
    student_info: Dict[str, Any] = {
        "ID": student_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": fake.random_int(min=18, max=80)
    }
    return student_info

def generate_students(count: int) -> List[Dict[str, Any]]:
    students_list: List[Dict[str, Any]] = []
    for i in range(1, count + 1):
        single_student = generate_student(i)
        students_list.append(single_student)
    return students_list

if __name__ == "__main__":
    generated_data = generate_students(3)
    
print(generated_data)