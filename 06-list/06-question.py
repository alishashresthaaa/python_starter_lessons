# Reversing a string using loops
message = "Today we are learning loops"
for i in range(len(message)-1, -1, -1):
    print(message[i], end="")
