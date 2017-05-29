# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 12:13:40 2017

@author: Linux
"""

balance = 999999
annualInterestRate = 0.18
lowerbound = balance/12
upperbound = balance*(1+annualInterestRate)/12
monthlyPaymentRate = round((upperbound+lowerbound)/2,2)
Rate = 0


# Remaining balance: 31.38
def yearly(balance,annualInterestRate,monthlyPaymentRate):
    month=0
    while month<12:
            balance = round(balance-monthlyPaymentRate,2)
            if balance == 0:
                break
            else:
                balance = round(balance+(balance*monthlyinterest),2)
                month+=1
    return(round(balance,2))
          
while True:
    rate = yearly(balance,annualInterestRate,monthlyPaymentRate)
    
    if rate<0:
        lowerbound = monthlyPaymentRate
        monthlyPaymentRate = round((upperbound+lowerbound)/2,2)
    else:
        upperbound = monthlyPaymentRate
        monthlyPaymentRate = round((upperbound+lowerbound)/2,2)
    
    if abs(rate)<=.01:
        break
    
print(monthlyPaymentRate)