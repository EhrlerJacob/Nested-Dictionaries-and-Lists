x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x =[ [5,2,3], [15,8,9] ]
print(x)

students[0]["last_name"] = "Bryant"
print(students[0])

sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'][0])

z = [ {'x':10, 'y':30} ]
print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(students):
    for one_student in students:
        output = ''
        for key, value in one_student.items():
            output += f' {key} - {value}, '
        print(output)
        
iterateDictionary(students)

def iterateDictionary2(key_name,some_list):
    for one_student in some_list:
        print(one_student[key_name])

iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key, val in dict.items():
        print('----------')
        print(f"{len(val)} {key.upper()}")
        for i in range(0,len(val)):
            print(val[i])

printInfo(dojo)