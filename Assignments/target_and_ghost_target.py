#Write a program using class to display the actual target and ghost target for each scan from the list of top 10 moving detections. To identify if a target is a ghost target


import pandas as pd
def get_detections( detection):

  with open("/home/fousiai/Downloads/replay-det_VP160.txt",'r') as file:  #read the file
    data = file.readlines()
    file.close()
  value = []
  for line in data:
    if "Skipped" in line:
      break  
    x = line.find('SS')  #to remove ss
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
            float(list_of_words[1]), #rng
            float(list_of_words[3]), #azi
            float(list_of_words[5]), #elev
            float(list_of_words[7]), #dopl
            float(list_of_words[9]), #magn
            float(list_of_words[11]) #snr
          ])
  detection.append(value)
  return detection
 
def max_snr(detection,k):  

  for scan in detection:
    details = pd.DataFrame(scan,columns = ['scan','rng','azi','elev','dopl','magn','snr'])
    rslt_pd = details.sort_values(by = 'snr',ascending = 0,ignore_index = 1)
    print("\n",rslt_pd.iloc[ :k])
    
    
def find_target( detection):  #target condition
    target = 11.46
    scn=0
    for scan in detection:
        print( "Scan", scn)
        scn+=1
        ghost_target = []
        for i in scan:
            if  (target <= i[1] < target+2):  #ghost target condition
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
