import datetime # view information about datetime at https://docs.python.org/3/library/datetime.html

class Panel:
    def __init__(self, name, startTime: datetime, endTime:datetime):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
    
    def getPanelDetails(self):
        return(f"{self.name} will occur on {self.startTime.strftime("%a %b %d %I:%M%p")}-{self.endTime.strftime("%I:%M%p")}")

    def getDuration():
        pass

if __name__ == "__main__":
    print("Testing Panel...")
    myPanel = Panel("Opening Ceremonies", datetime.datetime(2025, 6, 20, 17, 30), datetime.datetime(2025, 6, 20, 18, 0))
    print(myPanel)
    print(myPanel.getPanelDetails())

