import matplotlib.pyplot as plt
#sudo apt-get install python3-tk
#pip install matplotlib

print("\n\n*****INCOME*****")
salary = int(input("Salary/wage : "))
other_income = int(input("Other income: "))
TOTAL = float(salary + other_income)

print("\n\n*****EXPENSES*****")

print("\nHOUSING EXPENSES")
mortgage = int(input("Mortgage : "))
house_insurance = int(input("Insurance : "))
bills = int(input("Water/Electricity/gas : "))
cable = int(input("Cable : "))
maintenance = int(input("Maintenance :"))
HOUSING = float(mortgage + house_insurance + bills + cable + maintenance)
housing_percentage = float(HOUSING / TOTAL)*100
print("HOUSING EXPENSES ", HOUSING)



print("\nTRANSPORT EXPENSES")
car_loan = int(input("monthly car loan : "))
car_insurance = int(input("Car insurance : "))
fuel = int(input("Fuel : "))
repairs = int(input("Car maintenance : "))
TRANSPORT = float(car_loan + car_insurance + fuel + repairs)
transport_percentage = float(TRANSPORT / TOTAL) * 100
print ("TRANSPORT EXPENSES ", TRANSPORT)

print("\nEDUCATIONAL EXPENSES")
supplies = int(input("Educational supplies : "))
eduactional_loans = int(input("Eduactional loans : "))
tuition = int(input("Tuition fees :"))
EDUCATION = float(supplies +  eduactional_loans + tuition)
educationaL_percentage = float(EDUCATION / TOTAL) * 100
print ("EDUCATION EXPENSES ", EDUCATION)

print("\nPERSONAL EXPENSES")
food = int(input("Monthly food expenses : "))
clothing = int(input("Clothing expenses : "))
entertainment = int(input("Entertainment expenses : "))
medical = int(input("Medical expenses : "))
PERSONAL = float(food + clothing + entertainment + medical)
personal_percentage = float(PERSONAL / TOTAL) * 100
print ("PERSONAL EXPENSES ", PERSONAL)


print("\n\n*****SAVINGS*****")

print("\nSAVINGSS")
emergency = int(input("Emergency funds : "))
investments = int(input("Investments : "))
retirement = int(input("Retirement funds :"))
SAVINGS = float(emergency + investments + retirement)
savings_percentage = float(SAVINGS / TOTAL) * 100
print ("SAVINGS EXPENSES ", SAVINGS)


print("\n\n")
print("HOUSING PERCENTAGE ", housing_percentage)
print("TRANSPORT PERCENTAGE ", transport_percentage)
print("EDUCATION PERCENTAGE ", educationaL_percentage)
print("PERSONAL PERCENTAGE ", personal_percentage)
print("SAVINGS PERCENTAGE ", savings_percentage)
HEADROOM = 100 - (housing_percentage+transport_percentage+educationaL_percentage+personal_percentage+savings_percentage)

labels = 'HOUSING', 'TRANSPORT', 'EDUCATION', 'PERSONAL', 'SAVINGS','HEADROOM'
sizes = [housing_percentage, transport_percentage, educationaL_percentage
, personal_percentage, savings_percentage, HEADROOM]
if(HEADROOM > 10):
	colors = ['azure', 'cyan', 'fuchsia', 'floralwhite', 'powderblue', 'mintcream']
else:
	colors = ['azure', 'cyan', 'fuchsia', 'floralwhite', 'powderblue', 'firebrick']
#explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=0)

plt.axis('equal')
plt.show()
