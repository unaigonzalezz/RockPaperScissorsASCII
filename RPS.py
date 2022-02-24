import random
import time


randomnum = random.randrange(0, 3)
choosepc = ""
print ("""                                                                                                                       
 _____ _____ _____ _____      _____ _____ _____ _____ _____    _____ _____ ____     _____ _____ _____ _____ _____ _____ _____ _____ 
| __  |     |     |  |  |    |  _  |  _  |  _  |   __| __  |  |  _  |   | |    \   |   __|     |     |   __|   __|     | __  |   __|
|    -|  |  |   --|    -|_   |   __|     |   __|   __|    -|  |     | | | |  |  |  |__   |   --|-   -|__   |__   |  |  |    -|__   |
|__|__|_____|_____|__|__| |  |__|  |__|__|__|  |_____|__|__|  |__|__|_|___|____/   |_____|_____|_____|_____|_____|_____|__|__|_____|
                        |_|                                                                                                         
                                                                                                                                 
""")
time.sleep(1)
print(""" by:

  _   _           _    ___               __ _        
 | | | |_ _  __ _(_)  / __|___ _ _  ____/_/| |___ ___
 | |_| | ' \/ _` | | | (_ / _ \ ' \|_ / _` | / -_)_ /
  \___/|_||_\__,_|_|  \___\___/_||_/__\__,_|_\___/__|

                                                     
@unaiitxuu
""")
time.sleep(1)

while True:
	rockASCII ='''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
	'''
		
	paperASCII ='''  
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
	'''
	scissorsASCII = '''  
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
	'''  
	win =("""
  _______
 |       |
(| Winner|)
 |  #1   |
  \     /
   `---'
   _|_|_ """)

	loose = ("(✖╭╮✖)")

	print ("1 (Rock):", rockASCII)
	print ("2 (Paper):", paperASCII)
	print ("3 (Scissors):", scissorsASCII)

	election = int(input("Choose one for starting the game: "))
	while True:
		try:
			if 0 < election < 4:
				break;

			else:
				print("That's not a valid option! Choose again")
				exit()

		except ValueError():
				print("Sorry, I didn't understand that.")

	if election == 1 :
		print ("You choosed Rock:")
		print (rockASCII)
		userchoose = "Rock"

	elif election ==  2 :
		print ("You choosed Paper:")
		print (paperASCII)
		userchoose = "Paper"

	elif election == 3: 
		print ("You choosed Scissors:")
		print (scissorsASCII)
		userchoose = "Scissors"

	if randomnum == 0:
		choosepc = "Rock"
		pc = rockASCII

	if randomnum == 1:
		choosepc = "Paper"
		pc = paperASCII

	if randomnum == 2:
		choosepc = "Scissors"
		pc = scissorsASCII

	print ("The computer has chosen:", choosepc)
	print( pc)
	print("")

	if choosepc == "Rock" and userchoose == "Paper":
		print ("You won the game! Paper wraps up Rock :)")
		print (win)
		print ("")
	elif choosepc == "Rock" and userchoose == "Scissors":
		print ("You lost the game! Scissors has been smashed by Rock :(")
		print (loose)
		print ("")
	elif choosepc == "Paper" and userchoose == "Rock":
		print("You lost the game! Rock destroys Paper :(")
		print (loose)
		print ("")
	elif choosepc == "Paper" and userchoose == "Scissors":
		print("You won the game! Scissors cut the Paper :)")
		print (win)
		print ("")
	elif choosepc == "Scissors" and userchoose == "Rock":
		print("You won the game! Rock smash the Scissors :)")
		print (win)
		print ("")
	elif choosepc == userchoose:
		print("That's a tie! UwU")
		print ("")

	print("1.Yes =D")
	print("2.No, exit the program =(")
	print("")
	final =  int(input("Do you want another match?"))
	print(final)

	if final == 1:
		continue
	if final == 2:
		exit()