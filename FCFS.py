# Scheduling-Algorithms
#Clear function
def Clear():
	import os
	os.system('clear')
	return
#screen display function	
def FCFS():
	Clear()
	print("First Come First Serve ")
	return raw_input()
#no of processes
def NoOfProcess():
	Clear()
	print("number Of Job(s): ")
	return input()
	
#dictionary items
def Input(no,dictionary):
	Clear()
	no1 = 0
	P_no = 0
	
	while (no1 < no):
		arr = {}
		arr['name']=raw_input ("Process Name : ")
		arr['arrival']=input ("A.Time : ")
		arr['burst']=input ("B.Time : ")
		dictionary.append(arr)
		no1 = no1+1
	return


def FCFS(no,dictionary):

	Clear()
	print ("Algo processing")
	total = 0
	P_no = 0
	
	from operator import itemgetter
	dictionary.sort(key = itemgetter('arrival'))
	while(P_no < no):
		if P_no == 0:
			total = total + dictionary[P_no]['arrival'] + dictionary[P_no]['burst']
		elif dictionary[P_no]['arrival'] < total:
			total = total + dictionary[P_no]['burst']
		else:
			total = dictionary[P_no]['arrival']  + dictionary[P_no]['burst']
			
		print ("%s Takes %d seconds to complete." % (dictionary[P_no]['name'],total))
		P_no = P_no+1	
	print ("FCFS ENDS \n ")

    

no = NoOfProcess()

dictionary = []
Input(no,dictionary)
FCFS(no,dictionary)
