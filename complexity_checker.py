import os
clear = lambda: os.system('cls')

with open("password_wordlist.txt", 'r', encoding='latin-1') as file:
    password_list = [line.strip() for line in file.readlines()]


#This function checks the strength of passwords and return it with additional feedback
def check_strength(password):
    isUpper = False
    isLower = False
    isSpecialSymbol = False
    isNumber = False
    strength = "Weak"
    feedback = ""
    LenPass = len(password)
    
    #checks the wordlist of password if it exist there
    if password in password_list:
        strength = "Very Weak"
        feedback = "\nPassword exist in a breached password list, Never use this Password!!\n"
        return strength, feedback
    
    for letter in password:
        if letter >= "A" and letter <= "Z":
            isUpper = True
        elif letter >= "a" and letter <= "z":
            isLower = True
        elif letter >= "1" and letter <="9":
            isNumber = True
        else:
            isSpecialSymbol = True

    
    #if password is empty
    if LenPass == 0:
        strength = "Very Weak"
        feedback = "Please Enter a Password"
        return strength, feedback
    
    
    if isUpper and isLower and not isNumber and not isSpecialSymbol: # if Upper and Lower letters combination
        feedback = "\nUpper and Lower letters: \n1. Increase length to atleast 12\n2. Add Special Characters\n3. Add Numbers\n"
        if LenPass <= 8:
            strength = "Very Weak"          
        elif LenPass == 9:
            strength = "Weak"
        elif LenPass > 9 and LenPass <= 11:
            strength = "Good"
        else:
            strength = "Strong"
            feedback = "\nUpper and Lower letters: \n1. Your Password is Secure\n2. Add Special Characters\n3. Add Numbers\n"
    elif isUpper and isLower and isNumber and not isSpecialSymbol: # if Numbers, Upper, and Lowercase letters combination
        feedback = "\nNumbers, Upper, and Lowercase letters: \n1. Increase length to atleast 12\n2. Add Special Symbols\n"
        if LenPass <= 7:
            strength = "Very Weak"
        elif LenPass > 7 and LenPass <= 9:
            strength = "Weak"
        elif LenPass > 9 and LenPass <= 11:
            strength = "Good"
        else:
            strength = "Strong"
            feedback = "\nNumbers, Upper, and Lowercase letters: \n1. Your Password is Secure\n2. Add Special Character\n"
    elif isUpper and isLower and isNumber and isSpecialSymbol: # if Numbers, Upper, Lowercase letters, Symbols combination
        feedback = "\nNumbers, Upper, Lowercase letters, Symbols: \n1. Increase length to atleast 11\n"
        if LenPass <= 7:
            strength = "Very Weak"
        elif LenPass > 7 and LenPass <= 9:
            strength = "Weak"
        elif LenPass == 10:
            strength = "Good"
        else:
            strength = "Strong"
            feedback = "\nNumbers, Upper, Lowercase letters, Symbols: \n1. Your Password is Secure\n"
    elif not isUpper and not isLower and isNumber and not isSpecialSymbol: # if Number only Password
        feedback = "\nNumber only Password: \n1. Increase length to atleast 20\n2. Add upper and lowercase letter\n3. Add Special Symbols\n"
        
        if LenPass <= 14:
            strength = "Very Weak"
        elif LenPass >= 15 and LenPass <= 17:
            strength = "weak"
        elif LenPass >= 18 and LenPass <= 20:
            strength = "Good"
        else:
            strength = "Strong"
            feedback = "\nNumber only Password: \n1. Your Password is Secure\n2. Add upper and lowercase letter\n3. Add Special Symbols\n"
    elif isUpper and not isLower and not isNumber and not isSpecialSymbol: # if Uppercase Only Password
        feedback = "\nUppercase Only Password: \n1. Increase Length to atleast 15\n2. Add Lowercase Characters\n3. Add Numbers\n4. Add Special Characters\n"
        if LenPass <= 10:
            strength = "Very Weak"
        elif LenPass > 10 and LenPass <= 12:
            strength = "Weak"
        elif LenPass > 12 and LenPass <= 14:
            strength = "Good"
        else:
            strength = "Strong"
            feedback = "\nUppercase Only Password: \n1. Your Password is Secure\n2. Add Lowercase characters\n3. Add Special Symbols\n4. Add Numbers\n"
    elif not isUpper and isLower and not isNumber and not isSpecialSymbol: # if Lowercase Only Password
        feedback = "\nLowercase Only Password: \n1. Increase Length to atleast 15\n2. Add Uppercase Characters\n3. Add Numbers\n4. Add Special Characters\n"
        if LenPass <= 10:
            strength = "Very Weak"
        elif LenPass > 10 and LenPass <= 12:
            strength = "Weak"
        elif LenPass > 12 and LenPass <= 14:
            strength = "Good"
        else:
            strength = "Strong"
            feedback = "\nNumber only Password: \n1. Your Password is Secure\n2. Add uppercase characters\n3. Add Special Symbols\n4. Add Numbers\n"
    else: # if random combination of Numbers, Upper, Lowercase letters, Symbols
        feedback = "\n1. Increase length to atleast 11\n"
        if LenPass <= 7:
            strength = "Very Weak"
        elif LenPass > 7 and LenPass <= 9:
            strength = "Weak"
        elif LenPass == 10:
            strength = "Good"
        else:
            strength = "Strong"
            feedback = "\n1. Your Password is Secure\n"
        
            
    return strength, feedback


def main():
    status = "weak"
    feedback = "Enter A password"
    password = ""
    while True:  
        print("Strength: " + status)
        print("Feedback: " + feedback)
        password = input("Password: ")
        status, feedback = check_strength(password)
        clear()


if __name__ == "__main__":
    main()