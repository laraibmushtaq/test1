import csv
import json

emps = []
number_of_employee_in_department=0

def read_records():
    global emps
    with open("emp.csv") as f:
        rows = csv.DictReader(f)
        emps = [x for x in rows]


def correct_types(data):
    for e in data:
        e['age'] = int(e['age'])


def calculate_number_of_employe():
    global number_of_employee_in_department
    number_of_employee_in_department+=1
    return 1


def read_json_records():
    print("\nReading from json file\n")
    global profs
    profs = json.load(open("emp_json.json"))


# average employee age
def find_average_age(emp_data):
    avg_age = sum([x['age'] for x in emp_data]) / len(emp_data)
    return avg_age


# TODO:: implement this
def find_average_age_for_dept(dept,emp_data):
    global number_of_employee_in_department
    number_of_employee_in_department = 0
    try:
        avg_age = sum([x['age'] for x in emp_data if x['dept'] == dept if
                       (calculate_number_of_employe())]) / number_of_employee_in_department
        return avg_age
    except ZeroDivisionError:
        return 0.0


def main():
    read_records()
    correct_types(emps)
    print("Average emp age is:", find_average_age(emps))

    print("Average emp age for dept d1:", find_average_age_for_dept("d1",emps))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2",emps))

    # TODO: Do same thing with json file instead of csv file
    print("Average emp age is:", find_average_age(profs))
    print("Average emp age for dept d1:", find_average_age_for_dept("d1", profs))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2", profs))


if __name__ == "__main__":
    main()
