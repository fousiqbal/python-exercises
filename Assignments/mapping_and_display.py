# Write a program to get the Reset Event ID from last-reset-info-logs.txt. Find the Event corresponding to the Reset Event ID from fusa-events-mapping.xlsx and display it.

import pandas as pd
with open("/home/fousiai/Downloads/last-reset-info-logs(3).txt",'r') as file:
    data = file.readlines()
    ID = None
    for line in data:
        if "Reset Event ID" in line:
            ID = line.split(' ')[-1]
    doc = pd.read_excel("/home/fousiai/Downloads/fusa-events-mapping.xlsx")
    event = doc[doc["Reset Event ID"] == float(ID)]
    print(str(event["Event"]))
event
