students=["Bruno","Minion","Oreo","Goofy","Max"]
search=input("Search for student: ")
if search in students:
    print("{} found at position {}".format(search,students.index(search)+1))
else:
    print("{} not found".format(search))