def get_usage(): 
with open("/home/fousiai/Downloads/DDR_Usage_log.txt", 'r') as file: #reads the file 
data = file.readlines() 
file.close() 
values = {} 
usageDict = {} 
ref = {} 
for line in data: 
if "available memory" in line: 
line = line.replace('(', ' ').replace(')', ' ')
 list_of_words = line.split() 
 usage = float(list_of_words[10]) * 100 / (float(list_of_words[5]) + float(list_of_words[10])) #given equation 
 values[list_of_words[1]] = usage
 if ("python command" in line) and ("capture" in line): #identify presets 
 list_of_words = line.split() 
 if "--preset" in line: 
 presets = list_of_words[5] 
 elif "mukna" in line:
 presets = 'mukna' 
 else: 
 presets = "atlas"
 usageDict[presets] = values
 for val in values: 
 ref[val] = {} 
 values = {} 
 for pres in usageDict: 
 for usage in usageDict[pres]: 
 ref[usage][pres] = usageDict[pres][usage] 
  return ref
 def show_usage_error(usage): #identify error 
 for section in usage: 
 error = False error_dict = {} 
 for preset in usage[section]: 
 if (usage[section][preset] > 70): 
 error = True 
 error_dict[preset] = usage[section][preset] 
 if (error == True):
 print("JENKINS_ERROR: memory usage for " + section + " is >70% for") #printing 
 for err in error_dict:
 print("usage for " + err + " is " + str(error_dict[err]) + " %") 
 else: 
 print("JENKINS_OK: memory for " + section + " is within the limit for all types of scans") 
 usage = get_usage() 
 show_usage_error(usage) 
 #output 
 JENKINS_OK: memory for RHAL_DRAM is within the limit for all types of scans 
 JENKINS_OK: memory for RDC_DRAM is within the limit for all types of scans 
 JENKINS_OK: memory for TFS_MEM is within the limit for all types of scans 
 JENKINS_OK: memory for RHAL_RDC1 is within the limit for all types of scans
  JENKINS_OK: memory for RHAL_DCU_ECC is within the limit for all types of scans 
  JENKINS_ERROR: memory usage for RHAL_DCU is >70% for 
  usage for CP101 is 70.08066585412791 % 
  usage for VP114U is 94.23231124510873 % 
  usage for mukna is 82.65363397267303 % 
  usage for atlas is 78.25630252100841 % 
  JENKINS_ERROR: memory usage for USER_SRAM is >70% for 
  usage for CP101 is 78.5506750982738 % 
  usage for VP112 is 78.5506750982738 % 
  usage for VP114U is 78.5506750982738 % 
  usage for mukna is 78.5506750982738 % 
  usage for atlas is 78.5506750982738 % 
  JENKINS_ERROR: memory usage for USER_SRAM_UNCACHED is >70% for 
  usage for CP101 is 86.9140625 % 
  usage for VP112 is 86.9140625 % 
  usage for VP114U is 86.9140625 % 
  usage for mukna is 86.9140625 % 
  usage for atlas is 86.9140625 % 
  JENKINS_OK: memory for SCP_TCMA is within the limit for all types of scans 
  JENKINS_OK: memory for SCP_TCMB is within the limit for all types of scans 
  JENKINS_OK: memory for ACP_DRAM is within the limit for all types of scans 
  JENKINS_OK: memory for ACP_TCMA is within the limit for all types of scans 
  JENKINS_OK: memory for ACP_TCMB is within the limit for all types of scans
