def can_measure(weight, lst):
    y= map_list(lst)
    x=1
    for i in xrange(len(y)):
        if sum_list(y[i])==weight:
            x=x*0
        else:
            x=x*1
    if x==1:
        return False
    elif x==0:
        return True
    else: 
        print "Argument Error"

#defines all possible mappings of the list of weights to left of balance (-1), right of the balance (1) or not used (0). 
#without loss of generality we didn't have to try out so many because if either one set is -weight or the weight...
def map_list(lst):
    k=len(lst)
    if k ==1:
        return [[-1*lst[0]], [1*lst[0]], [0*lst[0]]]
    elif k>1:
        y =[map_list(lst[:k-1])[i]+[-1*lst[k-1]] for i in xrange(len(map_list(lst[:k-1])))]
        x =[map_list(lst[:k-1])[i]+[1*lst[k-1]] for i in xrange(len(map_list(lst[:k-1])))]
        z =[map_list(lst[:k-1])[i]+[0*lst[k-1]] for i in xrange(len(map_list(lst[:k-1])))]
        w = y+x+z
        return w
    else:
        print "Argument error"

def sum_list(lst):
    y=0
    for i in xrange(len(lst)):
        y=y+lst[i]
    return y