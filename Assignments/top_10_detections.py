

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
