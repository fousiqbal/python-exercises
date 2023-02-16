                                                    ASSIGNMENT1

Q1) Write a program to get the Reset Event ID from last-reset-info-logs.txt. Find the Event corresponding to the Reset Event ID from fusa-events-mapping.xlsx and display it.


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



Q2) Write a program to get the list of top 10 moving detections with maximum SNR for each scan.(flags parameter is empty for moving detections)


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
    
OR


def get_detections( detection):

  with open("/home/fousiai/Downloads/replay-det_VP160.txt",'r') as file:
    data = file.readlines()
    file.close()
  value = []
  for line in data:
    if "Skipped" in line:
      break  
    x = line.find('SS')
    if x == -1:
        list_of_words = line.split()
        if "Scan sequence" in line:
          seq_no=list_of_words[2].replace(',', '')
          if seq_no != "0":
            detection.append(value)
            value = []
          continue
         
        else :
          value.append( [
            seq_no,
            float(list_of_words[1]),
            float(list_of_words[3]),
            float(list_of_words[5]),
            float(list_of_words[7]),
            float(list_of_words[9]),
            float(list_of_words[11]) #snr
          ])
  detection.append(value)
  return detection
 
def max_snr(detection,k):

  import pandas as pd
  for scan in detection:
    details = pd.DataFrame(scan,columns = ['scan','rng','azi','elev','dopl','magn','snr'])
    rslt_pd = details.sort_values(by = 'snr',ascending = 0,ignore_index = 1)
    print("\n",rslt_pd.iloc[ :k])

detection=[]      
get_detections(detection)  
max_snr(detection, 10)

#output

 scan     rng     azi  elev    dopl     magn     snr
0    0  11.580   0.568   0.0   9.922  -76.915  33.760
1    0  17.534  -2.967   0.0  19.962  -89.734  21.175
2    0  17.534   0.000   0.0  20.030  -88.957  21.025
3    0  17.534   0.568   0.0  19.724  -88.957  20.602
4    0  23.796   0.568   0.0   9.922  -88.957  19.983
5    0  23.796   0.542   0.0  30.003  -89.864  19.096
6    0  23.796   0.355   0.0 -10.075  -92.027  17.071
7    0  17.534  37.949   0.0  19.962 -100.885  16.129
8    0  17.534 -35.056   0.0  19.979 -102.243  13.750
9    0   1.879   0.604   0.0  44.707 -102.400  13.363

   scan     rng     azi  elev    dopl     magn     snr
0    1  11.320   0.391   0.0   9.956  -71.159  40.235
1    1  17.397   0.568   0.0  20.030  -82.936  27.441
2    1   1.879  -3.402   0.0 -15.333 -101.451  14.477
3    1   1.252   1.030   0.0  27.603 -104.350  12.955
4    1   1.879 -48.401   0.0 -42.307 -105.542  12.459
5    1   1.879 -63.679   0.0 -54.390 -103.751  11.967
6    1   0.626  23.651   0.0 -24.115 -114.418  11.942
7    1   1.252   1.030   0.0 -15.708 -105.483  11.822
8    1   1.252 -63.535   0.0 -37.219 -105.679  11.520
9    1   1.252  50.723   0.0  31.637 -108.556  10.867

   scan     rng     azi  elev    dopl     magn     snr
0    2  11.320   0.408   0.0   9.990  -68.144  43.192
1    2  17.445   0.559   0.0  19.979  -77.309  33.039
2    2  23.551   0.488   0.0   9.990  -82.590  27.025
3    2  23.796   0.426   0.0  29.952  -87.347  22.259
4    2  29.431   0.471   0.0  19.877  -89.018  19.988
5    2   1.879  -3.429   0.0 -15.367 -101.912  14.398
6    2   2.505   0.781   0.0 -56.262 -102.976  12.299
7    2   1.879 -63.947   0.0 -54.390 -104.315  11.722
8    2  51.974  58.270   0.0 -14.806  -95.918  11.250
9    2  48.843  44.759   0.0   1.651 -100.971  11.169

   scan     rng     azi  elev    dopl     magn     snr
0    3  11.320   0.408   0.0   9.990  -68.108  42.926
1    3  17.445   0.400   0.0  19.979  -76.615  33.472
2    3  23.570   0.400   0.0   9.990  -81.512  27.805
3    3  23.796   0.364   0.0  29.952  -87.779  21.492
4    3  29.431   0.373   0.0  19.877  -89.458  19.211
5    3   1.252 -54.982   0.0  17.256 -105.244  12.957
6    3   1.879 -63.597   0.0 -43.924 -104.054  11.555
7    3  51.348 -63.535   0.0 -33.594  -95.203  11.475
8    3  45.086  33.351   0.0 -38.070 -102.878  11.468
9    3  48.843   5.441   0.0 -13.189  -96.198  11.039

   scan     rng     azi  elev    dopl     magn     snr
0    4  11.330   0.408   0.0   9.990  -68.817  43.052
1    4  17.455   0.400   0.0  19.962  -77.214  33.325
2    4  23.551   0.391   0.0  10.007  -82.514  27.447
3    4  23.522   0.373   0.0  29.952  -86.649  23.315
4    4   1.252   4.933   0.0  -2.825 -105.392  13.438
5    4   1.879  -3.269   0.0 -15.350 -104.135  12.981
6    4   1.879 -63.700   0.0 -43.941 -103.606  12.647
7    4   1.879   5.076   0.0 -45.660 -104.705  12.645
8    4   1.879  -3.740   0.0 -46.408 -105.247  11.951
9    4   1.879   0.977   0.0 -29.577 -104.336  11.947

   scan     rng     azi  elev    dopl     magn     snr
0    5  11.320   0.400   0.0   9.990  -68.881  43.554
1    5  17.445   0.391   0.0  19.979  -77.421  33.546
2    5  23.570   0.462   0.0   9.990  -82.640  27.573
3    5  23.531   0.400   0.0  29.952  -87.641  22.626
4    5   1.879  -3.420   0.0 -15.367 -102.693  14.557
5    5   1.879 -63.432   0.0 -43.941 -104.436  12.552
6    5   1.252 -54.935   0.0  17.239 -107.010  12.416
7    5   1.879  57.791   0.0  18.856 -105.587  12.208
8    5   1.879  -3.651   0.0 -46.391 -105.364  12.198
9    5   1.252   5.236   0.0  43.022 -107.076  12.141

   scan     rng     azi  elev    dopl     magn     snr
0    6  11.320   0.417   0.0   9.990  -68.163  43.159
1    6  17.445   0.408   0.0  19.962  -76.625  33.611
2    6  23.570   0.364   0.0   9.990  -82.654  26.773
3    6  23.580   0.426   0.0  29.952  -85.559  23.828
4    6  29.431   0.337   0.0  19.877  -89.972  18.728
5    6   1.252   1.021   0.0 -15.691 -105.314  11.608
6    6   1.252 -63.473   0.0 -37.219 -105.581  11.242
7    6  48.217 -48.295   0.0 -40.299  -98.220  11.067
8    6  48.843 -26.385   0.0  28.590 -102.408  10.908
9    6  49.152 -64.979   0.0 -13.223  -96.548  10.740

   scan     rng     azi  elev    dopl     magn     snr
0    7  11.320   0.400   0.0   9.990  -68.682  43.208
1    7  17.445   0.400   0.0  19.962  -77.105  33.856
2    7  23.561   0.462   0.0   9.990  -82.617  27.252
3    7  23.796   0.391   0.0  29.952  -88.504  21.372
4    7   1.879  -3.384   0.0 -15.367 -102.231  14.688
5    7   3.757  -3.722   0.0 -43.668 -101.038  13.565
6    7   3.131  -3.349   0.0  32.573 -102.083  13.097
7    7   3.131  -3.633   0.0 -29.305 -102.394  12.937
8    7   2.505 -55.904   0.0  24.778 -104.221  12.388
9    7   2.505   0.666   0.0 -42.562 -103.405  12.384

   scan     rng     azi  elev    dopl     magn     snr
0    8  11.320   0.400   0.0   9.990  -68.875  42.987
1    8  17.445   0.408   0.0  19.962  -77.510  33.160
2    8  23.561   0.426   0.0   9.990  -82.453  27.464
3    8  23.580   0.400   0.0  29.952  -86.138  23.796
4    8   1.879  -3.322   0.0 -15.367 -103.072  14.514
5    8   2.505   9.408   0.0 -32.028 -104.832  14.017
6    8   1.879   5.005   0.0 -45.626 -104.214  13.731
7    8   1.252 -55.060   0.0  17.273 -105.672  13.649
8    8   2.505   0.719   0.0 -42.579 -102.609  13.233
9    8   1.879  -3.758   0.0 -46.391 -104.879  12.858

   scan     rng     azi  elev    dopl     magn     snr
0    9  11.580   0.408   0.0   9.990  -68.457  42.966
1    9  17.455   0.417   0.0  19.962  -76.715  33.663
2    9  23.561   0.408   0.0   9.990  -82.775  26.790
3    9  23.796   0.355   0.0  29.952  -88.591  20.977
4    9   2.505 -63.473   0.0 -49.948 -101.713  13.579
5    9   1.879 -63.597   0.0 -43.941 -102.743  13.417
6    9   1.879  -3.393   0.0 -15.367 -103.211  13.258
7    9   1.879   5.022   0.0 -45.643 -104.232  12.907
8    9   1.252   1.012   0.0  27.603 -104.726  12.656
9    9   2.505   0.719   0.0 -56.262 -102.927  12.385

   scan     rng    azi  elev    dopl     magn     snr
0   10  11.330  0.408   0.0   9.990  -68.803  43.251
1   10  17.465  0.391   0.0  19.962  -77.187  33.803
2   10  23.561  0.400   0.0  10.007  -82.423  27.728
3   10  23.512  0.373   0.0  29.952  -86.404  23.804
4   10   3.131 -3.438   0.0  32.556 -101.391  13.591
5   10   1.879  0.586   0.0  44.656 -103.232  13.408
6   10   3.131  0.994   0.0 -19.230 -101.414  13.366
7   10   3.131  5.031   0.0 -13.427 -102.184  13.309
8   10   2.505  9.462   0.0 -32.011 -105.027  13.083
9   10   2.505 -3.260   0.0 -50.255 -103.151  12.799

   scan     rng     azi  elev    dopl     magn     snr
0   11  11.320   0.400   0.0   9.990  -68.965  43.391
1   11  17.445   0.400   0.0  19.979  -77.384  33.993
2   11  23.570   0.453   0.0  10.007  -82.790  27.604
3   11  23.531   0.346   0.0  29.952  -87.364  23.098
4   11   1.879  -3.402   0.0 -15.367 -102.081  15.017
5   11   4.383 -42.305   0.0 -45.370 -104.700  13.734
6   11   3.493  -3.776   0.0 -29.288 -101.963  13.376
7   11   2.505 -55.904   0.0  24.880 -103.769  13.168
8   11   3.757  -3.482   0.0 -30.326 -101.522  13.072
9   11   3.757  -3.749   0.0 -43.668 -101.955  13.027

   scan     rng     azi  elev    dopl     magn     snr
0   12  11.580   0.408   0.0   9.990  -68.514  43.034
1   12  17.455   0.400   0.0  19.962  -77.163  33.211
2   12  23.551   0.435   0.0   9.990  -82.071  27.389
3   12  23.580   0.479   0.0  29.952  -85.932  23.497
4   12  29.431   0.364   0.0  19.877  -89.253  19.757
5   12   1.879  -3.331   0.0 -15.367 -102.883  14.055
6   12   2.505   9.381   0.0 -32.011 -104.539  13.893
7   12   1.252 -55.044   0.0  17.273 -105.578  13.575
8   12   2.505 -55.716   0.0 -44.928 -103.615  12.998
9   12   2.505 -64.112   0.0  46.357 -102.536  12.792

   scan     rng     azi  elev    dopl     magn     snr
0   13  11.320   0.400   0.0   9.990  -68.801  43.367
1   13  17.465   0.408   0.0  19.962  -77.273  33.771
2   13  23.570   0.453   0.0   9.990  -83.265  26.945
3   13  23.796   0.417   0.0  29.952  -88.475  21.736
4   13  29.431   0.400   0.0  19.877  -88.924  20.688
5   13   3.131  -3.749   0.0 -29.254 -101.288  14.393
6   13   3.757  -3.438   0.0 -30.326 -100.209  13.966
7   13   1.879  -3.402   0.0 -15.333 -102.934  13.899
8   13   2.813 -64.092   0.0 -49.982 -101.686  13.842
9   13   2.505   0.692   0.0 -56.245 -102.971  13.159

   scan     rng     azi  elev    dopl     magn     snr
0   14  11.330   0.408   0.0   9.990  -68.961  43.100
1   14  17.445   0.400   0.0  19.962  -77.295  33.809
2   14  23.551   0.382   0.0   9.990  -82.823  27.436
3   14  23.796   0.435   0.0  29.952  -89.178  21.013
4   14   3.757  -3.598   0.0 -30.377  -99.081  15.714
5   14   3.757 -42.583   0.0 -30.411 -104.999  14.306
6   14   2.505   4.960   0.0  51.088 -103.074  13.495
7   14   3.513  -3.438   0.0 -29.407 -101.551  13.309
8   14   2.505 -64.236   0.0  46.374 -102.537  13.285
9   14   3.131   0.906   0.0 -19.230 -101.928  13.206

   scan     rng     azi  elev    dopl     magn     snr
0   15  11.320   0.400   0.0   9.990  -68.687  43.288
1   15  17.445   0.400   0.0  19.962  -77.188  33.734
2   15  23.796   0.453   0.0   9.990  -83.220  26.543
3   15  23.561   0.355   0.0  29.952  -87.420  22.542
4   15  29.431   0.373   0.0  19.877  -90.069  19.363
5   15   1.879  -3.287   0.0 -15.367 -102.956  14.225
6   15   3.757  -3.633   0.0 -30.343 -100.968  13.542
7   15   2.505   0.684   0.0 -42.562 -102.537  13.413
8   15   3.503  -3.527   0.0 -29.356 -101.299  13.340
9   15   2.505 -64.257   0.0  46.289 -102.984  12.931

   scan     rng     azi  elev    dopl     magn     snr
0   16  11.330   0.400   0.0   9.990  -69.074  42.919
1   16  17.455   0.408   0.0  19.962  -77.342  33.542
2   16  23.570   0.391   0.0   9.990  -82.899  27.172
3   16  23.512   0.426   0.0  29.952  -87.689  22.391
4   16   4.012  -3.678   0.0 -30.377  -99.954  14.557
5   16   5.010  -3.536   0.0  44.060  -99.810  14.108
6   16   3.757 -42.571   0.0 -30.616 -105.274  13.561
7   16   2.505 -64.215   0.0  46.374 -102.160  13.476
8   16   5.636  -3.544   0.0 -33.066 -100.607  13.475
9   16   3.131  -3.491   0.0  32.573 -101.759  13.430

   scan     rng     azi  elev    dopl     magn     snr
0   17  11.330   0.400   0.0   9.990  -69.160  42.817
1   17  17.455   0.391   0.0  19.962  -77.589  33.287
2   17  23.551   0.382   0.0   9.990  -83.099  26.942
3   17  23.512   0.373   0.0  29.952  -87.761  22.299
4   17   4.012  -3.660   0.0 -30.377  -99.429  15.299
5   17   5.636 -55.185   0.0  11.811 -100.472  14.255
6   17   5.636   0.639   0.0  52.705  -99.730  14.105
7   17   3.757 -42.510   0.0 -30.411 -104.733  14.096
8   17   5.010  -3.447   0.0  44.060  -99.998  13.976
9   17   1.879   0.932   0.0 -29.595 -103.342  13.697

   scan     rng     azi  elev    dopl     magn     snr
0   18  11.330   0.408   0.0   9.990  -68.853  43.170
1   18  17.455   0.408   0.0  19.962  -77.128  33.730
2   18  23.561   0.373   0.0  10.007  -82.972  27.193
3   18  23.796   0.373   0.0  29.952  -88.831  21.385
4   18   4.002  -3.616   0.0 -30.377  -99.047  15.384
5   18   3.757 -42.388   0.0 -30.411 -104.391  14.347
6   18   2.505 -63.989   0.0 -49.982 -102.229  13.543
7   18   4.383  -3.740   0.0 -45.285 -100.720  13.511
8   18   4.383 -64.195   0.0 -27.433 -100.432  13.371
9   18   4.383 -42.281   0.0 -45.319 -104.876  13.329

   scan     rng     azi  elev    dopl     magn     snr
0   19  11.320   0.400   0.0   9.990  -69.129  42.912
1   19  17.455   0.391   0.0  19.962  -77.723  33.359
2   19  23.561   0.426   0.0  10.007  -82.729  27.415
3   19  23.561   0.408   0.0  29.952  -86.605  23.551
4   19  29.431   0.293   0.0  19.877  -89.798  19.923
5   19   5.636 -55.107   0.0  11.828  -99.878  14.895
6   19   4.031  -3.464   0.0 -30.377  -99.929  14.197
7   19   5.205   4.826   0.0  54.339 -100.288  14.141
8   19   3.532  -3.571   0.0 -29.339 -100.827  14.007
9   19   5.636   0.755   0.0  52.671  -99.608  13.983

    
                                                      ASSIGNMENT 2
    
Q3)Write a program to compute mean(reference), maximum and minimum voltage for each rail from the capture logs. The diag output will give the reference values for each rail(0-5). Compare this reference value with the reference value from the capture log and report PASS if values approximately match.


from statistics import mean

with open("/home/fousiai/Downloads/capture_10mslog.txt",'r') as fin:
    file_data = fin.read()
    fin.close()
with open("/home/fousiai/Downloads/diag_vm_poll_100ms(1)log.txt",'r') as fin:
    file2_data = fin.read()
    fin.close()
rail0=[]
rail1=[]
rail2=[]
rail3=[]
rail4=[]
rail5=[] 
for x in file_data.split('\n')[1:]:
    d = x.split()  
    if d == []:
        continue    
    elif d[1] == 'voltage' and d[3]=='[0]':
        rail0.append( float( d[-1])) 
    elif d[1] == 'voltage' and d[3]=='[1]':
        rail1.append( float( d[-1])) 
    elif d[1] == 'voltage' and d[3]=='[2]':
        rail2.append( float( d[-1]))    
    elif d[1] == 'voltage' and d[3]=='[3]':
        rail3.append( float( d[-1]))  
    elif d[1] == 'voltage' and d[3]=='[4]':
        rail4.append( float( d[-1])) 
    elif d[1] == 'voltage' and d[3]=='[5]':
        rail5.append( float( d[-1]))         
reference_volt = []

for x in file2_data.split('\n')[1:]:
    d = x.split()
    if d == []:
        continue
       
    elif d[1] == 'voltage':
        reference_volt.append( float( d[-1]))

# mean of each rail
b=[rail0,rail1,rail2,rail3,rail4,rail5]  #group of list
mean_list=[]
for i in b:
    c = mean(i)
    mean_list.append(c)

# pass or fail check
check = []
for i in range(6):
    if (round(mean_list[i])==round( reference_volt[i])):
        check.append('Pass')
    else:
        check.append('Fail')

# printing 
print('Mean of rail0=',mean_list[0],'\n','min of rail0=',min( rail0),'\n','max of rail0=',max( rail0),'\n',check[0],'\n')
print('Mean of rail1=',mean_list[1],'\n','min of rail1=',min( rail1),'\n','max of rail1=',max( rail1),'\n',check[1],'\n')
print('Mean of rail2=',mean_list[2],'\n','min of rail2=',min( rail2),'\n','max of rail2=',max( rail2),'\n',check[2],'\n')
print('Mean of rail3=',mean_list[3],'\n','min of rail3=',min( rail3),'\n','max of rail3=',max( rail3),'\n',check[3],'\n')
print('Mean of rail4=',mean_list[4],'\n','min of rail4=',min( rail4),'\n','max of rail4=',max( rail4),'\n',check[4],'\n')
print('Mean of rail5=',mean_list[5],'\n','min of rail5=',min( rail5),'\n','max of rail5=',max( rail5),'\n',check[5],'\n')

#output

Mean of rail0= 1.8258545614438064 
 min of rail0= 1.825072 
 max of rail0= 1.828548 
 Pass 

Mean of rail1= 1.1481795662018048 
 min of rail1= 1.147289 
 max of rail1= 1.150092 
 Pass 

Mean of rail2= 0.8898042688207315 
 min of rail2= 0.889111 
 max of rail2= 0.892021 
 Pass 

Mean of rail3= 1.0897530705264884 
 min of rail3= 1.089012 
 max of rail3= 1.092064 
 Pass 

Mean of rail4= 1.7811104887649665 
 min of rail4= 1.780269 
 max of rail4= 1.784172 
 Pass 

Mean of rail5= 3.1792896719698214 
 min of rail5= 3.173745 
 max of rail5= 3.190249 
 Fail 
    
                                                        ASSIGNMENT 3
    
 Q4)Write a program using class to display the actual target and ghost target for each scan from the list of top 10 moving detections. To identify if a target is a ghost target,


import pandas as pd
def get_detections( detection):

  with open("/home/fousiai/Downloads/replay-det_VP160.txt",'r') as file:
    data = file.readlines()
    file.close()
  value = []
  for line in data:
    if "Skipped" in line:
      break  
    x = line.find('SS')
    if x == -1:
        list_of_words = line.split()
        if "Scan sequence" in line:
          seq_no=list_of_words[2].replace(',', '')
          if seq_no != "0":
            detection.append(value)
            value = []
          continue
         
        else :
          value.append( [
            seq_no,
            float(list_of_words[1]),
            float(list_of_words[3]),
            float(list_of_words[5]),
            float(list_of_words[7]),
            float(list_of_words[9]),
            float(list_of_words[11]) #snr
          ])
  detection.append(value)
  return detection
 
def max_snr(detection,k):

  for scan in detection:
    details = pd.DataFrame(scan,columns = ['scan','rng','azi','elev','dopl','magn','snr'])
    rslt_pd = details.sort_values(by = 'snr',ascending = 0,ignore_index = 1)
    print("\n",rslt_pd.iloc[ :k])
    
    
def find_target( detection):
    target = 11.46
    scn=0
    for scan in detection:
        print( "Scan", scn)
        scn+=1
        ghost_target = []
        for i in scan:
            if  (target <= i[1] < target+2):
                ghost_target.append( i)
        ghost_target.sort(key=lambda a:a[1])
        if ghost_target == []:
            print( "No target and ghost target found")
            continue
        
        Target = ghost_target.pop(0)

        actualGhost = []
        for i in ghost_target:
            if round(i[4]) == -round(Target[4]):
                actualGhost.append( i)
                
        print("Targets")
        details = pd.DataFrame([Target],columns = ['scan','rng','azi','elev','dopl','magn','snr'])
        print("\n",details.iloc[ :1])
        
        if actualGhost == []:
            continue
            
        print("\nGhost targets")
        details = pd.DataFrame(actualGhost,columns = ['scan','rng','azi','elev','dopl','magn','snr'])
        rslt_pd = details.sort_values(by = 'snr',ascending = 0,ignore_index = 1)
        print("\n",rslt_pd.iloc[ :10])       
detection=[]      
get_detections(detection)  
find_target( detection)

#output

Scan 0
Targets

   scan     rng     azi  elev   dopl     magn     snr
0    0  11.467 -63.349   0.0  10.16 -100.396  10.007

Ghost targets

   scan     rng     azi  elev    dopl    magn     snr
0    0  11.580   2.042   0.0  -9.990 -62.363  46.466
1    0  11.898  -2.842   0.0 -10.075 -98.140  11.208
2    0  11.898  59.062   0.0 -10.075 -98.970  10.294
Scan 1
No target and ghost target found
Scan 2
No target and ghost target found
Scan 3
No target and ghost target found
Scan 4
No target and ghost target found
Scan 5
No target and ghost target found
Scan 6
No target and ghost target found
Scan 7
No target and ghost target found
Scan 8
No target and ghost target found
Scan 9
Targets

   scan    rng    azi  elev  dopl    magn     snr
0    9  11.58  0.408   0.0  9.99 -68.457  42.966
Scan 10
No target and ghost target found
Scan 11
No target and ghost target found
Scan 12
Targets

   scan    rng    azi  elev  dopl    magn     snr
0   12  11.58  0.408   0.0  9.99 -68.514  43.034
Scan 13
No target and ghost target found
Scan 14
No target and ghost target found
Scan 15
No target and ghost target found
Scan 16
No target and ghost target found
Scan 17
No target and ghost target found
Scan 18
No target and ghost target found
Scan 19
No target and ghost target found












