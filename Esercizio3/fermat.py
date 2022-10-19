def MCMillerRabinTest(n,q,a):
    s = 0
    while(q%2==0):
        s = s + 1
        q = q / 2

    x = (a**q) % n

    if x == 1%n or x == -1%n:
       return("n forse primo")
    else:
        while(s-1>=0):
            x = (x**2) % n
            if x == -1%n:
                return("n forse primo")
            s = s-1
        return("n è composto")

def main():
    n1 = 7
    n2 = 9
    q1 = n1-1
    q2 = n2-1
    for a in range(2,6):
        print(MCMillerRabinTest(n1,q1,a))
        
    for a in range(2,8):
        print(MCMillerRabinTest(n2,q2,a))
main()