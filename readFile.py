import os

'''
使用if判断
'''
print("first read ------- ")
data = open("sketch.txt")
for word in data :
	if not word.find(":") == -1:
	    (role,line_word) = word.split(":", 1)
	    print(role, end = "")
	    print(" said ", end = "")
	    print(line_word,end = "")
data.close()

'''
使用try except异常捕捉
'''
print("\nsecond read ------- ")
data = open("sketch.txt")
for word in data :
	try:
	    (role,line_word) = word.split(":", 1)
	    print(role, end = "")
	    print(" said ", end = "")
	    print(line_word,end = "")
	except ValueError:
		pass
data.close()

print("\nthird read ------- ")
if os.path.exists("zhangtao.txt"):
	data = open("zhangtao.txt")
	for word in data :
		if not word.find(":") == -1:
			(role,line_word) = word.split(":", 1)
			print(role, end = "")
			print(" said ", end = "")
			print(line_word,end = "")
	data.close()

print("\nfour read ------- ")
try:
	data = open("zhangtao.txt")
	for word in data :
		try:
			(role,line_word) = word.split(":", 1)
			print(role, end = "")
			print(" said ", end = "")
			print(line_word,end = "")
		except ValueError:
			pass
	data.close()
except IOError:
	print("file is missing !")
