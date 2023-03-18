#definition of code
#cambio de commit
def create_board (n,m):
    pass

def movements_table (left_sen, up_sen, right_sen,down_sen, hq):
    # the movements will be represented by numbers  1 = up, 2 = left, 3 = down, 4 = right
    # when the mouse found the cheese, this will be represented by the number 5 = found cheese
    # when any sensor is true, it means that the mouse can go in that direction, otherwise he cant (false)
    action = 0
    if hq:
        action = 5
        return action
    elif (left_sen and up_sen and right_sen and down_sen and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen and right_sen and down_sen == False and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen and right_sen == False and down_sen and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen and right_sen == False and down_sen == False and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen == False  and right_sen and down_sen and hq == False): 
        action = 2
        return action
    
    elif (left_sen and up_sen == False and right_sen and down_sen == False and hq == False): 
        action = 4
        return action
    
    elif (left_sen and up_sen == False and right_sen == False and down_sen and hq == False): 
        action = 2
        return action
    
    elif (left_sen and up_sen == False and right_sen == False and down_sen == False and hq == False): 
        action = 2
        return action
    
    elif (left_sen == False and up_sen and right_sen and down_sen and hq == False): 
        action = 1
        return action
    
    elif (left_sen == False and up_sen and right_sen and down_sen == False and hq == False): 
        action = 4
        return action

    elif (left_sen == False and up_sen and right_sen == False and down_sen and hq == False): 
        action = 3
        return action
    
    elif (left_sen == False and up_sen and right_sen == False and down_sen == False and hq == False): 
        action = 1
        return action

    elif (left_sen == False and up_sen == False and right_sen and down_sen and hq == False): 
        action = 4
        return action
    
    elif (left_sen == False and up_sen == False and right_sen and down_sen == False and hq == False): 
        action = 4
        return action
    
    elif (left_sen == False and up_sen == False and right_sen == False and down_sen and hq == False): 
        action = 3
        return action
    
#print(movements_table(True,True,True,False,False))