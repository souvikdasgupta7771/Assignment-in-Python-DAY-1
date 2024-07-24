# Input principal amount, interest rate, and time period

principal=float(input("Enter the principal amount: "))
rate=float(input("Please Enter the rate of Interest: "))
time=float(input("Please Enter the time period in Years: "))

#Calculate The Simple Interest
interest=(principal*rate*time)/100

#print the  calculated Simple interest
print("Simple Interest: ",interest)

#Total Amount You have to pay with Simple Interest
print("Total Amount You have to pay: principal+interest",principal+interest)
