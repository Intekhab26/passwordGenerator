import random
import string

string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '~!@#$%^&*()'

def userInput():
    length = int(input("Enter the length of the password: "))
    Use_SpecialChars = input("Include special characters?(yes/no):").lower() == 'yes'
    use_numbers = input("Include numbers?(yes/no): ").lower() == 'yes'
    return(length, Use_SpecialChars, use_numbers)

def generate_password(length, Use_SpecialChars, use_numbers):
    """Generates a random password based on user preferences."""
    if (length < (Use_SpecialChars + use_numbers)):
        return "Password length too short for given options."
    characters = string_char

    if (use_numbers):
        characters += string_num
    if (Use_SpecialChars):
        characters += string_special
    password = ''.join(random.choice(characters) for _ in range(length))
    
    if (use_numbers):
        password = password[:-2] + random.choice(string_num) + password[-1]

    if (Use_SpecialChars):
        password = password[:-1] + random.choice(string_special)

    return password



if __name__ == '__main__':
    length, Use_SpecialChars, use_numbers = userInput()
    generated_password = generate_password(length, Use_SpecialChars, use_numbers)
    print("\nGenerated Password:", generated_password)