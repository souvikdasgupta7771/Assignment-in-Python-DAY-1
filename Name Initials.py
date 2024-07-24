#Assignment 10: Name Initials Write a program that takes a
#full name as input and outputs the initials in uppercase.
#For example, if the input is "John Doe", the output should be "JD".

print("Name Initials program - ")
Full_name=input("Please enter your full name : ")
name_in_title_format=Full_name.title()
index_of_space=name_in_title_format.find(" ")
name_initials=name_in_title_format[0]+name_in_title_format[index_of_space+1]
print("Hello ",name_initials,"!!")
