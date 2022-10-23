# ask for age
age = input("How old are you? : ")
if age:
    # 18-21 then give them wristband to identify them and not give alcohol
    # You can use for if statement "not age" also "age !=" both give the same result.
    # Removed "not" and it works too because for empty input else statement is written.
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter but you need a wristband!")

    # 21+ give normal entry without wristband

    elif age > 21:
        print("You are good to enter and drink alcohol!")

    # under 18 don't give them entry

    elif not (age >= 18 and age <= 21):
        print("You are too young, where are your parents?")

else:  # If there is no input
    print("Please enter age otherwise I cannot allow you to enter!")
