import os
import myloopprint
import pickle
man = []
other = []
try:
	data = open("sketch.txt")
	for word in data :
		try:
			(role,line_word) = word.split(":", 1)
			line_word = line_word.strip()
			if role == 'Man':
				man.append(line_word)
			elif role == 'Other Man':
				other.append(line_word)
		except ValueError:
			pass
	data.close()
except IOError:
	myloopprint.print_loop("file is missing !")
print(man)
print(other)

try:
	newdata = open("zhangtao.txt","w")
	myloopprint.print_loop(["zhangtao nihao "],fh = newdata)
except IOError:
	print("file error")
finally:
	newdata.close()

try:
	ztf = open("afasd.txt")
	myloopprint.print_loop(ztf)
except IOError as e:
	print("file error:" + str(e))
finally:
	if "ztf" in locals():
		ztf.close()

try:
	with open("man.txt","w") as mans,open("other.txt","w") as others:
		myloopprint.print_loop(man, fh = mans)
		myloopprint.print_loop(other, fh = others)
except IOError as e:
	print("file error:" + str(e))

try:
	with open("afasd.txt","wb") as bfile: 
		pickle.dump([1,2,3,4,5,'fsdf','zhangtao'],bfile)
except IOError as ioError:
	print("file error :" + str(ioError))

try:
	with open("afasd.txt","rb") as storefile:
		filedata = pickle.load(storefile)
		print(filedata)
except IOError as ioError:
	print("file error :" + str(ioError))
