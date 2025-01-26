combatStrength = input("Enter your combat Strength: (Number between 1-6) ")
isValueNumeric = combatStrength.isnumeric() and int(combatStrength) >= 1 and int(combatStrength) <= 6
while not isValueNumeric:
    print("Input must be an integer between 1-6")
    combatStrength = input("Enter your combat Strength: (Number between 1-6) ")
    isValid = combatStrength.isnumeric() and int(combatStrength) >= 1 and int(combatStrength) <= 6
combatStrength = int(combatStrength)