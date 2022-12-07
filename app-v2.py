"""
SPECS

Handle the actions of a game character

character traits:
    Name
    Power Points
    Can teleport

needs to perform actions:

    run
        - costs 1 power point
        - Print message if running
        - print message contining number of points if not enough points

    rest
        - gain 1 power point
        - Print messasge if resting
        - print plenty of points message if no rest is necessary

    teleport 
        - costs 2 power points
        - print name is teleporting
        - print message if not enough power points
        - print message if unable to teleport

    invalid actions
        - print 'Invalid Action'

! considerations:
    ! player can only have 0 to 10 power points.
"""