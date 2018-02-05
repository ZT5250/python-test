import io
'''
resolve time string 
'''
def sanitize(time_string):
	if ":" in time_string:
		splitter = ":"
	elif "-" in time_string:
		splitter = "-"
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins+","+secs)

'''
从文件中读取数据
'''
def get_coach_data(filename):
	try:
		with open(filename) as fileData:
			data = fileData.readline()
			return(data.strip().split(","))
	except IOError as ioerr:
		print('File error : '+str(ioerr))
		return(None)

james = get_coach_data("hfpy_ch5_data/james.txt")
julie = get_coach_data("hfpy_ch5_data/julie.txt")
mikey = get_coach_data("hfpy_ch5_data/mikey.txt")
sarah = get_coach_data("hfpy_ch5_data/sarah.txt")
print("------origin data----------")
print(james)
print(julie)
print(mikey)
print(sarah)
print("------sorted data----------")
sortJames = []
sortjulie = []
sortmikey = []
sortsarah = []
for time in james:
	sortJames.append(sanitize(time))
for time in julie:
	sortjulie.append(sanitize(time))
for time in mikey:
	sortmikey.append(sanitize(time))
for time in sarah:
	sortsarah.append(sanitize(time))
print(sorted(sortJames))
print(sorted(sortjulie))
print(sorted(sortmikey))
print(sorted(sortsarah))

print("------sorted data:使用推到列表方式----------")
sortJames2 = [sanitize(time) for time in james]
sortjulie2 = [sanitize(time) for time in julie]
sortmikey2 = [sanitize(time) for time in mikey]
sortsarah2 = [sanitize(time) for time in sarah]
print(sorted(sortJames2))
print(sorted(sortjulie2))
print(sorted(sortmikey2))
print(sorted(sortsarah2))
print("------sorted data:使用使用集合取出重复----------")
print(sorted(set([sanitize(time) for time in james]))[0:3])
print(sorted(set([sanitize(time) for time in julie]))[0:3])
print(sorted(set([sanitize(time) for time in mikey]))[0:3])
print(sorted(set([sanitize(time) for time in sarah]))[0:3])


sarahUpdate = get_coach_data("hfpy_ch6_data/sarah2.txt")
(sarah_name, sarah_dob) = sarahUpdate.pop(0), sarahUpdate.pop(0)
print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarahUpdate]))[0:3]))
