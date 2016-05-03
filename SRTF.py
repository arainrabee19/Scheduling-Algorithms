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
		no1 += no1+1
	return

def SRTF(no,dictionary):
	print ("SRTF processing.....")
	total = 0
	P_no = no
	from operator import get
	dictionary.sort(key = get('arrival'))
	temp = dictionary[0]
	del dictionary[0]
	total = total + temp['arrival']
	P_no1 = 0
	while(P_no):	
		P_no2 = 0
		next_process= 0
		while(P_no2 < P_no-1):
				if( dictionary [next_process]['burst'] < temp['burst']):
					if(dictionary[next_process]['arrival'] <= total):
						dictionary += [temp]
						temp = dictionary[next_process]
						del dictionary[next_process]
					else:
						next_process = next_process + 1
				P_no2 = P_no2+1
			
		temp['burst'] = temp['burst']-1
		total = total + 1
		if(temp['burst'] == 0):
			print ("%s takes %d seconds to complete." % (temp['name'],total))
			if(P_no != 0):
				dictionary.sort(key = get('arrival'))
				temp = dictionary[0]
				del dictionary[0]
			P_no = P_no - 1 
	print ("SJF ENDS")

	
no = NoOfProcess()

dictionary = []
Input(no,dictionary)
SJF(no,dictionary)


	
