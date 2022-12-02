"""
SPECS

Handle the actions of a game character

character traits:
    Name
    Power Points
    Can teleport

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

considerations:
    player can only have 0 to 10 power points.
"""

# update this stuff to be a list of character objects
name = 'FuzzBall'
power_points = 1 # minimum = 0, maximum = 10
can_teleport = True 

print ( f'{name} has {power_points} Power Points and {"can" if can_teleport else "cannot"} teleport' )

action = 'teleport' # run, rest, teleport 

if action == 'run':
    if power_points > 0:
        power_points -= 1
        print ( f'{name} is running' )
    else:
        print ( 'not enough power points to run')
elif action == 'rest':
    if power_points < 10:
        print( 'resting' )
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

print ( power_points )

"""
SPECS
    // Create a collection of items the character can carry
    // Add an 'inventory' action that displays all the items in inventory
"""

items = [
    'sword',
    'shield',
    'potion'
]

for i in range(len(items)):
    print(items[i])

"""
SPECS
    iterate through a list of characters - build a list of objects, one for each character, update above. Use for loop
    isolate the action functionality into a function
    randomly select action
"""