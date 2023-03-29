#Jesse Stoner
#Homework 2
#2/15/2023
#CIS5685-101



initial_organisms = int(input("Enter the initial number of organisms:"))
growth_rate = int(input("Enter the rate of growth (a real number > 1):"))
hours_to_achieve = int(input("Enter the number of hours to achieve the rate of growth:"))
total_hours = int(input("Enter the total hours of growth:"))

population = initial_organisms

list(range(total_hours//hours_to_achieve))

for i in range(total_hours//hours_to_achieve):
    population = population * growth_rate

print(population)












































