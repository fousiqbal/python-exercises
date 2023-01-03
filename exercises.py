# Q1) Write a program to get the Reset Event ID from last-reset-info-logs.txt. Find the Event corresponding to the Reset Event ID from fusa-events-mapping.xlsx and display it.


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

#output
9 FUSA_EVENT_CCP_FATAL_ERROR,
Name: Event, dtype: object
Reset Event ID	Event
9	9.0	FUSA_EVENT_CCP_FATAL_ERROR,



# Q2) Write a program to get the list of top 10 moving detections with maximum SNR for each scan.(flags parameter is empty for moving detections)


with open("/home/fousiai/Downloads/replay-det_VP160.txt",'r') as file:

    
    
    snr_value =[] 
    t = []

    for line in file:
#         print(line)
        x = line.find('SS')
#         print(x)
        if x ==-1:
            list_of_words = line.split()
            if( len( list_of_words) < 8):
                snr_value.append( t)
                t = []
                continue
            t.append( float(list_of_words[ 11]))
            

for i in range( 1, 20):
    snr_value[i].sort(reverse=1)
    print( "Scan", i, snr_value[i][:10])
    
    
    #output
Scan 1 [33.76, 21.175, 21.025, 20.602, 19.983, 19.096, 17.071, 16.129, 13.75, 13.363]
Scan 2 [40.235, 27.441, 14.477, 12.955, 12.459, 11.967, 11.942, 11.822, 11.52, 10.867]
Scan 3 [43.192, 33.039, 27.025, 22.259, 19.988, 14.398, 12.299, 11.722, 11.25, 11.169]
Scan 4 [42.926, 33.472, 27.805, 21.492, 19.211, 12.957, 11.555, 11.475, 11.468, 11.039]
Scan 5 [43.052, 33.325, 27.447, 23.315, 13.438, 12.981, 12.647, 12.645, 11.951, 11.947]
Scan 6 [43.554, 33.546, 27.573, 22.626, 14.557, 12.552, 12.416, 12.208, 12.198, 12.141]
Scan 7 [43.159, 33.611, 26.773, 23.828, 18.728, 11.608, 11.242, 11.067, 10.908, 10.74]
Scan 8 [43.208, 33.856, 27.252, 21.372, 14.688, 13.565, 13.097, 12.937, 12.388, 12.384]
Scan 9 [42.987, 33.16, 27.464, 23.796, 14.514, 14.017, 13.731, 13.649, 13.233, 12.858]
Scan 10 [42.966, 33.663, 26.79, 20.977, 13.579, 13.417, 13.258, 12.907, 12.656, 12.385]
Scan 11 [43.251, 33.803, 27.728, 23.804, 13.591, 13.408, 13.366, 13.309, 13.083, 12.799]
Scan 12 [43.391, 33.993, 27.604, 23.098, 15.017, 13.734, 13.376, 13.168, 13.072, 13.027]
Scan 13 [43.034, 33.211, 27.389, 23.497, 19.757, 14.055, 13.893, 13.575, 12.998, 12.792]
Scan 14 [43.367, 33.771, 26.945, 21.736, 20.688, 14.393, 13.966, 13.899, 13.842, 13.159]
Scan 15 [43.1, 33.809, 27.436, 21.013, 15.714, 14.306, 13.495, 13.309, 13.285, 13.206]
Scan 16 [43.288, 33.734, 26.543, 22.542, 19.363, 14.225, 13.542, 13.413, 13.34, 12.931]
Scan 17 [42.919, 33.542, 27.172, 22.391, 14.557, 14.108, 13.561, 13.476, 13.475, 13.43]
Scan 18 [42.817, 33.287, 26.942, 22.299, 15.299, 14.255, 14.105, 14.096, 13.976, 13.697]
Scan 19 [43.17, 33.73, 27.193, 21.385, 15.384, 14.347, 13.543, 13.511, 13.371, 13.329]
    
        
