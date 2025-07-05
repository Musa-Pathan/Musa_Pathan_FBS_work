# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
num_passengers = int(input("Enter the number of passengers: "))
ticket_cost = float(input("Enter cost per ticket: "))

total_amount = 0  # To store the total amount to be paid

for i in range(1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    if age < 12:
        discount = 0.30  # 30% discount
    elif age > 59:
        discount = 0.50  # 50% discount
    else:
        discount = 0.0   # No discount

    passenger_cost = ticket_cost * (1 - discount)
    print(f"  Ticket cost for passenger {i} = ₹{passenger_cost:.2f}")

    total_amount += passenger_cost

print(f"\nTotal ticket amount to be paid for all passengers: ₹{total_amount:.2f}")
