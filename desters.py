class Dog:
    def __init__(self, name):
        self.name = name

    def speaking (self):
        print (f"I am a dog. My name is {self.name}")

class Cat:
    def __init__(self, name):
        self.name = name

    def speaking (self):
        print (f"I am a cat. My name is {self.name}")
        print (f"My friend is {dog1.name}")

    def speaking_and_eating (self):
        self.speaking()


dog1 = Dog ("Bova")
cat1 = Cat ("Momo")

cat1.speaking()
cat1.speaking_and_eating()


