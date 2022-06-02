import pandas
students = pandas.read_excel('input.xlsx', sheet_name='Students')

students_sort = students.sort_values(by=['level'])
print(students)
students_filtr = students[students['period'].notnull()]
print(students_filtr)
students_filtr.to_excel('output_students.xlsx')