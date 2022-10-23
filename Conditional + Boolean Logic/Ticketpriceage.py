print("What's your age?")

age = int(input())
# for ages 2-8 ticket price is 3 dollars
# for ages 65+ the ticket is 7 dollars
# for in between ages the ticket is 10 dollars


if age == 1:
    print("FREE FOR BABIES BUT YOU CAN GET KICKED OUT IF YOU CRY!")
elif not ((age >= 2 and age <=8) or age >= 65):
    print("You are an adult pay 8 dollars for the ticket")
elif age >= 2 and age <= 8:
    print("For children ticket price is '3 dollars'")
else:
    print("Ticket price for old people is 10 dollars, we don't like senior citizens!")
