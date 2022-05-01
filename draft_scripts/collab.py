def ActRobot(robot):
if   isRobotCloseToEnemy(enemy_position,robot_position):
    if ((enemy_position[0])==robot_position[0]) : 
         if  (not left == "friend") : return 4
         elif (not right == "friend") : return 2
    elif ((enemy_position[1])==robot_position[1]) :
        if  (not up == "friend") : return 1
        elif (not down == "friend") : return 3
    elif ( (enemy_position[0])-1==robot_position[0])and((enemy_position[1])-1==robot_position[1])) 
        if  (not down == "friend") : return 3
        elif (not right == "friend") : return 2
    elif ( (enemy_position[0])+1==robot_position[0])and((enemy_position[1])-1==robot_position[1])) 
        if  (not down == "friend") : return 3
        elif (not left == "friend") : return 4
    elif ( (enemy_position[0])-1==robot_position[0])and((enemy_position[1])+1==robot_position[1])) 
        if  (not up == "friend") : return 1
        elif (not right == "friend") : return 2
    elif ( (enemy_position[0])+1==robot_position[0])and((enemy_position[1])+1==robot_position[1])) 
        if  (not up == "friend") : return 1
        elif (not left == "friend") : return 4
elif ((enemy_position[0])> robot_position[0])  : return 2
elif ((enemy_position[0])< robot_position[0]) : return 4
elif ((enemy_position[1])> robot_position[1]) :return 3
elif ((enemy_position[1])< robot_position[1]) :return 1 