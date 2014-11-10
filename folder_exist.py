import sys, os
 
def main():
	usage = """
	You should pass at least 1 argument to %d
	Arguments are folders full path separed by space.
	""" % sys.argv[0]
	
	argv = sys.argv[1:]
	
	#if not arguments passed
	if not argv:
		#do some code
	
	for option in argv:
		exist = "folder exist"
		#do some code here to check string is path
		if os.path.exist(option):
			exist = "folder doesn't exist"
		output.append([option, exist])
 
	for i, folder, exist in enumerate(output):
		print "%r. %s\t [%s]" % i+1, folder, exist
 
if __name__ == '__main__':
	main()
