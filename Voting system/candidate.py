'''
The purpose of this python script is to create a candidate database. 

The code works on a menu-based system which has option to:
		Add a candidate (after checking their age and criminal rocord)
		Change details (Name and home address) of a particular candidate
		Display the details of a particular candidate
		Display the entire candidate's list
		Remove a candidate from the list
		
The details of these candidates are stored using a nested dictionary with the main key value being their unique candidateID.
'''

import colorama
from colorama import Fore		#Used to make the fonts coloured
import time						#Used to pause the code for better readability in terminal

#The start function is called in the main file and is used to create and alter the candidate's database
def start():
	def checkcandidate(candidate, temp, age, year):
	#This function is used to check if the entered details of a new candidate are valid (age [>=18] and aadhar number [unique for each person] and no criminal records)
		flag = -1		#if flag==-1, the candidate details are valid
		candidateid = 'ID' + str(temp)
		for x in dict_can:
			if candidate['Aadhar number'] == dict_can[x]['Aadhar number']:			
				flag += 1

		if (year - int(candidate['Year of birth']) >= age) and (flag == -1):		#checking age and aadhar number	
			dict_can[candidateid] = candidate
			print(Fore.GREEN +"Data saved successfully!")		#Confirmation message
			temp += 1
		else:
			print(Fore.RED + "Invalid details. Please check the entered Aadhar number and Year of Birth.")		#Invalid details message
		return temp



	def newcandidate(temp,age,year):
	#This function is used to input details of a new candidate from the user [finally stored in a nested dictionary]
		name = input("Enter full name: ")
		aadhar_no = input("Enter aadhar number: ")
		dob = input("Enter year of birth: ")
		address = input("Enter home address: ")
		criminalrcd = input("Do you have a criminal record? (Yes/No): ")
		if criminalrcd == 'no' or criminalrcd == 'No':
			candidate = {'Name':name,'Aadhar number':aadhar_no,'Year of birth':dob,'Address':address}
			newtemp = checkcandidate(candidate,temp,age,year)
			return newtemp
		elif criminalrcd == 'yes' or criminalrcd == 'Yes':		#asking to check non-existence of any criminal records
			print(Fore.RED + "Sorry. You are not eligible")
			return temp
		else:
			print(Fore.RED + "Invalid input. Please try again.")
			return temp


	def removecandidate():
	#This function is used to remove a candidate from the database on specifying a valid candidateID by the user
		removeid = input("Enter the candidateid of the person to be removed: ").upper()
		flag =- 1
		for x in dict_can:
			if removeid == x:
				del dict_can[x]
				print(Fore.GREEN + "Voter details successfully removed")		#Confirmation message
				return dict_can
				flag = 0
		if flag ==- 1:
			print(Fore.RED + "The candidateid does not exist in database. Contact helpdesk.")			#Invalid candidateID message



	def changecandidate():
	#This function is used to change the 'Name' and 'Address' of a particular candidate's details (on specifying a valid candidateID)
		changeid=input("Enter the candidateid of the person whose details are to be changed: ").upper()
		flag=-1
		for x in dict_can:
			if changeid==x:
				name=input("Enter full name: ")
				address=input("Enter home address: ")
				dict_can[x]['Name']=name
				dict_can[x]['Address']=address
				flag=0
				print("The new candidate details for this ID are: ",dict_can[x])
		if flag==-1:
			print(Fore.RED +"The candidateid does not exist in database. Contact helpdesk.")			#Invalid candidateID message



	def displaycandidate():
	#This function is used to display the details of a particular candidate on specifying a valid candidateID
		did=input("Enter candidate ID of the person whose details are needed: ").upper()
		try:
			print("The required details are: ")
			print(dict_can[did])
		except:
			print(Fore.RED +"The candidate ID doesn't exist in database. Contact helpdesk.")



	def displayall():
	#This function is used to display the entire database
		for x in dict_can:
			print(x,'-',end=' ')
			print(dict_can[x])



	dict_can={}
	temp=1


	print("*******************************")
	year=int(input("Enter the year in which elections are to be conducted: "))
	age=int(input("Enter minimum age criteria of candidates: "))
	while True:
		time.sleep(0.6)
		print(Fore.BLACK +'Menu:')
		print(Fore.BLACK +"Enter 1 to add new candidate to the list")
		print(Fore.BLACK +"Enter 2 to change details of a particular candidate")
		print(Fore.BLACK +"Enter 3 to display a particular candidate details")
		print(Fore.BLACK +"Enter 4 to display entire candidate's list")
		print(Fore.BLACK +"Enter 5 to remove a candidate")
		print(Fore.BLACK +"Enter 6 to exit")
		option=input()
		#We shall use try and except since if the user enters a non-int option the code will show an error
		try:
			if int(option)==1:
				temp=newcandidate(temp,age,year)
			elif int(option)==2:
				changecandidate()
			elif int(option)==3:
				displaycandidate()
			elif int(option)==4:
				displayall()
			elif int(option)==5:
				removecandidate()
			elif int(option)==6:
				print("*******************************")
				return dict_can
				break
		except:
			print(Fore.RED +"Invalid input. Please try again.")





