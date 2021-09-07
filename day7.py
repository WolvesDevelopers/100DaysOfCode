my_list = [1,3,5,7,9]

number_tag = 9

for i, number in enumerate(my_list[:-1]):
    test = number_tag - number
    if test in my_list[i+1:]:
        print(f"solution : {number} and {test}")
        break
    else:
        print("No solution")
  

    
