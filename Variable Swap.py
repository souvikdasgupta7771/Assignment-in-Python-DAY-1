#Swap two Numbers without using temporary variable
#Two Integer Inputs from the user and swap them without using temporary variable

a=int(input("Please Enter the Value of a : "))
b=int(input("Please Enter the Value of b : "))
print("Result Before Swapping The Value of a & b  is: ",a,b)
a,b=b,a
print("Result After Swapping: ")
print("After swapping the value of a is: ",a)
print("After swapping the value of b is: ",b)
