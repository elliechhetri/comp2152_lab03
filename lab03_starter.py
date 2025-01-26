# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

#ToDo Use list() and range() to create a list of dice values ([1, 2, 3, 4, 5, 6]) instead of the current hard-coded dice values
diceOptions = list(range(1, 7))
print (diceOptions)

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"] 
        
#Use a for loop with the in keyword to iterate over the weapons array and display the available weapons to the player.
print("Available weapons: ")
i=1
for w in weapons:
    print(f"{i}. {w}") 
    i += 1
    
#Player Input Validation
#combatStrength = int(input("Enter your combat Strength: (Number between 1-6) "))
combatStrength = input("Enter your combat Strength: (Number between 1-6) ")
isValueNumeric = combatStrength.isnumeric() and int(combatStrength) >= 1 and int(combatStrength) <= 6

while not isValueNumeric:
    print("Input must be an integer between 1-6")
    combatStrength = input("Enter your combat Strength: (Number between 1-6) ")
    isValueNumeric = combatStrength.isnumeric() and int(combatStrength) >= 1 and int(combatStrength) <= 6

combatStrength = int(combatStrength)

#monsters combat strength

mcombatStrength = input("Enter your monster's combat Strength: (Number between 1-6) ")
isValueNumeric = mcombatStrength.isnumeric() and int(mcombatStrength) >= 1 and int(mcombatStrength) <= 6

while not isValueNumeric:
    print("Input must be an integer between 1-6")
    mcombatStrength = input("Enter your mcombat Strength: (Number between 1-6) ")
    isValueNumeric = mcombatStrength.isnumeric() and int(mcombatStrength) >= 1 and int(mcombatStrength) <= 6

mcombatStrength = int(mcombatStrength)


# Main Game Loop
        
input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

# Roll the dice (1-6) to choose which weapon you must use. Save the roll in a variable called weaponRoll.
weaponRoll = random.choice(diceOptions)  # Roll a dice (1-6)
    
# Add your weaponRoll to the hero's combat strength
combatStrength += weaponRoll

# Use this variable as an index into the weapons array and print out the name of the hero's weapon.
print("The name of the hero's weapon is: " + weapons[weaponRoll])

# if weaponRoll is less than or equal to 2, print out "You rolled a weak weapon, friend".
if (weaponRoll <= 2):
    print("You rolled a weak weapon, friend")
# But if weaponRoll is less than or equal to 4, print out "Your weapon is meh"
elif (weaponRoll <= 4):
    print("Your weapon is meh")
# Else, print out "Nice weapon, friend! "
else:
    print("Nice weapon, friend! ")

# If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
if (weapons[weaponRoll-1] != "Fist"):
    print("Thank goodness you didn't roll the Fist...")

input("Analyze the roll (Press enter)")
# Equality operators
print("--- You are matched in strength: " + str(combatStrength == mcombatStrength))

# Relational operators
print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

# and keyword
print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

# not keyword
print("--- Phew, you have a healing potion: " + str(
    not (                               # monster will NOT kill hero in one blow
        healthPoints < mcombatStrength  # monster will kill hero in one blow
    )
    and
    healingPotion == 1                  # hero has a healing potion
))

# or keyword
print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

# in keyword
print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# --- Expanded if statement
if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")


# --- Nested if statement
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print("Your sword (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength
    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print("Monster's Claw (" + str(mcombatStrength) + ") ---> You (" + str(healthPoints) + ")")

    #  Ensure healthPoints is handled correctly
    if mcombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mcombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))

# --- Battle Sequence
print("\n--- BATTLE SEQUENCE ---")
for x in range(1, 20, 2):  # Loop from 1 to 20, stepping by 2 (10 rounds)
    print(f"\n--- Round {x} ---")

    # Break condition
    if x == 11:
        print("Sudden Battle Truce! The battle ends.")
        break

    # Roll dice for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Announce selected weapons (with validation)
    if 1 <= heroRoll <= 6:
        print(f"Hero rolled: {heroRoll} - Weapon: {weapons[heroRoll - 1]}")
    else:
        print(f"Hero rolled an invalid value: {heroRoll}")

    if 1 <= monsterRoll <= 6:
        print(f"Monster rolled: {monsterRoll} - Weapon: {weapons[monsterRoll - 1]}")
    else:
        print(f"Monster rolled an invalid value: {monsterRoll}")

    # Add dice roll to combat strengths
    heroStrength = combatStrength + heroRoll
    monsterStrength = mcombatStrength + monsterRoll

    # Print total strengths
    print(f"Hero Total Strength: {heroStrength}, Monster Total Strength: {monsterStrength}.")

    # Determine the winner
    if heroStrength > monsterStrength:
        print("Hero wins the round!")
    elif monsterStrength > heroStrength:
        print("Monster wins the round!")
    else:
        print("It's a draw!")