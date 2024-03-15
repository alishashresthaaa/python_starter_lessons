# Writing to a file,
output_file = open("db.txt", "w") #Replaces the content everytime
output_file = open("db.txt", "a") #Appends the content when write is called multiple times
output_file.write("The is week six\n")
output_file.write("We are learning file operations")
output_file.close()