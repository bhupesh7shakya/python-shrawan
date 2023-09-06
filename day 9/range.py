def range(end,start=0,step=0):
    print(start+step)
    if start != end:
        range(end,start+1,step)
        
range(10,start=0,step=2)