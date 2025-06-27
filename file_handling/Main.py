'''f1 = open("File_01", "r")
print(f1.read())

f2 = open("File_02","w")
f2.write("Vegash")'''




# Checking What are all the Mode Creating file if file doesnt exist
'''''''''''f3 = open("File_03","r")'''
f4 = open("File_04","w")
f5 = open("File_05","a")
f6 = open("File_06","w+")
f7 = open("File_07","r+")
f8 = open("File_08","a+")



f4.write("Bangalore Chennai Delhi Hydrabad Telgana")
f5.write("Banana")


f6.write("Fruit Vegatables")
f6.seek(0)
print(f6.read())


print(f7.read())
f7.write("F7 Writing")

f8.write("Appending")
f8.seek(0)
print(f8.read())




