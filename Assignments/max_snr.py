# Write a program to get the list of top 10 moving detections with maximum SNR for each scan.(flags parameter is empty for moving detections)

  
    with open("/home/fousiai/Downloads/replay-det_VP160.txt",'r') as file:  #read the file
    value =[] 
    detection = []
    for line in file:
        x = line.find('SS') #to remove ss 
        if x ==-1:
            list_of_words = line.split()
            
            if( len( list_of_words) < 10):   #seperate the first 2 lines
                value.append( detection)
                detection = []

            else:
                detection.append( [
                    float(list_of_words[1]), #rng
                    float(list_of_words[3]), #azi
                    float(list_of_words[5]), #elev
                    float(list_of_words[7]), #dopl
                    float(list_of_words[9]),#magn
                    float(list_of_words[11]) #snr
                ])
                
def display_detection( i):
    rng,azi,elev,dopl,magn,snr = [],[],[],[],[],[]
    for v in value[i][ :10]:#get 10 values
        rng.append( v[0])
        azi.append( v[1])
        elev.append( v[2])
        dopl.append( v[3])
        magn.append( v[4])
        snr.append( v[5])
    print( "\nScan",i," Rng", rng)#printing
    print( "Scan",i, " Azi", azi)
    print( "Scan",i," Elev", elev)
    print( "Scan",i, " Dopl", dopl)
    print( "Scan",i," Magn", magn)
    print( "Scan",i, " SNR", snr)

def max_snr( a):
    return a[5]

for i in range( 1, 20):
    value[i].sort(reverse=1, key=max_snr) #lamda a:a[5]
    display_detection( i)
    
        
