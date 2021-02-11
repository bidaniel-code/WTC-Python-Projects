import random
import turtle

x = range(-100,100)
y = range(-200,200)
obstacles = []

def is_position_blocked(x,y):
    """
    
    """
    for obstacles in get_obstacles():
        if (obstacles[0] <= x <= obstacles[0] + 4) and (obstacles[1] <= y <= obstacles[1] + 4):
            return True
        return False  


def is_path_blocked(x1,y1, x2, y2):
    """
    
    """
    x_1 = min([x1, x2])
    x_2 = max([x1, x2])
    y_1 = min([y1, y2])
    y_2 = max([y1, y2])
    if x1 == x2:
        for x in range(y_1, y_2+1):
            if is_position_blocked(x1, x):
                return True
    elif y1 == y2:
        for x in range(x_1, x_2 + 1):
            if is_position_blocked(x, y1):
                return True
    return False


def get_obstacles():
    """
    
    """
    global obstacles
    obstacles = []
    rand_num = random.randint(1,10)
    for i in range(rand_num):
        x = random.randint(-100,100)
        y = random.randint(-200,200)
        obstacles.append((x,y))
    
    return obstacles


def draw_obstacles(x,y):
    screen = turtle.Turtle()
    turtle.tracer(0)
    screen.begin_fill()
    screen.ht()
    screen.pu()
    screen.goto(x,y)
    screen.pendown()
    screen.goto(x,y+4)
    screen.goto(x+4,y+4)
    screen.goto(x+4,y)
    screen.goto(x,y)
    screen.end_fill()
    screen.pu()
    turtle.tracer(1)

def all_obstacales_draw():
    print("There are some obstacles:")
    for coordinate in obstacles:
        draw_obstacles(coordinate[0],coordinate[1])

# def all_obstacales_text():
#     if obstacles != None:
#         print("There are some obstacles:")
#         for coordinate in obstacles:
#             print(f"- At position {coordinate[0]},{coordinate[1]} (to {coordinate[0]+4},{coordinate[1]+4})")