import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters to create the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            # User input for the password length
            length = int(input("\nEnter the desired length for the password: "))
            if length < 8:  # We recommend a minimum length of 8 for security reasons
                print("For better security, it's recommended to choose a password length of at least 8 characters.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print(f"\nYour generated password is: {password}")

        # Ask if the user wants to generate another password
        repeat = input("\nDo you want to generate another password? (y/n): ").lower()
        if repeat != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
