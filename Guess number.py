import random 
def gen_code():
    set_code = [] 	
    for i in range(4):
        val = random.randint(0, 9)
        set_code.append(val)
    return set_code 	
# asks for input from the user 
def input_code():
    code = input("Enter your four digit guess code: ")
    return code  
def guessthenumber():
    genCode = gen_code()
    i = 0
    while i < 10:
        result = ""
        inputCode = [int(c) for c in input_code()]
        if len(inputCode) != 4:
            print("Enter only 4 digit number")
            continue
        if inputCode == genCode:
            print("You guessed it !", genCode)
            break
        for element in inputCode:
            if element in genCode:
                if inputCode.index(element) == genCode.index(element):
                    result+="R"
                else:
                    result+="Y"
            else:
                result+="B"
        print(result)
        i += 1
    else:
            print("You ran out of trys !", genCode)	 
		
print(" Guess the code in 10 tries or less\n If any guessed digit code is wrong then print ""--> B "" \n If the digit is correct but at the wrong place, the computer should print "" -->Y ""\n If both digit and position is correct, the computer should print  ""--> R "" \n")	     
guessthenumber() 
