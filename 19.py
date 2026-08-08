student_details = {}
name = input("STUDENT NAME : ")
age = int(input("STUDENT AGE : "))
city = input("STUDENT CITY : ")

#ADD DATA TO DICTIONARY
print("\nAFTER ADDING DATA")
student_details["NAME"] = name
student_details["AGE"] = age
student_details["CITY"] = city
print(student_details)

#UPDATE DATA OF DICTIONARY
print("\nAFTER UPDATE DATA")
student_details["NAME"] = "SATYAM"
student_details["AGE"] = '20'
student_details.update({"CITY":"AHEMDABAD"})
print(student_details)

#DELETION ON DATA OF DICTIONARY
print("\nAFTER DELETING DATA")
student_details.clear()
print(student_details)