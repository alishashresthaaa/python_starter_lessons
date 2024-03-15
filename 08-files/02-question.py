# Comma seperated value: CSV
# First line is always a header
csv_file = open("data.txt", "a")
csv_file.write("Name, ID\n")
csv_file.write("Alizera, 6655\n")
csv_file.write("Alex, 1231\n")
csv_file.close()