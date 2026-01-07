Student={"Name":"Smruti","Roll":333,"Marks":99}
print(Student,type(Student))
print("Marks: ",Student['Marks'])
print("Marks: ",Student.get('Marks'))
print("Name: ",Student['Name'])
print("Name: ",Student.get('Name'))
#print("City: ",Student['City'])
#This Will Give Error 
print("City: ",Student.get('City'))
Student["City"]="Bhubneshwar"
print("After Adding City: ",Student)
Student["Name"]="Mergaret"
print("After Updating The Name: ",Student)
del Student["Marks"]
print("After Deleting Marks: ",Student)
Student.pop("Roll")
print("After Poping Roll: ",Student)
print("Keys: ",list(Student.keys()))
print("Values: ",list(Student.values()))
print("Items: ",list(Student.items()))
Student.clear()
print("After CLearing The Dictionary: ",Student)