import sys
"""
this is my first python3 code test
"""
def print_loop(datas,indent=False,tabcount=0, fh=sys.stdout):
	for item in datas:
		if isinstance(item,list):
			print_loop(item,indent,tabcount+1, fh)
		else:
			if indent:
				for step in range(tabcount):
					print("\t",end='',file = fh)
			print(item, file = fh)