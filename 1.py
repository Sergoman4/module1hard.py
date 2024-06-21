import statistics
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
good = statistics.mean(grades[0])
good1 = statistics.mean(grades[1])
good2 = statistics.mean(grades[2])
good3 = statistics.mean(grades[3])
good4 = statistics.mean(grades[4])
students1 = sorted(list(students))
bal = {(students1[0]): good, (students1[1]): good1, (students1[2]): good2, (students1[3]): good3, (students1[4]): good4,}
print('Список студентов', students)
key = input("Введите имя из указаных сверху : ")
print("Значение:", bal[key])
