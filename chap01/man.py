class Man:
    def __init__(self, name):
        self.name = name
        print('初期化しました')
    
    def hello(self):
        print("Hello, " + self.name + "!")
    
    def goodbye(self):
        print("Bye, " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()
