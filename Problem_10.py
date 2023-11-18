# fast_number = int(input())
# last_number = int(input())
# data = []
# for number in range(fast_number, last_number + 1):
#     if number > 1:
#         for i in range(2, number):
#             if number % 2 == 0:
#                 break
#         else:
#             data.append(number)
# print(data)

if __name__ == '__main__':
    student_data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_data.append([name, score])

student = student_data
student.sort(key=lambda student: abs(student[1]))
# print(student)

if student[1][1] == student[2][1]:
    print(f'{student[1][0]}\n{student[2][0]}')
