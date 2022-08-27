'''
The purpose of this python script is to create a voter database. 

The code works on a menu-based system which has option to:
		Add a voter (after checking their age and ensuring that he/she has a unique aadhar number)
		Change details (Name and home address) of a particular voter
		Display the details of a particular voter
		Display the entire voter's list
		Remove a voter from the list
		
The details of these voters are stored using a nested dictionary with the main key value being their unique voterID.
'''

import colorama
from colorama import Fore		#Used to make the fonts coloured
import time						#Used to pause the code for better readability in terminal

#The start function is called in the main file and is used to create and alter the voter's database
def start():
	def checkvoter(voter, temp):
	#This function is used to check if the entered details of a new voter are valid (age [>=18] and aadhar number [unique for each person])
		flag =- 1	#if flag==-1, the voter details are valid
		voterid = 'ID' + str(temp)
		for x in dict:
			if voter['Aadhar number'] == dict[x]['Aadhar number']:
				flag+=1

		if (n-int(voter['Year of birth']) >= 18) and (flag == -1):		#checking age and aadhar number
			dict[voterid] = voter
			print(Fore.GREEN + "Data saved successfully!")	#Confirmation message
			temp += 1
		else:
			print(Fore.RED + "Invalid details. Please check the entered Aadhar number and Year of Birth.")	#Invalid details message
		return temp



	def newvoter(temp):
	#This function is used to input details of a new voter from the user [finally stored in a nested dictionary]
		name = input("Enter full name: ")
		aadhar_no = input("Enter aadhar number: ")
		dob = input("Enter year of birth: ")
		address = input("Enter home address: ")
		voter = {'Name':name,'Aadhar number':aadhar_no,'Year of birth':dob,'Address':address}
		newtemp = checkvoter(voter,temp)
		return newtemp



	def removevoter():
	#This function is used to remove a voter from the database on specifying a valid voterID by the user
		removeid = input("Enter the voterid of the person to be removed: ").upper()
		flag = -1
		for x in dict:
			if removeid == x:
				del dict[x]
				print(Fore.GREEN + "Voter details successfully removed")		#Confirmation message
				return dict
				flag = 0
		if flag == -1:
			print(Fore.RED + "The voterid does not exist in database. Contact helpdesk.")		#Invalid voterID message



	def changevoter():
	#This function is used to change the 'Name' and 'Address' of a particular voter's details
		changeid = input("Enter the voterid of the person whose details are to be changed: ").upper()
		flag = -1		#to check if the voterID exists in database
		for x in dict:
			if changeid == x:
				name = input("Enter full name: ")
				address = input("Enter home address: ")
				dict[x]['Name'] = name
				dict[x]['Address'] = address
				flag = 0
				print("The new voter details for this ID are: ")
				print(dict[x])
		if flag == -1:
			print(Fore.RED + "The voterid does not exist in database. Contact helpdesk.")		#Invalid voterID message



	def displayvoter():
	#This function is used to display the details of a particular voter on specifying a valid voterID
		did = input("Enter voter ID of the person whose details are needed: ").upper()
		try:
			print("The required details are: ")
			print(dict[did])
		except:
			print(Fore.RED + "The voter ID doesn't exist in database. Contact helpdesk.")



	def displayall():
	#This function is used to display the entire database
		for x in dict:
			print(x,'-',end='')
			print(dict[x])



	dict = {}
	temp = 1


	print("*******************************")
	n = int(input("Enter the year in which elections are to be conducted: "))
	while True:
		time.sleep(0.6)
		print(Fore.BLACK + 'Menu:')
		print(Fore.BLACK + "Enter 1 to add new voters to the list")
		print(Fore.BLACK + "Enter 2 to change details of a particular voter")
		print(Fore.BLACK + "Enter 3 to display a particular voter details")
		print(Fore.BLACK + "Enter 4 to display entire voter's list")
		print(Fore.BLACK + "Enter 5 to remove a voter")
		print(Fore.BLACK + "Enter 6 to exit")
		option=input()
		#We shall use try and except since if the user enters a non-int option the code will show an error
		try:
			if int(option) == 1:
				temp = newvoter(temp)
			elif int(option) == 2:
				changevoter()
			elif int(option) == 3:
				displayvoter()
			elif int(option) == 4:
				displayall()
			elif int(option) == 5:
				removevoter()
			elif int(option) == 6:
				print("*******************************")
				return dict
				break
		except:
			print(Fore.RED + "Invalid input. Please try again.")






