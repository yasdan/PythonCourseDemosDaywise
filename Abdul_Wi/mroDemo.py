class hello:
    def greet(self):
        print("hello! All!")

class flower:
    def greet(self):
        print("flowers have natural fragrance")

class hify(hello,flower):
    def __init__(self):
        print("Constructor of hify")

hf= hify()
hf.greet()

#print(hify.__mro__)
#print(hify.mro())

