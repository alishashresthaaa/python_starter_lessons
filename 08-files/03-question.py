# Reading a file
input_file = open("data.txt", "r")
# print(input_file.readline(1))
# print(input_file.readlines())

csv_reader = csv.reader(input_file)
print(next(csv_reader))

for row in csv_reader:
    print(row)

for row in csv_reader:
    print(row[0], "-", row[1])

# If file does not exist when reading the file
try:
    input_file = open("dta.txt", "r")
except:
    print("The file does not exists")
