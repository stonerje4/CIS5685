###James Stoner
###PA4
###2/26/2023


user_input = int(input("Enter a int value of 1-5 here to select your data:"))

result = []

f = open("python homework\PA4\moxy.csv", 'r')
next(f)
file = f.readlines()

output_file = open("python homework\PA4\output.csv", "w")

for line in file:
    line = line.strip()
    values = line.split(',')
    if user_input == int(values[3]) and user_input < float(values[2]):
        print(line)
        output_file.write(line + "\n")

f.close()

