class MyClass():
    def __init__(self):
        self.birthDay = "20230326"
        
    def saySomething(self,something="Hello World"):
        print(something)
    
    def sayBirthday(self):
        print("Hello, my birthday is ",self.birthDay)

def main():
    myclass=MyClass()
    myclass.saySomething()
    myclass.sayBirthday()
    
if __name__ =="__main__":
    main()