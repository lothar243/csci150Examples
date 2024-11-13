import datetime

class Panel:
    def __init__(self, name, startTime: datetime, endTime:datetime):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
    
    def __str__(self):
        return(f"{self.name} will occur on {self.startTime.strftime("%a %b %d %I:%M%p")}-{self.endTime.strftime("%I:%M%p")}")

    # for backwards compatability, let's keep this method definition, but have it point to the new method
    def getPanelDetails(self):
        return str(self)

    # define == as two panels that occur concurrently
    def __eq__(self, other):
        return self.startTime < other.endTime and other.startTime < self.endTime

    def __lt__(self, other):
        return self.endTime <= other.startTime
    
    def __gt__(self, other):
        return self.startTime >= other.endTime
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __le__(self, other):
        return self < other or self == other
    
    def __ne__(self, other):
        return not self == other

    def getDuration():
        pass

if __name__ == "__main__":
    print("Testing Panel...")
    myPanel = Panel("Opening Ceremonies", datetime.datetime(2025, 6, 20, 17, 30), datetime.datetime(2025, 6, 20, 18, 0))
    print(myPanel)

    myPanel2 = Panel("Overlapping with first half of opening ceremonies", datetime.datetime(2025, 6, 20, 17, 15), datetime.datetime(2025, 6, 20, 17, 45))
    myPanel3 = Panel("Overlapping with second half of opening ceremonies", datetime.datetime(2025, 6, 20, 17, 45), datetime.datetime(2025, 6, 20, 18, 15))

    print(f"{myPanel == myPanel=} - expect True")
    print(f"{myPanel == myPanel2=} - expect True")
    print(f"{myPanel == myPanel3=} - expect True")
    print(f"{myPanel2 == myPanel3=} - expect False")
    print(f"{myPanel < myPanel=} - expect False")
    print(f"{myPanel < myPanel2=} - expect False")
    print(f"{myPanel2 < myPanel3=} - expect True")
    print(f"{myPanel2 > myPanel3=} - expect False")
    print(f"{myPanel2 <= myPanel=} - expect True")
    print(f"{myPanel2 != myPanel=} - expect False")
    print(f"{myPanel2 != myPanel3=} - expect True")

