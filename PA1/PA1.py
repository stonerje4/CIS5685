initial_organism = int(input("Enter the initial number of organisms:"))
growth_rate = int(input("Enter the rate of growth (a real number > 1):"))
growth_time = int(input("Enter the number of hours to achieve the rate of growth:"))
totalhours_growth = int(input("Enter the total hours of growth:"))


population = initial_organism
for i in range(totalhours_growth//growth_time):
    population = population * growth_rate

print("The total population is", population)
