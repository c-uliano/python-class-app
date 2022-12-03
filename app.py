"""
SPECS

Handle the actions of a game character

character traits:
    // Name
    // Power Points
    // Can teleport

needs to perform actions:

    run
        //- costs 1 power point
        //- Print message if running
        //- print message contining number of points if not enough points

    rest
        //- gain 1 power point
        //- Print messasge if resting
        //- print plenty of points message if no rest is necessary

    teleport 
        //- costs 2 power points
        //- print name is teleporting
        //- print message if not enough power points
        //- print message if unable to teleport

    invalid actions
        //- print 'Invalid Action'

! considerations:
    ! player can only have 0 to 10 power points.
"""

"""
SPECS
    // iterate through a list of characters - build a list of objects, one for each character. 
        // Use for loop
    // isolate the action functionality into a function
    // randomly select action
"""

# ? action functionality into a function
# just moved everything into this function
# ! this stuff was already written out from the first go-around when there was just one character. It never would have occured to me to make this a separate function instead of just adding all this action code into the character for loop
# ! does this have to be before the for loop because it needs to be above where it's called?
def characterAction(action, character):
    name, power_points, can_teleport = character.values()
    if action == 'run':
        if power_points > 0:
            power_points -= 1
            print ( f'{name} is running' )
        else:
            print ( 'not enough power points to run')
    elif action == 'rest':
        if power_points < 10:
            print( f'{name} is resting' )
            power_points += 1
        else:
            print( 'no rest needed' )
    elif action == "teleport":
        if can_teleport:
            if power_points >= 2:
                power_points -= 2
                print(f"{name} is teleporting")
            else:
                print("not enough powerpoints")
        else:
            print('unable to teleport')
    else:
        print ( "Invalid Command" )

# ? all the characters into a list (array), each element of the list a dictionary (object) for each character
characters = [
    {
        "name": 'FuzzBall',
        "power_points": 1, # minimum = 0, maximum = 10
        "can_teleport" : True 
    },
    {
        "name": 'River',
        "power_points": 8 ,# minimum = 0, maximum = 10
        "can_teleport": False 
    }
]


# ? randomly select an action
import random

# ? iterate through. So for each character (for each index) in the characters list it will print all their details
for character in characters:
    # ? destructuring each dictionary (object) so each key is a variable with it's value
    # ! if it's destructuring the dictionary then why is it character.values() and not characters.value()?
    # ! is it because it's destructuring each separate dictionary (object)? characters is a list (array), each element in the list is the dictionary
    name, power_points, can_teleport = character.values()

    print ( f'{name} has {power_points} Power Points and {"can" if can_teleport else "cannot"} teleport' )

    # update this to a list of all actions
    actions = [
        'teleport',
        'rest',
        'run'
    ]
    # ? pick a random action
    action = random.choice(actions)

    characterAction(action, character)







"""
SPECS
    // Create a collection of items the character can carry
    // Add an 'inventory' action that displays all the items in inventory
"""

# items = [
#     'sword',
#     'shield',
#     'potion'
# ]

# for i in range(len(items)):
#     print(items[i])

