#Write a program to get the list of top 10 moving detections with maximum SNR for each scan.(flags parameter is empty for moving detections)


def get_detections( ):

    with open("/home/fousiai/Downloads/replay-det_VP160.txt",'r') as file:
        data = file.readlines()
        file.close()
     
    value = [] 
    detection = []  

    for line in data:
        if "Skipped" in line:
            continue
        #print(line)
        
        x = line.find('SS')
        if x == -1:
            list_of_words = line.split() 

            if "Scan sequence" in line:
               # print("debug3")
                value.append( detection)
                print("value: ",value)
                detection = []
            else:
                print(list_of_words)
                detection.append( [ 
                    float(list_of_words[1]),
                    float(list_of_words[3]),
                    float(list_of_words[5]),
                    float(list_of_words[7]),
                    float(list_of_words[9]),
                    float(list_of_words[11]) #snr
                ])              
            #return value, detection
            #print(value) 
                
def display_detection( i):
    
    rng,azi,elev,dopl,magn,snr = [],[],[],[],[],[]
    for v in value[i][ :10]:
        rng.append( v[0])
        azi.append( v[1])
        elev.append( v[2])
        dopl.append( v[3])
        magn.append( v[4])
        snr.append( v[5])
    #print( "\nScan",i," Rng", rng)
    #print( "Scan",i, " Azi", azi)
    #print( "Scan",i," Elev", elev)
    #print( "Scan",i, " Dopl", dopl)
    #print( "Scan",i," Magn", magn)
    print( "Scan",i, " SNR", snr)
def max_snr( a):
    return a[5]

def main():  
    value,detection = get_detections()
    #print(value,detection)
    #print("debug1")
    for i in range( 1, 20):
      #  print("debug2")

        value[i].sort(reverse=1, key=max_snr) #lamda a:a[5]  
        display_detection( i)  

        
main()
