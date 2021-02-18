# tax calculator

income = float(input("Enter the annual income: "))

# if income is < 85,528, PIT is income * 18% - 556.02
# if income is > 85,528, PIT is (income - 85,528)*32%, + 14,839.02

lowerTaxRate = 0.18
higherTaxRate = 0.32

if income<85528:
    tax=((income*lowerTaxRate)-556.02)
    if tax<0: tax=0
else:
    tax=(((income-85528)*higherTaxRate)+14839.02)


tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# completed successfully 