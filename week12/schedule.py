from week12.panel import *

panel1 = Panel("Opening Ceremonies", datetime.datetime(2025, 6, 20, 17, 30), datetime.datetime(2025, 6, 20, 18, 0))
panel2 = Panel("Closing Ceremonies", datetime.datetime(2025, 6, 23, 17, 30), datetime.datetime(2025, 6, 23, 18, 0))


print(panel1.getPanelDetails())
print(panel2.getPanelDetails())