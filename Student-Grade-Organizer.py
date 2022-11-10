'''---------------------------------------------------

Gabriela Muriel

----------------------------------------------------------'''


import os
print('---------------------------------------------------')
print("\n\nHello and Welcome!\n\n")

def name():

    file_name = input("\n\nPlease enter file name: ")
    i = 0
    while(not os.path.isfile(file_name)):

      if i >= 2:
          print('\n\nError!')
          exit(1)
          
      print("\n\nThis file does not exist. Please enter a valid file name.")
      i += 1
      file_name = input("\n\nPlease enter file name: ")
        
    return file_name
    
file_name = name()

print(file_name, "is Real!")
print(' ')

myfile = open(file_name, 'r')
contents = myfile.readlines()
myfile.close()

contents = [i.split('\n')[0] for i in contents]

student_grades = {}

def isFloat(string):
  for c in string:
    if not c.isnumeric() and c != '.':
      return False
  return True

student_grades = {}
student_numbers = {}
names_to_grades = {}

for line in contents:

  line_split = line.split(' ')
  
  if not isFloat(line_split[2]):
    student_grades[line_split[0] + line_split[1]] = []
    student_numbers[line_split[0] + line_split[1]] = line_split[2]
    
  else:
    student_grades[line_split[0] + line_split[1]].append(line_split[2])

for student_num,grades in student_grades.items():

  avg = 0
  for grade in grades:
    avg = (avg + float(grade))
  if len(grades) == 0:
    avg = 0
  else:
    avg = avg / len(grades)

  print(student_numbers[student_num], ' '.join(grades), round(avg, 2)) 

print('\n\n---------------------------------------------------')
