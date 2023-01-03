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
            t.append( [
                float(list_of_words[1]),
                float(list_of_words[3]),
                float(list_of_words[5]),
                float(list_of_words[7]),
                float(list_of_words[9]),
                float(list_of_words[11]) #snr
            ])
                
def pf( i):
    a,b,c,d,e,f = [],[],[],[],[],[]
    for v in snr_value[i][ :10]:
        a.append( v[0])
        b.append( v[1])
        c.append( v[2])
        d.append( v[3])
        e.append( v[4])
        f.append( v[5])
    print( "\nScan",i," Rng", a)
    print( "Scan",i, " Azi", b)
    print( "Scan",i," Elev", c)
    print( "Scan",i, " Dopl", d)
    print( "Scan",i," Magn", e)
    print( "Scan",i, " SNR", f)
    

for i in range( 1, 20):
    snr_value[i].sort(reverse=1, key=lambda a: a[5])
    pf( i)
    
    
#output

Scan 1  Rng [11.58, 17.534, 17.534, 17.534, 23.796, 23.796, 23.796, 17.534, 17.534, 1.879]
Scan 1  Azi [0.568, -2.967, 0.0, 0.568, 0.568, 0.542, 0.355, 37.949, -35.056, 0.604]
Scan 1  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 1  Dopl [9.922, 19.962, 20.03, 19.724, 9.922, 30.003, -10.075, 19.962, 19.979, 44.707]
Scan 1  Magn [-76.915, -89.734, -88.957, -88.957, -88.957, -89.864, -92.027, -100.885, -102.243, -102.4]
Scan 1  SNR [33.76, 21.175, 21.025, 20.602, 19.983, 19.096, 17.071, 16.129, 13.75, 13.363]

Scan 2  Rng [11.32, 17.397, 1.879, 1.252, 1.879, 1.879, 0.626, 1.252, 1.252, 1.252]
Scan 2  Azi [0.391, 0.568, -3.402, 1.03, -48.401, -63.679, 23.651, 1.03, -63.535, 50.723]
Scan 2  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 2  Dopl [9.956, 20.03, -15.333, 27.603, -42.307, -54.39, -24.115, -15.708, -37.219, 31.637]
Scan 2  Magn [-71.159, -82.936, -101.451, -104.35, -105.542, -103.751, -114.418, -105.483, -105.679, -108.556]
Scan 2  SNR [40.235, 27.441, 14.477, 12.955, 12.459, 11.967, 11.942, 11.822, 11.52, 10.867]

Scan 3  Rng [11.32, 17.445, 23.551, 23.796, 29.431, 1.879, 2.505, 1.879, 51.974, 48.843]
Scan 3  Azi [0.408, 0.559, 0.488, 0.426, 0.471, -3.429, 0.781, -63.947, 58.27, 44.759]
Scan 3  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 3  Dopl [9.99, 19.979, 9.99, 29.952, 19.877, -15.367, -56.262, -54.39, -14.806, 1.651]
Scan 3  Magn [-68.144, -77.309, -82.59, -87.347, -89.018, -101.912, -102.976, -104.315, -95.918, -100.971]
Scan 3  SNR [43.192, 33.039, 27.025, 22.259, 19.988, 14.398, 12.299, 11.722, 11.25, 11.169]

Scan 4  Rng [11.32, 17.445, 23.57, 23.796, 29.431, 1.252, 1.879, 51.348, 45.086, 48.843]
Scan 4  Azi [0.408, 0.4, 0.4, 0.364, 0.373, -54.982, -63.597, -63.535, 33.351, 5.441]
Scan 4  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 4  Dopl [9.99, 19.979, 9.99, 29.952, 19.877, 17.256, -43.924, -33.594, -38.07, -13.189]
Scan 4  Magn [-68.108, -76.615, -81.512, -87.779, -89.458, -105.244, -104.054, -95.203, -102.878, -96.198]
Scan 4  SNR [42.926, 33.472, 27.805, 21.492, 19.211, 12.957, 11.555, 11.475, 11.468, 11.039]

Scan 5  Rng [11.33, 17.455, 23.551, 23.522, 1.252, 1.879, 1.879, 1.879, 1.879, 1.879]
Scan 5  Azi [0.408, 0.4, 0.391, 0.373, 4.933, -3.269, -63.7, 5.076, -3.74, 0.977]
Scan 5  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 5  Dopl [9.99, 19.962, 10.007, 29.952, -2.825, -15.35, -43.941, -45.66, -46.408, -29.577]
Scan 5  Magn [-68.817, -77.214, -82.514, -86.649, -105.392, -104.135, -103.606, -104.705, -105.247, -104.336]
Scan 5  SNR [43.052, 33.325, 27.447, 23.315, 13.438, 12.981, 12.647, 12.645, 11.951, 11.947]

Scan 6  Rng [11.32, 17.445, 23.57, 23.531, 1.879, 1.879, 1.252, 1.879, 1.879, 1.252]
Scan 6  Azi [0.4, 0.391, 0.462, 0.4, -3.42, -63.432, -54.935, 57.791, -3.651, 5.236]
Scan 6  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 6  Dopl [9.99, 19.979, 9.99, 29.952, -15.367, -43.941, 17.239, 18.856, -46.391, 43.022]
Scan 6  Magn [-68.881, -77.421, -82.64, -87.641, -102.693, -104.436, -107.01, -105.587, -105.364, -107.076]
Scan 6  SNR [43.554, 33.546, 27.573, 22.626, 14.557, 12.552, 12.416, 12.208, 12.198, 12.141]

Scan 7  Rng [11.32, 17.445, 23.57, 23.58, 29.431, 1.252, 1.252, 48.217, 48.843, 49.152]
Scan 7  Azi [0.417, 0.408, 0.364, 0.426, 0.337, 1.021, -63.473, -48.295, -26.385, -64.979]
Scan 7  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 7  Dopl [9.99, 19.962, 9.99, 29.952, 19.877, -15.691, -37.219, -40.299, 28.59, -13.223]
Scan 7  Magn [-68.163, -76.625, -82.654, -85.559, -89.972, -105.314, -105.581, -98.22, -102.408, -96.548]
Scan 7  SNR [43.159, 33.611, 26.773, 23.828, 18.728, 11.608, 11.242, 11.067, 10.908, 10.74]

Scan 8  Rng [11.32, 17.445, 23.561, 23.796, 1.879, 3.757, 3.131, 3.131, 2.505, 2.505]
Scan 8  Azi [0.4, 0.4, 0.462, 0.391, -3.384, -3.722, -3.349, -3.633, -55.904, 0.666]
Scan 8  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 8  Dopl [9.99, 19.962, 9.99, 29.952, -15.367, -43.668, 32.573, -29.305, 24.778, -42.562]
Scan 8  Magn [-68.682, -77.105, -82.617, -88.504, -102.231, -101.038, -102.083, -102.394, -104.221, -103.405]
Scan 8  SNR [43.208, 33.856, 27.252, 21.372, 14.688, 13.565, 13.097, 12.937, 12.388, 12.384]

Scan 9  Rng [11.32, 17.445, 23.561, 23.58, 1.879, 2.505, 1.879, 1.252, 2.505, 1.879]
Scan 9  Azi [0.4, 0.408, 0.426, 0.4, -3.322, 9.408, 5.005, -55.06, 0.719, -3.758]
Scan 9  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 9  Dopl [9.99, 19.962, 9.99, 29.952, -15.367, -32.028, -45.626, 17.273, -42.579, -46.391]
Scan 9  Magn [-68.875, -77.51, -82.453, -86.138, -103.072, -104.832, -104.214, -105.672, -102.609, -104.879]
Scan 9  SNR [42.987, 33.16, 27.464, 23.796, 14.514, 14.017, 13.731, 13.649, 13.233, 12.858]

Scan 10  Rng [11.58, 17.455, 23.561, 23.796, 2.505, 1.879, 1.879, 1.879, 1.252, 2.505]
Scan 10  Azi [0.408, 0.417, 0.408, 0.355, -63.473, -63.597, -3.393, 5.022, 1.012, 0.719]
Scan 10  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 10  Dopl [9.99, 19.962, 9.99, 29.952, -49.948, -43.941, -15.367, -45.643, 27.603, -56.262]
Scan 10  Magn [-68.457, -76.715, -82.775, -88.591, -101.713, -102.743, -103.211, -104.232, -104.726, -102.927]
Scan 10  SNR [42.966, 33.663, 26.79, 20.977, 13.579, 13.417, 13.258, 12.907, 12.656, 12.385]

Scan 11  Rng [11.33, 17.465, 23.561, 23.512, 3.131, 1.879, 3.131, 3.131, 2.505, 2.505]
Scan 11  Azi [0.408, 0.391, 0.4, 0.373, -3.438, 0.586, 0.994, 5.031, 9.462, -3.26]
Scan 11  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 11  Dopl [9.99, 19.962, 10.007, 29.952, 32.556, 44.656, -19.23, -13.427, -32.011, -50.255]
Scan 11  Magn [-68.803, -77.187, -82.423, -86.404, -101.391, -103.232, -101.414, -102.184, -105.027, -103.151]
Scan 11  SNR [43.251, 33.803, 27.728, 23.804, 13.591, 13.408, 13.366, 13.309, 13.083, 12.799]

Scan 12  Rng [11.32, 17.445, 23.57, 23.531, 1.879, 4.383, 3.493, 2.505, 3.757, 3.757]
Scan 12  Azi [0.4, 0.4, 0.453, 0.346, -3.402, -42.305, -3.776, -55.904, -3.482, -3.749]
Scan 12  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 12  Dopl [9.99, 19.979, 10.007, 29.952, -15.367, -45.37, -29.288, 24.88, -30.326, -43.668]
Scan 12  Magn [-68.965, -77.384, -82.79, -87.364, -102.081, -104.7, -101.963, -103.769, -101.522, -101.955]
Scan 12  SNR [43.391, 33.993, 27.604, 23.098, 15.017, 13.734, 13.376, 13.168, 13.072, 13.027]

Scan 13  Rng [11.58, 17.455, 23.551, 23.58, 29.431, 1.879, 2.505, 1.252, 2.505, 2.505]
Scan 13  Azi [0.408, 0.4, 0.435, 0.479, 0.364, -3.331, 9.381, -55.044, -55.716, -64.112]
Scan 13  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 13  Dopl [9.99, 19.962, 9.99, 29.952, 19.877, -15.367, -32.011, 17.273, -44.928, 46.357]
Scan 13  Magn [-68.514, -77.163, -82.071, -85.932, -89.253, -102.883, -104.539, -105.578, -103.615, -102.536]
Scan 13  SNR [43.034, 33.211, 27.389, 23.497, 19.757, 14.055, 13.893, 13.575, 12.998, 12.792]

Scan 14  Rng [11.32, 17.465, 23.57, 23.796, 29.431, 3.131, 3.757, 1.879, 2.813, 2.505]
Scan 14  Azi [0.4, 0.408, 0.453, 0.417, 0.4, -3.749, -3.438, -3.402, -64.092, 0.692]
Scan 14  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 14  Dopl [9.99, 19.962, 9.99, 29.952, 19.877, -29.254, -30.326, -15.333, -49.982, -56.245]
Scan 14  Magn [-68.801, -77.273, -83.265, -88.475, -88.924, -101.288, -100.209, -102.934, -101.686, -102.971]
Scan 14  SNR [43.367, 33.771, 26.945, 21.736, 20.688, 14.393, 13.966, 13.899, 13.842, 13.159]

Scan 15  Rng [11.33, 17.445, 23.551, 23.796, 3.757, 3.757, 2.505, 3.513, 2.505, 3.131]
Scan 15  Azi [0.408, 0.4, 0.382, 0.435, -3.598, -42.583, 4.96, -3.438, -64.236, 0.906]
Scan 15  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 15  Dopl [9.99, 19.962, 9.99, 29.952, -30.377, -30.411, 51.088, -29.407, 46.374, -19.23]
Scan 15  Magn [-68.961, -77.295, -82.823, -89.178, -99.081, -104.999, -103.074, -101.551, -102.537, -101.928]
Scan 15  SNR [43.1, 33.809, 27.436, 21.013, 15.714, 14.306, 13.495, 13.309, 13.285, 13.206]

Scan 16  Rng [11.32, 17.445, 23.796, 23.561, 29.431, 1.879, 3.757, 2.505, 3.503, 2.505]
Scan 16  Azi [0.4, 0.4, 0.453, 0.355, 0.373, -3.287, -3.633, 0.684, -3.527, -64.257]
Scan 16  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 16  Dopl [9.99, 19.962, 9.99, 29.952, 19.877, -15.367, -30.343, -42.562, -29.356, 46.289]
Scan 16  Magn [-68.687, -77.188, -83.22, -87.42, -90.069, -102.956, -100.968, -102.537, -101.299, -102.984]
Scan 16  SNR [43.288, 33.734, 26.543, 22.542, 19.363, 14.225, 13.542, 13.413, 13.34, 12.931]

Scan 17  Rng [11.33, 17.455, 23.57, 23.512, 4.012, 5.01, 3.757, 2.505, 5.636, 3.131]
Scan 17  Azi [0.4, 0.408, 0.391, 0.426, -3.678, -3.536, -42.571, -64.215, -3.544, -3.491]
Scan 17  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 17  Dopl [9.99, 19.962, 9.99, 29.952, -30.377, 44.06, -30.616, 46.374, -33.066, 32.573]
Scan 17  Magn [-69.074, -77.342, -82.899, -87.689, -99.954, -99.81, -105.274, -102.16, -100.607, -101.759]
Scan 17  SNR [42.919, 33.542, 27.172, 22.391, 14.557, 14.108, 13.561, 13.476, 13.475, 13.43]

Scan 18  Rng [11.33, 17.455, 23.551, 23.512, 4.012, 5.636, 5.636, 3.757, 5.01, 1.879]
Scan 18  Azi [0.4, 0.391, 0.382, 0.373, -3.66, -55.185, 0.639, -42.51, -3.447, 0.932]
Scan 18  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 18  Dopl [9.99, 19.962, 9.99, 29.952, -30.377, 11.811, 52.705, -30.411, 44.06, -29.595]
Scan 18  Magn [-69.16, -77.589, -83.099, -87.761, -99.429, -100.472, -99.73, -104.733, -99.998, -103.342]
Scan 18  SNR [42.817, 33.287, 26.942, 22.299, 15.299, 14.255, 14.105, 14.096, 13.976, 13.697]

Scan 19  Rng [11.33, 17.455, 23.561, 23.796, 4.002, 3.757, 2.505, 4.383, 4.383, 4.383]
Scan 19  Azi [0.408, 0.408, 0.373, 0.373, -3.616, -42.388, -63.989, -3.74, -64.195, -42.281]
Scan 19  Elev [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Scan 19  Dopl [9.99, 19.962, 10.007, 29.952, -30.377, -30.411, -49.982, -45.285, -27.433, -45.319]
Scan 19  Magn [-68.853, -77.128, -82.972, -88.831, -99.047, -104.391, -102.229, -100.72, -100.432, -104.876]
Scan 19  SNR [43.17, 33.73, 27.193, 21.385, 15.384, 14.347, 13.543, 13.511, 13.371, 13.329]
    
