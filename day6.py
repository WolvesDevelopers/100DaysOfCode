def collatz(number):

    while number > 1:

        if(number == 1):
            break

        if(number % 2 == 0):
            number = number // 2
            print(number)

        elif(number % 2 == 1):
            number = 3 * number + 1
            print(number)


acces = True

while acces:
    try:
        print("==========COLLATZ SEQUENCE.============")
        my_number = int(input("Enter a number: \n"))
        collatz(my_number)
        prompt = "Do you want to repeat the operation?"
        prompt += "\nPress Yes to continue or No to exit: "
        question = input(prompt).title()

        if question == 'No':
            break
        elif question == 'Yes':
            continue

    except ValueError:
        print("Invalid Value")
