class car:
    def drive(self):
        print("Driving CAR")

class helicopter:
    def flyit(self):
        print("Flying the helicopter")

class hybridcartor(car,helicopter):
    def startcartor(self):
        print('Cartor started')

hybrid = hybridcartor()
hybrid.drive()
hybrid.flyit()
hybrid.startcartor()
