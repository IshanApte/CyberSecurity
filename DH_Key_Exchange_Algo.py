class KEA:
    def __init__(self):
        self.n=0
        self.g=0
        self.x=0
        self.y=0

    def input(self):
        self.n=int(input("Enter a random Prime number (Public): "))
        self.g=int(input("Enter a random Prime number (Public): "))
        self.x=int(input("Enter a random number (Secret): "))
        self.y=int(input("Enter a random number (Secret): "))

    def SecretKey(self):
        a=((self.g)**(self.x))%self.n
        b=((self.g)**(self.y))%self.n
        k1=((b)**(self.x))%self.n
        k2=((a)**(self.y))%self.n
        print("secret key is ",k1)
        print("secret key is ",k2)
k=KEA()
k.input()
kk=k.SecretKey()
