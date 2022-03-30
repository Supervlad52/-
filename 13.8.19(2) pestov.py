number_of_tickets = int(input("Enter the number of tickets: "))
price_tickets = 0

for i in range(number_of_tickets):
    age = int(input("Enter your age: "))
    i += 1
    if age < 18:
        print("Free!")
    elif 18 <= age < 25:
        price_tickets += 990
        print('The ticket costs 990 rubles')
    else:
        price_tickets += 1390
        print("The ticket costs 1390 rubles")
if number_of_tickets > 3:
    price_tickets = price_tickets*0.9
    print("The cost of tickets with a discount of 10%: ", price_tickets)
else:
    print("Total money", price_tickets)
