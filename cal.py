# function
def calculatebasicmath(num01 , operator, num02):      
    if operator == "+":
        resu = num01 + num02
    elif operator == "-":
        resu = num01 - num02
    elif operator == "*":
        resu = num01 * num02
    elif operator == "/":     
        resu = num01 / num02
    else:
        resu = "The operator is not valid!"
    
    print(resu)
# call
try: 
    num01 = int(input("Please Enter Number1: "))
    operator = input("Please Enter the operator(+ - * /): ")
    num02 = int(input("Please Enter Number2: "))
except:
    print("Something wrong!")    
else:
    calculatebasicmath(num01, operator, num02)
