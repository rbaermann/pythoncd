# 1
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x)
# students[0]['last_name'] = 'Bryant'
# print(students)
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
# z[0]['y'] = 30
# print(z)

#2
# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(some_list):
#     for value in some_list:
#         for key in value:
#             print(f'{key} - {value[key]}', end = ", ")
#         print()
# iterateDictionary(students)

#3
# def iterateDictionaryTwo(key_name, some_list):
#     for value in some_list:
#         print(f'{value[key_name]}')
# iterateDictionaryTwo('first_name', students)
# iterateDictionaryTwo('last_name', students)

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        print(f'{len(some_dict[key])} {key}')
        for value in some_dict[key]:
            print(value)
printInfo(dojo)