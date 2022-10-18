givenKilometer = input("How many Kilometres did you run today?")

miles = float(givenKilometer) / 1.60934

miles = round(miles, 2)

print(f"Wow you ran {givenKilometer} and {miles} miles!")

# round(thing to round, how many decimal points to round to)

#print("How many Kilometres di you run today?")
#kms = input()
#miles = float(kms)/1.60934
#miles = round(miles, 2)
#print(f"Ok you ran {kms} Kms and {miles} Miles")

#Same function in a new way 