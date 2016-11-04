while i<(len(lst)):
        if type(lst[i]) ==type([]):
            round_list(lst[i],decimals)
        elif type(lst[i]) == [type(0.0),type([])]:
            i+=1
        else:
            list1[i]=round(list1[i],decimals)
                i+=1
               
