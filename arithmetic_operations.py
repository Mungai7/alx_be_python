def perform_operation (num1 :float,num2 :float, operation :str):

    if operation == "+":
        return (num1 + num2)
    
    elif operation == "-":
        return (num1-num2)
    
    elif operation == "/":
         if num2 == 0 : 
          raise ValueError("Can not divide by zero")
         return (num1/num2) 
    
    elif operation == "*":
        return (num1*num2)
    
    else:
        raise ValueError ("Unsupported operation use","+","-","/","*")
print (perform_operation (10,0,"/"))
 
