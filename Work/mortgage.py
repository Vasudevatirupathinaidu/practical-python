# mortgage.py
'''Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.

Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:'''

# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)


# Exercise 1.8
'''Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?'''

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
month = 0

while principal > 0:

    month = month + 1

    if month < 13:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment

    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid, 'over', month, 'months')



# Exercise 1.9
'''How much will Dave pay if he pays an extra $1000/month for 4 years starting in year 5 of the mortgage?'''

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# extra_payment = 1000
# extra_payment_start_month = 60
# extra_payment_end_month = 108
# month = 0

# while principal > 0:
#     month = month + 1

# print('Total paid', total_paid, 'over', month, 'months')


# Exercise 1.10: Making a table
'''
Modify the program to print out a table showing the month, total paid so far, and the remaining principal. The output should look something like this:

1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
4 10736.44 497581.83
5 13420.55 496970.98
...
308 875705.88 674.44
309 878389.99 -2006.86
Total paid 878389.99
Months 309
'''
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000.0
extra_payment_start_month = 60
extra_payment_end_month = 108
month = 0

while principal > 0:
    month = month + 1

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(month, round(total_paid,2), round(principal,2))

print('Total paid', round(total_paid,2))
print('Months', month)
