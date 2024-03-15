# Question 2: File I/O (20 Points)
# Scenario: You are developing a Python script that needs to log messages to a file named "log.txt". Write a Python script that:
# •	Opens (or creates if it doesn't exist) a file named "log.txt" for appending.
# •	Asks the user to enter a log message.
# •	Writes the user's message to the file with a timestamp (e.g., "2023-03-15 12:00:00 - User's message").
# •	Ensures that the file is properly closed after the message is written.
# •	Bonus: Implement error handling for file operations.

from datetime import  datetime
def log_user_message(message):
    try:
        output_file = open("message.txt", "a")
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_file.write(f"{time_stamp} - {message}\n")
        output_file.close()

    except Exception as e:
        print(f"An unexpected error occurred.", e)

message = input("Enter your message: ")
log_user_message(message)