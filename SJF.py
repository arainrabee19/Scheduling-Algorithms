#Clear function
def Clear():
	import os
	os.system('clear')
	return
#screen display function	
def SJF():
	Clear()
	print("Shortest Job First ")
	return raw_input()
#no of processes
def NoOfProcess():
	Clear()
	print("nober Of Job(s): ")
	return input()
	
#dictionary items
def Input(no,dictionary):
	Clear()
	no1 = 0
	P_no = 0
	
	while(no1 < no):
		arr = {}
		arr['name']=raw_input ("Process Name : ")
		arr['arrival']=input ("A.Time : ")
		arr['burst']=input ("B.Time : ")
		dictionary.append(arr)
		no1 = no1+1
	return

def SJF(no,dictionary):
	print ("SHORT JOB FIRST SERVE ALGORITHUM IS RUNNING")
	total = 0
	P_no = 0
	from operator import get
	dictionary.sort(key = get('burst'))
	while(P_no < no):
		if P_no == 0:
			total = total + dictionary[P_no]['arrival'] + dictionary[P_no]['burst']
		else:
			total = total + dictionary[P_no]['burst']
		print ("%s takes %d seconds to complete." % (dictionary[P_no]['name'],total))
		P_no = P_no+1
	print ("SJF ENDS \n")

no = NoOfProcess()

dictionary = []
Input(no,dictionary)
SJF(no,dictionary)


	
