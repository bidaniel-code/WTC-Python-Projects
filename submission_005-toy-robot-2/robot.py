step = [0,0,0]


def name_robot():
    """get the user to input a name for the robot and then
       say hello to the user as the now named robot"""

    name = input("What do you want to name your robot? ").upper()
    print(name + ": Hello kiddo!")    
    return name 

def take_command(robo_name):
    """gets the user to input what they want the robot to do(command)"""

    command = input(robo_name + ": What must I do next? ")  
    valid_commands(command, robo_name)


def valid_commands(command, robo_name):
    """thakes the users command from (take_command) and checks if it is a
       valid command. If valid it runs that commands function, else it
       prints that it did not understand the command and returns to
       take_command"""

    if command.upper() == 'HELP':
        help_command(robo_name)
    elif command.upper() == 'OFF':    
        off_command(robo_name)
    elif command[:7].upper() == 'FORWARD':
        forward_command(command, robo_name)
    elif command[:4].upper() == 'BACK':
        back_command(command, robo_name)
    elif command.upper() == 'RIGHT':
        turn_right_command(robo_name)  
    elif command.upper() == 'LEFT':
        turn_left_command(robo_name)          
    elif command[:6].upper() == 'SPRINT':
        sprint_command(command, robo_name)
    else:
        print(robo_name + ": Sorry, I did not understand '" + command + "'.")
        take_command(robo_name)


def help_command(robo_name):
    """when called this function simply prints out the commands and there 
       discriptions that are valid (what the robot can do)then returns 
       to take_command"""

    print("I can understand these commands:")
    print("OFF  - Shut down robot")
    print("HELP - provide information about commands")
    print("FORWARD - Moves the robot forward the number of steps you give it")
    print("BACK - Moves the robot backwards the number of steps you give it")
    print("RIGHT - turns the robot 90% to the right")
    print("LEFT - turns the robot 90% to the left")
    print("SPRINT - Move the robot forward x amount of times")
    take_command(robo_name)


def off_command(robo_name):
    """turns OFF(exit) robot"""
    global step 
    step = [0,0,0]
    print(robo_name + ": Shutting down..")


def area_limit(numb):
    """limits the area in which the robot is allowed to move"""

    if step[2] == 90 or step[2] == -90:
        if (step[0] + numb < -100) or (step[0] + numb > 100):
            return False
        else:
            return True    
    elif (step[1] + numb < -200) or (step[1] + numb > 200):
        return False
    else:
        return True


def update_position(numb, robo_name, command):
    """keeps track of the direction(step[2]) in whic the robot is faceing thus 
    incramenting x(step[0]) and y(step[1]) accordingly. It then prints the updated
    position of the robot and returns to take_command"""

    global step
    if step[2] != 0 and step[2] != 90:
        numb = -(numb)
    if step[2] == 0:
        step[1] += numb
    elif step[2] == 90:
        step[0] += numb
    elif step[2] == -90:
        step[0] += numb
    elif step[2] == 180 or step[2] == -180:
        step[1] += numb
    if command != 'SPRINT':
        print(" > " + robo_name + " now at position (" + str(step[0]) + "," + str(step[1])+ ").")


def forward_command(command, robo_name):
    """moves the robot forward based on the number of step the user specifide.
       If the specifide number of steps exceeds the area limit the function
       prints out that the robot cannot move beyond its safe zone, the returns 
       to take_command, aslo returns to take_command if int != int"""

    try:
        numb = int(command[7:])
        if area_limit(numb):
            print(" > " + robo_name + " moved forward by " + str(numb) + " steps.")
            update_position(numb, robo_name, command)
            take_command(robo_name)
        else:
            print(robo_name + ": Sorry, I cannot go outside my safe zone.")
            print(" > " + robo_name + " now at position (" + str(step[0]) + "," + str(step[1])+ ").")
            take_command(robo_name)
    except:
        print(robo_name + ": Sorry, i did not understand " + command)
        take_command(robo_name)
    

def back_command(command, robo_name):
    """moves the robot back based on the number of step the user specifide.
       If the specifide number of steps exceeds the area limit the function
       prints out that the robot cannot move beyond its safe zone, the returns 
       to take_command, aslo returns to take_command if int != int"""
    
    try:
        numb = int(command[4:])
        if area_limit(-numb):
            print(" > " + robo_name + " moved back by " + str(numb) + " steps.")
            update_position(-numb, robo_name, command)
            take_command(robo_name)
        else:
            print(robo_name + ": Sorry, I cannot go outside my safe zone.")
            print(" > " + robo_name + " now at position (" + str(step[0]) + "," + str(step[1])+ ").")    
            take_command(robo_name)
    except:
        print(robo_name + ": Sorry, i did not understand " + command)
        take_command(robo_name)


def turn_right_command(robo_name):
    """turns the robot to the right by 90% at a time based on the direction
       the robot is facing at the time by incrementing or decrementing step[2]
       then prints that the robot has turned right and returns to take_command"""
    
    global step
    if step[2] == 180 or step[2] == -180:
        step[2] = -90
    else:
        step[2] += 90
    print(" > " + robo_name + " turned right.")
    print(" > " + robo_name + " now at position (" + str(step[0]) + "," + str(step[1])+ ").")        
    take_command(robo_name)


def turn_left_command(robo_name):
    """turns the robot to the left by 90% at a time based on the direction
       the robot is facing at the time by incrementing or decrementing step[2]
       then prints that the robot has turned left and returns to take_command"""
    
    global step
    if step[2] == 180 or step[2] == -180:
        step[2] = 90
    else:
        step[2] -= 90
    print(" > " + robo_name + " turned left.")
    print(" > " + robo_name + " now at position (" + str(step[0]) + "," + str(step[1])+ ").")        
    take_command(robo_name)


def sprint_command(command, robo_name):
    """gives a shor burst of speed to the robot and some extra distance
       by using a simple factorial recursiive function """
    try:
        numb = int(command[6:])
        if (numb <= 0):
            print(" > " + robo_name + " now at position (" + str(step[0]) + "," + str(step[1])+ ").")
            take_command(robo_name)

        elif area_limit(numb):
            print(" > " + robo_name + " moved forward by " + str(numb) + " steps.")
            update_position(numb, robo_name, 'SPRINT')
            sprint_command('SPRINT' + str(numb - 1), robo_name)
        else:
            print(robo_name + ": Sorry, I cannot go outside my safe zone.")
            take_command(robo_name)    
    except:
        print(robo_name + ": Sorry, i did not understand " + command)
        take_command(robo_name)
   

def robot_start():
    """This is the entry function, do not change"""
    robo_name = name_robot()
    take_command(robo_name)


if __name__ == "__main__":
    robot_start()
