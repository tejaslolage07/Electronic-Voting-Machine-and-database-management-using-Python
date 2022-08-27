'''
This is the main code for the project. In this code, we import two more python files (used to make voters' and candidates' database).
Using this database, we will conduct voting and display results
'''
import colorama
from colorama import Fore
import voter
import candidate
import time
import matplotlib.pyplot as plt


#Creating a list of the the possible menu options
list_1 = ["Enter 1 to create voter's database", "Enter 2 to create candidate's database"]
list_2 = ['Enter 1 to add votes', 'Enter 2 to display result', 'Enter 3 to exit']



def addvote():
#This function is used to add a particular voter's vote (on specifying a valid voterID)
	who = input(Fore.BLACK +"Enter your voterID: ").upper()
	if who in vot:
		print(Fore.BLACK +"Please choose one of the following candidates (enter their candidateID): ")
		for x in candidates:
			print(x,"  ",candidates[x])
		ans = input().upper()
		if ans in can:
			candidates_votes[ans] += 1
			vot.remove(who)
			print(Fore.GREEN + "Your vote is saved. Thank you for your participation")	#confirmation message
		else:
			print(Fore.RED + "Not a valid candidateID. Please try again.")	#if an invalid candidate ID is enetered by the user
	else:
		print(Fore.RED + "VoterID not applicable. Please try again")		#if an invalid voter ID is enetered by the user



def result():
#This function stores the results in a text file and displays it. It also displays a histogram for the same
	
	results = open("Results.txt", mode = "a")

	val_max = 0
	
	for x in candidates:
	#Here, 'Results.txt' is the text file where the results are saved using the following code below
		results.write('CandidateID: ')
		results.write(x + '\n')
		results.write('      ')
		results.write(str(candidates[x]))
		results.write('\n' + '      ')
		results.write('Number of votes received: ')
		results.write(str(candidates_votes[x]))
		results.write("\n")
		if candidates_votes[x] > val_max:
			val_max = candidates_votes[x]		#Finding the maximum number of votes
	results.write('\n')
	results.write('\n')
	results.write("The winner(s) is(are): " + '\n')
	for x in candidates_votes:
		if candidates_votes[x] == val_max:		#Checking if the particular candidate recieved the maximum votes
			results.write(x)
			results.write('\n' + '     ')
			results.write(str(candidates[x]))
			results.write('\n' + '     ')
			results.write('Number of votes received: ')
			results.write(str(candidates_votes[x]))
			results.write('\n')
	results.close()
	results = open("Results.txt", mode = "r")
	text = results.read()
	print(text)
	results.close()
	time.sleep(3.5)
	#Histogram for the results
	plt.bar(list(candidates_votes.keys()), candidates_votes.values(), color = 'g')
	plt.show()



#This is the first menu aimed at creating the candidate and voter databases
print("*******************************")
while len(list_1) != 0:
	time.sleep(0.6)
	for ele in list_1:
		print(Fore.BLACK + ele)

	option = input()
	try:

		if int(option) == 1:
			voters = voter.start()
			list_1.remove("Enter 1 to create voter's database")
		elif int(option) == 2:
			candidates = candidate.start()
			list_1.remove("Enter 2 to create candidate's database")
		
	except:
		print(Fore.RED + "Not a valid input. Please try again.")




#Adding a 'None of the above' option to the list of candidates
x = len(candidates) + 1
new = 'ID' + str(x)
candidates[new] = ['None of the above']


#Creating a list of all the voterIDs. This is used while taking votes as once a voter votes, his/her ID will be removed from the list making him ineligible henceforth.
vot = []
for x in voters:
	vot.append(x)

#Here, we will create another dictionary to store candidate's votes against their IDs.
can = []
for x in candidates:
	can.append(x)
defaultValue = 0
candidates_votes = dict.fromkeys(can,defaultValue)



#Text files are created containing all the databases

#The voter's database text file
voterfile = open("Voters.txt", mode = "w")
voterfile.write("The voter details are: " + '\n')
for x in voters:
	voterfile.write('   ' + x + '   ' + str(voters[x]) + '\n')
voterfile.close()

#The candidate's database text file
candidatefile = open("Candidates.txt", mode = "w")
candidatefile.write("The candidate details are: " + '\n')
for x in candidates:
	candidatefile.write('   ' + x + '   ' + str(candidates[x]) + '\n')
candidatefile.close()

#A text file for storing the results
results = open("Results.txt", mode = "w")
results.write("The result of the election is: " + '\n')
results.write('\n')
results.close()

time.sleep(0.6)
print("The voter and candidate database text files are now saved. Please refer to those to check your voter/candidate IDs.")
time.sleep(0.6)

#This menu us used to conduct the voting process as well display results
while True:
	time.sleep(0.6)
	for ele in list_2:
		print(Fore.BLACK + ele)

	option = input()

	try:

		if int(option) == 1:
			addvote()
		
		elif int(option) == 2:
			result()
		
		elif int(option) == 3:
			print("*******************************")
			break
	except:
		print(Fore.RED + "Not a valid input. Please try again.")
#We have used try and except since the user might enter a non-integer input which will show an error


