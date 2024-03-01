class Euclid:
    def __init__(self):
        self.a=0
        self.b=0

    def input(self):
        self.a=int(input("Enter First number: "))
        self.b=int(input("Enter Second number: "))

    def gcd(self):
        r1=self.a
        r2=self.b
        while r2>0:
            q=r1//r2
            r=r1-q*r2
            r1=r2
            r2=r
        print("GCD is: ",r1)

    def Extgcd(self):
        r1=self.a
        r2=self.b
        s1=1
        s2=0
        t1=0
        t2=1
        while r2>0:
            q=r1//r2
            r=r1-q*r2
            r1=r2
            r2=r
            s=s1-q*s2
            s1=s2
            s2=s
            t=t1-q*t2
            t1=t2
            t2=t

        print("The Value of s is: ",s1)
        print("The Value of t is: ",t1)
y=1
while(y):
    a=Euclid()
    a.input()
    s=a.gcd()
    g=a.Extgcd()
    print("Do you want to continue (1/0)")
    y=int(input("Enter choice: "))
print("Program Terminated")
