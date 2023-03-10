# def get_usage():
#     with open(
#         "/home/fousiai/Downloads/DDR_Usage_log.txt", "r"
#     ) as file:  # reads the file
#         data = file.readlines()
#         file.close()
#     values = {}
#     usageDict = {}
#     ref = {}

#     for line in data:
#         if "available memory" in line:
#             line = line.replace("(", " ").replace(")", " ")
#             list_of_words = line.split()
#             usage = (
#                 float(list_of_words[10])
#                 * 100
#                 / (float(list_of_words[5]) + float(list_of_words[10]))  # given equation
#             )
#             values[list_of_words[1]] = usage

#         elif ("python command" in line) and ("capture" in line):  # identify presets
#             list_of_words = line.split()
#             if "--preset" in line:
#                 presets = list_of_words[5]
#             elif "mukna" in line:
#                 presets = "mukna"
#             else:
#                 presets = "atlas"
#             usageDict[presets] = values
#             for val in values:
#                 ref[val] = {}
#             values = {}
#     for pres in usageDict:
#         for usage in usageDict[pres]:
#             ref[usage][pres] = usageDict[pres][usage]
#     return ref


# def show_usage_error(usage):  # identify error
#     for section in usage:
#         error = False
#         error_dict = {}
#         for preset in usage[section]:
#             if usage[section][preset] > 70:
#                 error = True
#                 error_dict[preset] = usage[section][preset]
#         if error == True:
#             print(f"JENKINS_ERROR: memory usage for {section} is >70% for")  # printing
#             for err in error_dict:
#                 print(f"usage for {err} is {str(error_dict[err])} %")

#         else:
#             print(
#                 f"JENKINS_OK: memory for {section} is within the limit for all types of scans"
#             )


# usage = get_usage()
# show_usage_error(usage)
import argparse, sys
parser = argparse.ArgumentParser()
parser.add_argument("--duration", help = "simulation time in seconds")
parser.add_argument("--sensor-data", help = "The path to file containing sensor data")
args = parser.parse_args()
print(f"Args: {args}\nCommand Line: {sys.argv}\nsensor-data: {args.sensor-data}")
print(f"Dict format: {vars(args)}")