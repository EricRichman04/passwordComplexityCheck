import string

#A function that checks the complexity/strength of a password
def passwordCheck(password):
    length = False
    numbers = False
    special_Character = False
    
    passDict = {}

    if len(password) < 12:
        passDict["length"] = "Password is too short, please try to make the password at least 12 characters long"
    else:
        length = True
    
    if passwordHasNumber(password) == 0:
        passDict["numbers"] = "Password does not contain a number or is only numbers. A password should try to contain at least 1 number but not only numbers"
    else:
        numbers = True

    if hasSpecialCharacter(password) == 0:
        passDict['special'] = "Password does not contain a special character"
    else:
        special_Character = True

    addDictionary = (length, numbers, special_Character)
    passDict["complexity"] = sum(addDictionary)
    return passDict

# A function to check if the password has a number in it and returns 0 if the password does not have a number or only has numbers and
# returns a 1 if the password has a number in it with non numeric characters
def passwordHasNumber(password):
    count = 0
    for i in password:
        x = i.isnumeric()
        if x:
            return 1
    return 0

#A function to check if the password has a special character in it and returns a 1 if the password contains a special character and a 0
# if no special character is found
def hasSpecialCharacter(password):
    specialCharacters = string.punctuation
    for i in password: 
        if i in specialCharacters:
            return 1
    return 0

def passwordErrors(dict):
    for x in dict:
        print(dict[x])

#Main function which accepts the password as input
def main():
    password = input("What is the password that you want to check? ")
    complexity = passwordCheck(password)
    x = complexity["complexity"]
    if (x == 0 or x == 1):
        passwordErrors(complexity)
        print("Your password is very insecure due to the listed reasons, please create a stronger password")
    elif x == 2:
        passwordErrors(complexity)
        print("Your password is slightly good, it can use some extra complexity but it otherwise is okay to use")
    else:
        print("Your password passed the complexity check, It is quite strong!")


if __name__ == '__main__':
    main()