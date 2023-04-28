not_n = []
with_n = []
def inputts(n, m):
    for x in range(1, m+1):
        if x % 3 == 0:
            with_n.append(x)
        else:
           not_n.append(x)
    nott_n = sum(not_n)
    withh_n = sum(with_n)
    
    subb=(withh_n-nott_n)
    print(abs(subb))

inputts(5,20) 
