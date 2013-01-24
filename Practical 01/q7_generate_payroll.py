# Filename: q7_generate_payroll.py
# Author: Chia Xiang Rong
# Date created: 22/1/2013
# Date modified: 22/1/2013
# Description: Generate a payroll statement from information provided

#Get information
name = str(input("Enter name: "))
worktime = int(input("Enter number of hours worked weekly: "))
payrate = float(input("Enter hourly pay rate ($): "))
cpfrate = float(input("Enter CPF contribution rate(%): "))

#Compute Gross Pay, Net Pay, CPF contribution
grosspay = payrate * worktime
cpfcon = grosspay * (cpfrate / 100)
netpay = grosspay - cpfcon

#Generate payroll
print ("""
Payroll statement for """ + name)
print ("Number of hours worked in week: {0}".format(worktime))
print ("Hourly pay rate: ${0:.2f}".format(payrate))
print ("Gross pay = {0:.2f}".format(grosspay))
print ("CPF contribution at {0}".format(cpfrate) + "% = {0:.2f}".format(cpfcon))
print ("""
Net pay = ${0:.2f}""".format(netpay))
