from types import new_class


def basedefence(base):
    up =base.investigate_up()
    down =base.investigate_down()
    left =base.investigate_left()
    right =base.investigate_right()
    ne =base.investigate_ne()
    nw =base.investigate_nw()
    se =base.investigate_se()
    sw =base.investigate_sw()
    resultant_step= {'release_virus' : 0}
    directions=[up, down, left, right, ne, nw, se, sw]
    enemycount=0
    for dire in directions:
        if 'enemy' in dire:
            enemycount+=1
    if enemycount>4:
        if base.GetVirus()>1000:
            base.DeployVirus(1000)
        else :
            base.DeployVirus(base.GetVirus()*0.9)
    elif enemycount>0:
        if base.GetVirus()>600:
            base.DeployVirus(600)
        else :
            base.DeployVirus(base.GetVirus()*0.75)

    friendcount=0
    for dire in directions:
        if 'friend' in dire:
            friendcount+=1
    #will keep 5 friends around the base
    if friendcount<5:
        if base.GetElixir()-50*(5-friendcount)>400:
            for i in range(1,6-friendcount):
                base.create_robot('defc')
    
def ActRobot(robot):
    basecrd=base.Getposition()
    robocrd=robot.GetPosition()
    initial=robot.GetInitialSignal()
    if ('defc' in initial) and (robocrd==basecrd) :
        return (randint(1,4))
    elif 'defc' in initial:
        if robocrd[0]<basecrd[0] and robocrd[1]>=basecrd[1]:
            return 1
        elif robocrd[0]>basecrd[0] and robocrd[1]<=basecrd[1]:
            return 3
        elif robocrd[0]>=basecrd[0] and robocrd[1]>basecrd[1]:
            return 4
        elif robocrd[0]<=basecrd[0] and robocrd[1]<basecrd[1]:
            return 2

if en.startswith("E:") :
                # Guide other robots to enemy base by using some algorithm
                e = en.split(":")[1].split(",")
                xe=int(e[0])
                ye=int(e[1])
                enemy_position = (xe, ye)
                robot_position = robot.GetPosition()
                xr=robot_position[0]
                yr=robot_position[1]
                if isRobotCloseToEnemy(enemy_position,robot_position)==False:
                    if xr<xe:
                        return 2
                    elif xr>xe:
                        return 4
                    if yr>ye:
                        return 1
                    elif yr<ye:
                        return 3
                    
                if enemy_position == robot_position or isRobotCloseToEnemy(enemy_position,robot_position):
                        virus_amt = 1000
                        while(robot.GetVirus() > virus_amt):
                                robot.DeployVirus(virus_amt)
                        return 0  



if 'attack' in initial:
                grid=int(initial.split()[1])
                pos=int(initial.split()[2])
                xc=int(initial.split()[3])
                yc=int(initial.split()[4])

                #make the robots reach their grid position
                if grid==1:
                        if (xr<=xc/2 and yr<=yc/2) == False:
                                if xr>xc/2:
                                        return 4
                                if yr>yc/2:
                                        return 1
                        elif (yr%2==1 and xr!=xc/2):
                                return 2
                        elif (yr%2==0 and xr!=1):
                                return 4
                        elif (yr%2==1 and xr==xc/2):
                                return 3
                        elif (yr%2==0 and xr==0 and yr!=yc/2):
                                return 3
                        elif (yr%2==0 and xr==0 and yr==yc/2):
                                return 1
                if grid==2:
                        if (xr<=xc and xr>xc/2 and yr<=yc/2) == False:
                                if xr<=xc/2:
                                        return 2
                                if yr>yc/2:
                                        return 1
                        elif (yr%2==1 and xr!=xc):
                                return 2
                        elif (yr%2==0 and xr!=1+xc/2):
                                return 4
                        elif (yr%2==1 and xr==xc):
                                return 3
                        elif (yr%2==0 and xr==1+xc/2 and yr!=yc/2):
                                return 3
                        elif (yr%2==0 and xr==1+xc/2 and yr==yc/2):
                                return 1
                if grid==3:
                        if (xr<=xc/2 and yr<=yc and yr>yc/2) == False:
                                if xr>xc/2:
                                        return 4
                                if yr<=yc/2:
                                        return 3
                        elif (yr%2==1 and xr!=xc/2):
                                return 2
                        elif (yr%2==0 and xr!=1):
                                return 4
                        elif (yr%2==1 and xr==xc/2):
                                return 3
                        elif (yr%2==0 and xr==0 and yr!=yc):
                                return 3
                        elif (yr%2==0 and xr==0 and yr==yc):
                                return 1
                if grid==4:
                        if (xr>xc/2 and yr>yc/2) == False:
                                if xr<=xc/2:
                                        return 2
                                if yr<=yc/2:
                                        return 3
                        elif (yr%2==1 and xr!=xc):
                                return 2
                        elif (yr%2==0 and xr!=1+xc/2):
                                return 4
                        elif (yr%2==1 and xr==xc):
                                return 3
                        elif (yr%2==0 and xr==0 and yr!=yc):
                                return 3
                        elif (yr%2==0 and xr==0 and yr==yc):
                                return 1

        
        
        
