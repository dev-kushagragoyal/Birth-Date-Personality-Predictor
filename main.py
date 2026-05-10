# Disclaimer: This program is intended for entertainment purposes only. The results generated are based on simple mathematical calculations and do not represent actual
# psychological analysis, medical advice, or factual personality assessments. Please use this script responsibly and for fun.

import time

a = "Intelligent"
b = "Aggressive""
c = "Beautiful / Handsome"
d = "Simple life liver"

birth_date = int(input("Enter your birth date  : "))
print()
birth_month = int(input("Enter your birth month number : "))
print()
birth_year = int(input("Enter your last 2 digit of birth year : "))
print()

cal_1 = birth_date % 4
cal_2 = birth_month % 4
cal_3 = birth_year % 4

# Birth date
if cal_1 == 1:
    result_1 = a
elif cal_1 == 2:
    result_1 = b
elif cal_1 == 3:
    result_1 = c
elif cal_1 == 4:
    result_1 = d
elif cal_1 == 0:
    result_1 = d

# Birth month
if cal_2 == 1:
    result_2 = a
elif cal_2 == 2:
    result_2 = b
elif cal_2 == 3:
    result_2 = c
elif cal_2 == 4:
    result_2 = d
elif cal_2 == 0:
    result_2 = d

# Birth year
if cal_3 == 1:
    result_3 = a
elif cal_3 == 2:
    result_3 = b
elif cal_3 == 3:
    result_3 = c
elif cal_3 == 4:
    result_3 = d
elif cal_3 == 0:
    result_3 = d

print("Calculating results...")
print()
time.sleep(5)
print("You are : ")
print()
print("1.", result_1)
print()
print("2.", result_2)
print()
print("3.", result_3)
