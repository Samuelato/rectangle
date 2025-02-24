class robot:
    def __init__(self,name):
        self.name=name
        self.batery=100
    def sleep(self):
        print(f"Hello! my name is {self.name} and my batery is fully charged to {self.batery}%")

Robot=robot("evllin")
Robot.sleep()

Robot1=robot("bastianali")
Robot1.sleep()