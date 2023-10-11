def get_student_data(student_list, roll_number):

  for student in student_list:
    if student[0] == roll_number:
      return student
  return None


def main():

  student_list = [
      ['743624', 'CSE', 'Barishal polytechnic institite', '22-23', 'Asraful islam'],
      ['743616', 'CSE', 'Barishal polytechnic institite', '22-23', 'Md sahil'],
      ['743611', 'CSE', 'Barishal polytechnic institite', '22-23', 'Musfiqur rahaman rohan'],
      ['743625', 'CSE', 'Barishal polytechnic institite', '22-23', 'Saikat']
  ]

  roll_number = input("Enter the roll number of the student: ")

  student_data = get_student_data(student_list, roll_number)

  if student_data is None:
    print("Student not found.")
  else:
    print("Student data:")
    print("Roll number:", student_data[0])
    print("Department:", student_data[1])
    print("Institute:", student_data[2])
    print("Session:", student_data[3])
    print("Student name:", student_data[4])

if __name__ == "__main__":
  main()
