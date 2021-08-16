#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


print("Welcome to the tip Calculator")
total_bill = float(input("What was the total bill? "))
percen_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill? "))
tip = percen_tip/100

total_bill_tip = total_bill*tip
result = (total_bill+total_bill_tip)/person
final_amount = round(result,2)

#alternative version
# tip = (percen_tip / 100) + 1
# result = (total_bill/person)*tip
# final_amount = round(result,2)

print(f"Each person should pay : {final_amount}")

