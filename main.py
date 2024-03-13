# This program is a simple calculator that tells you your monthly car payment

CarPrice = int(input("Enter the price of the vehicle: "))
LoanTerm = int(input("Enter the amount of months you plan to finance the vehicle for: "))
DownPayment = int(input("Enter your downpayment: "))
APR = float(input("Enter the loan percentage: "))
APR = APR*0.01
CarPrice = CarPrice - DownPayment

MonthlyPayment = (CarPrice*(APR/12))/(1-(1+(APR/12))**-LoanTerm)
TotalPrice = MonthlyPayment*LoanTerm
TotalInterest = TotalPrice - CarPrice

print("Your Monthly Payment is: ", MonthlyPayment)
print("The total price of the vehicle: ", TotalPrice)
print("The total interest paid throughout the life of the loan: ", TotalInterest)

