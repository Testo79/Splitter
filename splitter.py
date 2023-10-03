# Initialize empty lists to store usernames and passwords
usernames = []
passwords = []

# Open the file containing the credentials
with open('credentials.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Split the line into username and password using ":" as the separator
        parts = line.strip().split(':')
        if len(parts) == 2:
            username, password = parts[0], parts[1]
            # Append the username and password to their respective lists
            usernames.append(username)
            passwords.append(password)

# Write the lists of usernames and passwords to separate text files
with open('usernames.txt', 'w') as usernames_file:
    for username in usernames:
        usernames_file.write(username + '\n')

with open('passwords.txt', 'w') as passwords_file:
    for password in passwords:
        passwords_file.write(password + '\n')
