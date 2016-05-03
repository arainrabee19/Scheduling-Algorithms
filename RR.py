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
#no of p_timees
def NoOfp_time():
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
		arr['name']=raw_input ("p_time Name : ")
		arr['arrival']=input ("A.Time : ")
		arr['burst']=input ("B.Time : ")
		dictionary.append(arr)
		no1 = no1+1
	return


def RR(num,dictionary,Slice,IO):
	Clear()
	P_no = num
	print ("SHORT JOB FIRST SERVE ALGORITHUM IS RUNNING")
	wait = []
	total = 0
	temp = None
	from operator import itemgetter
	dictionary.sort(key = itemgetter('arrive'))

	while(P_no):
		if((len(dictionary) != 0) or (temp != None)):
			if(temp == None):
				temp = dictionary[0]
				temp['burst'] = Slice
				del dictionary[0]
			total = total + 1
			temp['burst'] = temp['burst'] - 1
			temp['p_time'] = temp['p_time'] - 1
			if(temp['p_time'] == 0):
				print ("%s Turn Around Time is : %d And its Waiting time is : %d" % (temp['name'],total,total-temp['arrive'])
				P_no = P_no - 1
				if(len(dictionary) != 0):
					temp = dictionary[0]
				else:
					temp = None
			elif(temp['burst'] == 0):
				temp['wait'] = total + IO
				wait += [temp]
				temp = None

		if(len(wait) != 0):
			wait.sort(key = itemgetter('wait'))
			if(wait[0]['wait'] <= total):
				dictionary += [wait[0]]
				del wait[0]
			elif(P_no):
				print (P_no)
				total  = total + 1
	
	print ("SJF ENDS")

	
GetNumber()

dictionary = []
GetInput(num,dictionary)
SLICE = input("Enter Time Slice : ")
IO = input("Enter I/O burst Time : ")

RR(num,dictionary,SLICE,IO)
