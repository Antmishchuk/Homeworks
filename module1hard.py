average_rating = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
ave_grades = []
for i in range(len(grades)):
    ave_grades.append(sum(grades[i])/len(grades[i]))
students_sort = sorted(students)
average_rating = dict(zip(students_sort, ave_grades))
print(average_rating)