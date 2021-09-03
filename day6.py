def collatz(number):
    
    while number > 1:

        if(number == 1):
            break
        
        if(number % 2 == 0):
            number = number // 2
            print (number)
            

        elif(number % 2 == 1):
            number = 3 * number + 1
            print (number)
  
try:   
    print("==========COLLATZ SEQUENCE.============")
    my_number = int(input("Enter a number: \n"))
    my_function = collatz(my_number)
    print(my_function)

except ValueError:
        print("Invalid Value")    

