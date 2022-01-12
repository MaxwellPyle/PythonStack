x = [ [5,2,3], [15,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

def iterateDictionary(dir):
    for list in dir:
        for key in list:
            print(key + " - " + list[key])
iterateDictionary(students)

def iterateDictionary2(key_name,dir):
    for list in dir:
        for key in list:
            if key == key_name:
                print(list[key])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for r in dict:
        print(len(dict[r]),r.upper())
        for d in dict[r]:
            print(d)
printInfo(dojo)