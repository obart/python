#Luis Marcano, Owen Bartolotta
#lab 6
#cisc 106-15
from cisc106 import *
##def round_list(lst, decimals):
##    """a function that takes a list of floats and rounds them
##    Parameter:lst, a list and an int, integer
##    return: a float that is rounded 
##
##    """
##    
####    if type(float_list[1]) is float and float_list[1]<0:
####        print("Sorry inapropiate list")
####        return None
####    i=0
####    while i<(len(lst)-1):
####        if type(lst[i]) ==type([]):
####            lst = [round_list(lst[i],decimals)]
####        elif type(lst[i]) ==type(0.0):
####            lst = [round(i,decimals)]# problem in red
######        elif type(lst[i]) is list:
######            lst = [round_list(lst[i],decimals)]
####        else:
####            return None
####        i = i+1
####    return lst
##    i=0
##    while i<len(lst):
##        if type(lst)!=type([]) or decimals<0:
##            return 0
##        elif type(lst[i]) == type([]):
##           return round_list(lst[i],decimals)
##        elif type(lst[i]) == type(""):
##            i+=1
##        elif type(lst[i]) ==type(0.0):
##            nf = round(lst[i],decimals)
##            lst[i]=nf
##            i+=1
####            lst = [round(lst[i],decimals)]
##    return lst
        
lst= [1.111, 2, [2.222,"a"]]
round_list(lst,1)
assertEqual(lst,[1.1, 2, [2.2, "a"]])
def word_separator(sentence):
    newsentence = ''
    for item in sentence:
        if item.isupper():
            newsentence += " "+item.lower() 
        else:
            newsentence += item
    if newsentence[0] == " ":
        newsentence = newsentence[1:]
        
    return newsentence.capitalize()


##s= "HiWordHouse"
##print(word_separator(s))



class Ship():
    symbol = ""
    length = 0

def draw_board(lst):
    ret = ""
    for row in lst:
 #       ret += "|"
        for cell in row:
            if type(cell) == type(Ship()):#type of coor instance
                ret += cell.symbol
            elif cell:
                ret += "X"
            else:
                ret += "."
        ret+="\n"
    return ret


s=Ship()
s.symbol="B"
s.length=3

board=[[True,True,False,False],
       [s,False,False,True],
       [s,True,False,True],
       [s,False,False,False]]
board_rendering="""XX..
B..X
BX.X
B...
"""
assertEqual(draw_board(board),board_rendering)
        

