# passwordComplexityCheck
Checks the complexity of a password based on if the password is 12 characters long, number(s), and special character(s)

**Variables** will show like this to show what the variables in the functions are

Functions 
- Main
    This function takes the input from the user of the password that is going to be checked and passes it to the passwordCheck function which will return a dictionary of all the fixes that the password will need then finally giving the analysis of the password strength/complexity
  
    **password** - The password inputted from the user
    **complexity** - The returned dictionary from running the passwordCheck function
    **x** - The amount of test the password has passed
    
- passwordCheck
      This function takes the inputted password and runs it through all the test methods to check if the password is secure. It stores the passed/failed test result as a boolean for the variables length, numbers, and special_character. This method stores the failed results as a dictionary and info for what to add to the password then finally passes it back to the main method to report the information to the user.
    **length** - Value of passed test for length
    **numbers** - Value of passed test for numbers
    **special_Character** - Value of passed test for special characters
    **passDict** - Dictionary that stores all the fixes that are needed for the password
    **addDictionary** - A tuple created to hold the boolean values for the test to pass to the sum() function


- passwordHasNumber
      This function checks if the password has a number in it
  
- hasSpecialCharacter
      This function checks if the password uses a special character
  
- passwordErrors
      This function prints all the errors that the password has stored from the dictionary

  
- proble
