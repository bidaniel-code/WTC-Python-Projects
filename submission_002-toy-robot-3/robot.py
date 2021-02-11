"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""


# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'replay silent', 'replay reversed', 'replay reversed silent']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_x, max_x = -100, 100
min_y, max_y = -200, 200


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    invalid = command
    command = command.lower()
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+invalid+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1) = split_command_input(command)

    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1) or arg1 == "silent" or arg1 == "reversed" or arg1 == 'reversed silent')


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays the movement commands
REPLAY SILENT - replays the movement commands without printing te steps
REPLAY REVERSED - replays the movement commands in the reversed order
REPLAY REVERSED SILENT - replays the movement commands in the reversed order without printing the steps
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command, history_list):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay':
        (do_next, command_output) = do_replay(history_list, robot_name, command)
    elif command_name == 'replay silent':
        (do_next, command_output) = do_replay_silent(robot_name, history_list)
    elif command_name == 'replay reversed':
        (do_next, command_output) = do_replay_reversed(robot_name, history_list)
    elif command_name == 'replay reversed silent':
        (do_next, command_output) = do_replay_reversed_silent(robot_name, history_list)

    print(command_output)
    show_position(robot_name)
    return do_next

def handle_command_silent(robot_name, command, history_list):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    ~ in terms of silent it does not print the command output or show position"""

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay':
        (do_next, command_output) = do_replay(history_list, robot_name, command)
    elif command_name == 'replay silent':
        (do_next, command_output) = do_replay_silent(robot_name, history_list)
    elif command_name == 'replay reversed':
        (do_next, command_output) = do_replay_reversed(robot_name, history_list)
    elif command_name == 'replay reversed silent':
        (do_next, command_output) = do_replay_reversed_silent(robot_name, history_list)

    # print(command_output)
    # show_position(robot_name)
    return do_next


def history_command(history_list,command):
    """Keeps a history of the commands given to it, in the order it was given."""

    if 'replay' in command or "help" in command:
        pass
    else:      
        history_list.append(command)
        #print(history_list)
    return history_list

def get_history_ranged(command, history_list):
    """restricting the range of commands that the robot replays"""
    pass
#or arg1[0].isdigit()
    #temp_history = []
    #print(len(command.split()))
    #if len(command.split()) == 1:
    #    #temp_history = "".join(history_list)
    #    new_history_list = history_list
    #
    #elif len(command.split()) == 2 and command.split()[1][0].isdigit() and '-' not in command.split():
    #    #print('If this works I am dope')
    #    n = command.split()[1]
    #    var = len(history_list) - n
    #    #print('  --  ', var)
    #    ranged = history_list[var:]
    #    new_history_list = history_list[ranged]
    #
    #elif len(command.split()) == 2 and command.spilt()[1][0].isdigit() and '-' in command.split():
    #    n = command.split()[1]    
    #    m = command.split()[2]
    #    var = len(history_list) -n
    #    ranged = slice(var,m + 1)
    #    new_history_list = history_list[ranged]
    #
    #print(command,'\n',new_history_list)
    #print(command,'\n',temp_history)


def do_replay(history_list, robot_name, command):
    """filters out he movement comands and redo only the ovement commands.
       ~ if reversed silent in command then do_replay_reversed _silent
       ~ if silent in command then do_replay_silent
       ~ if reversed in command then do_replay_reversed"""
    
    get_history_ranged(command,history_list)

    if "reversed silent" in command:
        do_replay_reversed_silent(robot_name, history_list)
        return True,f" > {robot_name} replayed {len(history_list)} commands in reverse silently."    

    elif "silent" in command:
        do_replay_silent(robot_name, history_list)
        return True,f" > {robot_name} replayed {len(history_list)} commands silently."

    elif "reversed" in command:
        do_replay_reversed(robot_name, history_list)
        return True,f" > {robot_name} replayed {len(history_list)} commands in reverse."

    
    for i in history_list:
        handle_command(robot_name, i, history_list)
    return True,f" > {robot_name} replayed {len(history_list)} commands."


def do_replay_silent(robot_name, history_list):
    """does the replay command silently... 
       ~ does not print the command output
       ~ only prints how many commands where replayed silently
       ~ then prints the updated position"""
    
    for i in history_list:
        handle_command_silent(robot_name, i, history_list)


def do_replay_reversed(robot_name, history_list):
    """does the replay command in reverse
       ~ does commands in the reversed order to what they where given
       ~ prints each command done + the updated position
       ~ then prints out how many commands where replayed in reverse"""
    
    rev = reversed(history_list)
    for i in rev:
        handle_command(robot_name, i, history_list)


def do_replay_reversed_silent(robot_name, history_list):
    """does the replay command in reverse siently
       ~ does commands in the reversed order to what they where given
       ~ prints only how many commands where replayed in reverse silently
       ~ prints the updated position"""
    
    rev = reversed(history_list)
    for i in rev:
        handle_command_silent(robot_name, i, history_list)


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index

    history_list =[]

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    hist = history_command(history_list, command)
    while handle_command(robot_name, command, history_list):
        command = get_command(robot_name)
        hist = history_command(history_list, command)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
