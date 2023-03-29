###James Stoner
###PA3
###2/26/2023


f = open("python homework\PA3\data.txt", 'r')
file = f.readlines()

total = 0
missing = 0 

total_lines = len(file)
min = float('inf')
max = float('-inf')

for line in file:
    line = line.strip()
    if line == '-1':
        missing += 1
        line = (int(line)+ 1)
    number = float(line)
    total += number
    if number < min and number != 0:
        min = number
    if number > max:
        max = number
    
total_lines = total_lines - missing

print("There are", missing, "missing files")
print("The sum is", round(total, 2))
print("The mean is", round(total/total_lines, 2))
print("The min value is", min)
print("The max value is", max)

f.close()
