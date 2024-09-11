num1 = 5
num2 = 7
adds = num1 + num2
print("The sum is:", adds)
mark1 = 18
mark2 = 20
mark3 = 15
final_mark = mark1 + mark2 + mark3
if final_mark >= 50:
    print(f"Final mark is {final_mark}. You passed!")
else:
    print(f"Final mark is {final_mark}. You failed.")
num1 = 9
num2 = 14
if num1 > num2:
    print(f"The largest number is {num1}")
else:
    print(f"The largest number is {num2}")  
for i in range(1, 11):
    print(f"{i}. Welcome to DCS")  
tickets = 15
if tickets > 25:
    print("You cannot buy more than 25 tickets in a single transaction.")
else:
    price_per_ticket = 20
    total_cost = tickets * price_per_ticket
    if tickets >= 20:
        total_cost *= 0.8  
    elif tickets >= 10:
        total_cost *= 0.9  
    print("The total cost is:", total_cost)  
num1 = 4
num2 = 5
result = num1 * num2 * 3
print("The result of multiplying the numbers three times is:", result)  
mark = 80
if mark >= 75:
    print("The student received a credit mark.")  
else:
    print("The student did not receive a credit mark.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = sum(int(i) for i in numbers)
print("The total of the ten numbers is:", total)  
bill = 300
diners = 6
if 10 <= bill <= 500 and 1 <= diners <= 12:
    split_amount = bill / diners
    print(f"Each person needs to pay: ${split_amount:.2f}")  
else:
    print("Invalid input. Please ensure the bill is between $10 and $500, and diners are up to 12.")
bill_amount = 250
if bill_amount > 200:
    print("The bill is greater than 200 USD. You will pay using a credit card.")  
else:
    print("The bill is less than or equal to 200 USD. You will pay using cash.")
