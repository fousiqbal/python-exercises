# Write a program to get the list of top 10 moving detections with maximum SNR for each scan.(flags parameter is empty for moving detections)

with open("/home/fousiai/Downloads/replay-det_VP160.txt",'r') as file:  #read the file

    snr_value =[] 
    t = []

    for line in file:
#         print(line)
        x = line.find('SS')  #to remove ss 
#         print(x)
        if x ==-1:
            list_of_words = line.split()
            if( len( list_of_words) < 10):   #seperate the first 2 lines
                snr_value.append( t)
                t = []
                continue
            t.append( [
                float(list_of_words[1]),  #rng
                float(list_of_words[3]),  #azi
                float(list_of_words[5]),  #elev
                float(list_of_words[7]),  #dopl
                float(list_of_words[9]),  #magn
                float(list_of_words[11])  #snr
            ])
                
def pf( i):
    a,b,c,d,e,f = [],[],[],[],[],[]
    for v in snr_value[i][ :10]:  #get 10 values
        a.append( v[0])
        b.append( v[1])
        c.append( v[2])
        d.append( v[3])
        e.append( v[4])
        f.append( v[5])
    print( "\nScan",i," Rng", a)  #printing
    print( "Scan",i, " Azi", b)
    print( "Scan",i," Elev", c)
    print( "Scan",i, " Dopl", d)
    print( "Scan",i," Magn", e)
    print( "Scan",i, " SNR", f)
    

for i in range( 1, 20):
    snr_value[i].sort(reverse=1, key=lambda a: a[5])  #sort in descending order
    pf( i)
