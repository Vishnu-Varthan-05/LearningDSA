def printsomenums(n):
    if n == 0:
        return 
    print(n)
    printsomenums(n-1)

def printsomenumsRev(n):
    if n == 0:
        return 
    printsomenumsRev(n-1)
    print(n)
    

printsomenums(5)
printsomenumsRev(5)