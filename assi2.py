#Write a program to compute mean(reference), maximum and minimum voltage for each rail from the capture logs. The diag output will give the reference values for each rail(0-5). Compare this reference value with the reference value from the capture log and report PASS if values approximately match.


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
