import sys
import os
import time 
import random 
from colorama import init, Fore, Back, Style
from pathlib import Path
from ASCIIArt import *

# Changes the color after one colored line
init(autoreset=True) 

# Code to clear printed text, can be used to reset health 
# os.system('cls' if os.name == 'nt' else "printf '\033c'")

#For maps, or other text files: 
# f = open('example.txt', 'r')
# file_contents = f.read()
# print (file_contents)
#To close the file: 
# f.close()

#For colored text: 
#from colorama import init, Fore, Back, Style
#init()
#print(Fore.RED + 'some red text') 

#For sound files: 
#import simpleaudio as sa
#wave_obj = sa.WaveObject.from_wave_file("path/to/file.wav")
#play_obj = wave_obj.play()
#play_obj.wait_done()
#For the simpleaudio documentation: https://simpleaudio.readthedocs.io/en/latest/tutorial.html#playing-audio-directly

#IDEAS: 
# Maybe make a gold/store system? 
# Make it exploration based ? 
# Make a weapon inventory, access before fight to see damge of starting weapons
# Make running out of mana reduce damage instead of disable it
# Add an "animated" snake visual that changes on attack
# Create an inventory save for when people die in the fights
# Add color to the map, make maps into python files
# Have an ascii character of zao instead of just scrolling text 

def MainMenu(): 
	#Welcomes the player to the game 
	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	print(OpeningPlanet)
	# Have actual animations for when you land and zao is talking, make a function for this 
	print(GameTitle)
	print('A Text Based Exploration Combat Game') 
	#Gives the player options on what to pick
	gamestartoptions = (input('New Game(Type n)|Credits(Type c)|Quit Game(Type q) \n')) 
	#If statement deciding if the player wants to choose new game 
	if gamestartoptions == 'n':
		NewGame() 
	#If the player chooses to watch the credits 
	elif gamestartoptions == 'c':
		Credits() 
	#If the player decides to quit the game 
	elif gamestartoptions == 'q': 
		QuitDecision() 
	#If the player types in anything other than new game, credits, or quit game 
	elif gamestartoptions != 'n' or 'c' or 'q': 
		print('<Please type in a valid choice>') 
		MainMenu() 
		
def QuitDecision(): 
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		#Asks the player if they are sure they want to quit the game 
		quitdecision = (input('Are you sure you want to quit the game? (y/n) \n')) 
		if quitdecision == 'y':
			QuitGame() 
		elif quitdecision == 'n': 
				os.system('cls' if os.name == 'nt' else "printf '\033c'")
				MainMenu() 
		elif quitdecision != 'yes' or 'no': 
			print('<Please type in a valid choice>') 
			QuitDecision()

def NewGame(): 
	#Runs the game 
	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	GameCore()

def Credits(): 
	#Runs the credits 
	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	print('Programmed by Shane O\'Brien') 
	time.sleep(5) 
	print('Story by Shane O\'Brien') 
	time.sleep(5) 
	print('Designed by Shane O\'Brien \n') 
	time.sleep(5) 
	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	MainMenu() 

def QuitGame(): 
	#Quits the game 
	quit() 

##############################################################################

global test_time
test_time = 5

def OpenMap(MapName, status): 
	map_folder = Path("./Maps/") # Relative path
	MapName = map_folder / MapName
	f = open(MapName, 'r')
	if status == 'open': 
		file_contents = f.read()
		print(file_contents) 
	elif status == 'close': 
		f.close()

def printw(text):
	print(text)
	time.sleep(test_time)
	os.system('cls' if os.name == 'nt' else "printf '\033c'")

def ZaoDial(text): 
	print(Leader_Zao) 
	print(text)
	time.sleep(test_time)
	os.system('cls' if os.name == 'nt' else "printf '\033c'") # Text not printing out
	
#################################################################################

def GameCore(): 
	#Saying the backstory if the player chooses new game 
	#Create a save file here

	print(OpeningSpace)
	printw('The year is 2075') 
	
	print(OpeningSpace)
	printw('You were on a routine mission to resupply the base on Mars') 
	
	print(OpeningSpace)
	printw('You realize that you are veering off course')
	
	print(OpeningSpace)
	printw('As you were panicking, you accidentally go into warp speed') 

	print(OpenPlanet)
	printw('Warp speed stops and you arrive at an alien planet')
	
	print(OpenPlanet)
	printw('You land on the planet') 
	
	print(OpenPlanet)
	printw('Your instruments say that the air is breathable') 
	
	print(OpenPlanet)
	printw('You get out of the spaceship') 
	
	print(Knockout)
	printw('You are knocked out and taken somewhere')
	
	print(OpeningJail)
	printw('You wake up in a dark room') 
	
	print(OpeningJail)
	printw('There is only a little bit of light coming from under the door') 
	 
	#Player chooses characters name 
	print(OpeningJail)
	printw('You hear an alien voice') 
	 
	#Player name is defined 
	global playername 
	print(OpeningJail)
	print('Unknown Voice: What is your name?') 
	playername = (input('<Type in what you want your characters name to be>\n'))
	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	
	print(OpeningJail)
	printw('Unknown Voice: '+ playername + ', welcome to the planet Xivryn') 
	
	print(OpeningJail)
	printw('Unkown Voice: We appologize for knocking you out') 
	 
	print(OpeningJail)
	printw('Unkown Voice: We did not know if you were friendly or not \n') 
	time.sleep(2.5)
	 

	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	ZaoDial('Leader Zao: My name is Leader Zao of Loena') 
	
	ZaoDial('Leader Zao: The planet you are on is Xivryn')
	
	ZaoDial('Leader Zao: Welcome to my city, Loena')
	
	ZaoDial('Leader Zao: My people are called the Loens') 
	
	ZaoDial('Leader Zao: We are now going to release you') 
	
	ZaoDial('Leader Zao: Now we know our planet is not the same as Earth') 
	 
	ZaoDial('Leader Zao: We hope you see it as another home though') 
	 
	ZaoDial('Leader Zao: You are now released and you are free to go') 
	 
	ZaoDial('Leader Zao: But before you go there is something you must decide')
	 
	ZaoDial('Leader Zao: There are three different tomes') 
	 
	ZaoDial('Leader Zao: These different tomes will teach you how to survive') 
	 
	ZaoDial('Leader Zao: Not only in Loena, but also the entire planet of Xivryn')
	 

	playerflg=0
	while playerflg==0: 
		#Asks the player what class they want to be 
		ZaoDial('Leader Zao: The three tomes are: The Art of Stealth, The Art of Battle, and The Art of Sorcery') 

		global classdecision 
		print(Leader_Zao)
		print('Leader Zao: You must pick one of the three tomes to follow and use')
		classdecision=(input('<Type s for Stealth, b for Warrior, and m for Sorcerer> \n'))
		#The player chooses their class 
		if classdecision == 's': 
			print('<You are now following the path of the assassin>') 
			playerflg=1
		elif classdecision == 'b': 
			print('<You are now following the path of the warrior>')
			playerflg=1
		elif classdecision == 'm': 
			print('<You are now following the path of the sorcerer>') 
			playerflg=1
		else: 
			print('<Please type in a valid choice>') 
			playerflg=0

	 
	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	ZaoDial('You are now ready to explore Xivryn') 
	 
	ZaoDial('Leader Zao: However I must warn you of danger that lurks on Xivryn') 
	 
	ZaoDial('Leader Zao: The evil enemy of Loena and all of Xivryn') 
	 
	ZaoDial('Leader Zao: Him and his men will try to kill you') 
	 
	ZaoDial('Leader Zao: This man is named Xuth-Dire') 
	 
	ZaoDial('Leader Zao: His followers are called the Wolves') 
	 
	ZaoDial('Leader Zao: He and his men want to destroy Loena and rule all of Xivryn') 
	 
	ZaoDial('Leader Zao: You must help us fight off this evil enemy') 
	 
	ZaoDial('Leader Zao: Kill any Wolves you come across in your travels') 
	 
	ZaoDial('Leader Zao: Then maybe one day, we wll have the opportunity to kill Xuth-Dire himself') 
	 
	print(Leader_Zao)
	print('Leader Zao: Here is a potion of mana, to help you on your journey')
	printw('<1 Mana potion has been added to your inventory>')

	global Inventory 
	Inventory = {"Mana Potions:":1, "Scrip:":0} # Defines the potions and the players inventory 
	# Make a weapon list ?
	# To enable new weapons

	 
	ZaoDial('Leader Zao: In case you encounter some evil and need a boost') 
	 
	ZaoDial('Leader Zao: Remember, you need mana to make your attacks deal more damage')
	 
	ZaoDial('Leader Zao: If you try to attack with low mana, your attacks will be less effective') 
	
	ZaoDial('Leader Zao: Before you go, maybe you should get some rest') 
	 
	ZaoDial('Leader Zao: So you will be ready to start adventuring in the morning') 
	 
	print('You fall alseep') 
	time.sleep(1) 
	print('Z')
	time.sleep(1) 
	print('z')
	time.sleep(1) 
	print('Z')
	time.sleep(1) 
	print('z')
	time.sleep(1) 

	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	
	printw('You awaken and it is morning') 
	 
	ZaoDial('Leader Zao: Good, you are awake') 
	 
	ZaoDial('Leader Zao: Now go explore all of Xivryn') 
	 
	ZaoDial('Leader Zao: Also, remember to kill any of the Wolves you happen to come upon') 
	 
	ZaoDial('Leader Zao: Another thing, be careful of the beasts that roam Xivryn') 
	 
	ZaoDial('Leader Zao: Feel free to come back to Loena capital to visit anytime you want') 
	 

	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	printw('You leave the Capital of Loena and approach the vast Delta Forest') 
	 
	printw('As you are walking out of the gate you see something on the ground') 
	 

	if classdecision == 's': 
		printw('On the ground you see a knife') 
		
		printw("You pick it up")
		
		printw('You remember reading about it in the tome you read')
	elif classdecision == 'b': 
		 
		printw('On the ground you see a hatchet')
		
		printw('You pick it up') 
		
		printw('You remember reading about it in the tome you read')
	elif classdecision == 'm': 
		printw('You feel the tingle of electricity running through your veins') 
		
		printw('You remember this feeling being described in the tome you read')

	 
	printw('You hear something in the bushes, right as you are leaving Loena') 
	 
	printw('You go over to investigate') 
	 
	printw('A giant snake jumps out of the bushes') 
	 
	printw('The Snake: Who might you be?') 
	 
	printw(playername + ': My name is ' + playername) 
	 
	printw('The Snake: Well, ' + playername + ' this is my territory so leave and never return') 
	 
	printw(playername + ': You will have to make me') 
	time.sleep(2.5)
	 

	os.system('cls' if os.name == 'nt' else "printf '\033c'")
	# Snake battle sequence, make battle sequences a sepereate file? 


 ################################################################################################### 

 # Implement stamina system so there is no abuse of heavy weapons 
 # Make classes have benfits? 
 # Add a border to where the snake is
	def SnakeBattle(light_atck, heavy_atck): # Make save points with argumanets of functions storing important info

		snake_health = 100
		snake_light_dmg = 5
		snake_heavy_dmg = 10 

		player_health=100 
		player_light_dmg = 10
		player_heavy_dmg = 20 
		player_mana = 50

		if Inventory["Mana Potions:"] < 1: # If the player restarts the fight, this give them back the mana potion if they used it
			Inventory["Mana Potions:"] = Inventory["Mana Potions:"] + 1
		else: 
			pass

		snake_atk_list = [snake_light_dmg, snake_heavy_dmg] 
		player_atk_list = [player_light_dmg, player_heavy_dmg] # Make individual lists for each class, have the ability tp add more abilties/weapons to them 

		if classdecision == 's' or 'b' or 'm': # Stealth class fight sequence 
			snake_fight = 0
			while (snake_health > 0) and (player_health > 0):
				if player_health <= 0: # Breaks the loop if the snake gets the players health to be low enough 
					break
				print('############################################')
				print('Your health: ' + Style.BRIGHT + Fore.RED + str(player_health) + '/100' + ' HP') # Health stays at top of fight screen and just updates after each attack sequence 
				print('Your mana: ' + Style.BRIGHT + Fore.BLUE + str(player_mana) + '/50' + ' MN')
				print('The Snake\'s health: ' + Style.BRIGHT + Fore.RED + str(snake_health) + '/100' + ' HP')
				print('############################################')
				print("") 

				print(SnakeEnemy)

				if player_health == 100 and snake_health == 100: # Only prints on the first strike 
					print('You strike first!')
				player_off_flag = 0
				while player_off_flag == 0: 
					player_off_snake = (input('Do you use a light attack, heavy attack, a mana potion, or do you want to look in your inventory? (l/h/p/i) \n'))
					
					if player_off_snake == 'l': # Light attack 
						if player_mana < 5: 
								print('You do not have enough mana to perform this attack!')
								player_off_flag = 0
						elif player_mana >= 5: 
							print(light_atck) 
							snake_health=snake_health-player_light_dmg
							player_mana = player_mana-5
							time.sleep(2)
							player_off_flag = 1

					elif player_off_snake == 'h': # Heavy attack
						if player_mana < 15: 
							print('You do not have enough mana to perform this attack!')
							player_off_flag = 0
						elif player_mana >= 15: 
							print(heavy_atck) 
							snake_health=snake_health-player_heavy_dmg 
							player_mana = player_mana-15
							time.sleep(2) 
							player_off_flag = 1
					
					elif player_off_snake == 'i': # Opening inventory 
						print('Your inventory:') # Make into a function, clear screen when open
						print("Mana Potions: " + str(Inventory["Mana Potions:"]))
						print('')
						player_off_flag = 0
					
					elif player_off_snake == 'p': # Using Potions, make potions get used up, make it check if a potion is there
						if (player_mana != 50): 
							if (player_mana < 50) and (player_mana >=30) and (Inventory["Mana Potions:"]==1): 
								player_mana = 50 
								print('Mana restored to max!')
								time.sleep(2)
								Inventory["Mana Potions:"]=Inventory["Mana Potions:"]-1
								player_off_flag = 1
							elif (player_mana < 30) and (Inventory["Mana Potions:"]==1): 
								player_mana = player_mana + 20 # Mana potions restore 20
								print('20 Mana restored!') 
								time.sleep(2) 
								Inventory["Mana Potions:"]=Inventory["Mana Potions:"]-1
								player_off_flag = 1
							elif Inventory["Mana Potions:"]==0: 
								print('Out of mana potions! \n')
								player_off_flag = 0
						elif (player_mana == 50) and (Inventory["Mana Potions:"]==1): 
							if Inventory["Mana Potions:"] == 0: 
								print('Out of mana potions! \n')
								player_off_flag = 0
							print('Mana full! \n')
							player_off_flag = 0
					
					else: 
						print('Your strike misses, giving the snake an opportunity to strike')
						time.sleep(2) 
						break # Breaks the player attack loop

				snake_rand_atk = random.choice(snake_atk_list) # Defines the snakes attack for the round, randomizes on each interation 
				print("") 

				if snake_health <= 0: # Checks the snakes health before going to his attack
					break 
				os.system('cls' if os.name == 'nt' else "printf '\033c'")
				print('############################################')
				print('Your health: ' + Style.BRIGHT + Fore.RED + str(player_health) + '/100' + ' HP') 
				print('Your mana: ' + Style.BRIGHT + Fore.BLUE + str(player_mana) + '/50' + ' MN')
				print('The Snake\'s health: ' + Style.BRIGHT + Fore.RED + str(snake_health) + '/100' + ' HP')
				print('############################################')
				print("")

				print(SnakeEnemy)


				if snake_rand_atk == snake_light_dmg:
					print('The snake strikes at you! You lose 5HP') 
					player_health=player_health-snake_light_dmg 
					time.sleep(2)
					os.system('cls' if os.name == 'nt' else "printf '\033c'")
					pass 
				elif snake_rand_atk == snake_heavy_dmg:
					print('The snake strikes at you and latches on, injecting some venom! You lose 10 HP') 
					player_health=player_health-snake_heavy_dmg 
					time.sleep(2)
					os.system('cls' if os.name == 'nt' else "printf '\033c'")
					pass


			if player_health <= 0: 
				print('You are defeated!') # Make defeat screen into a function ?
				print('  ________                        ________                    ._.') 
				print(' /  _____/_____    _____   ____   \_____  \___  __ ___________| | ')
				print('/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \ | ')
				print('\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/\| ')
				print(' \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|   ')
				print('        \/     \/      \/     \/          \/          \/       \/')
				snake_quit_flag=0
				while snake_quit_flag == 0:
					snake_quit=(input('Would you like to restart the battle or quit to main menu? (r/q) \n'))
					if snake_quit == 'r': 
						snake_quit_flag = 1
						if classdecision == 's': 
							os.system('cls' if os.name == 'nt' else "printf '\033c'")
							SnakeBattle('You slash with your knife! The snake loses 10HP', 'You stab your blade! The snake loses 20HP')
						elif classdecision == 'b': 
							os.system('cls' if os.name == 'nt' else "printf '\033c'")
							SnakeBattle('You swing your hatchet! The snake loses 10HP', 'You swing bring your hatchet down with all of your might! The snake loses 20HP')
						elif classdecision == 'm': 
							os.system('cls' if os.name == 'nt' else "printf '\033c'")
							SnakeBattle('You zap him with lightning! The snake loses 10HP', 'You use all of your strength to shoot a ball of lightning! The snake loses 20HP')
					elif snake_quit == 'q': 
						snake_quit_decis_flg = 0
						while snake_quit_decis_flg == 0: 
							os.system('cls' if os.name == 'nt' else "printf '\033c'")
							snake_quit_decis = (input('Are you sure you want to quit to main menu and lose progress? (y/n) \n'))
							if snake_quit_decis == 'y': 
								snake_quit_flag = 1
								os.system('cls' if os.name == 'nt' else "printf '\033c'")
								MainMenu()
							elif snake_quit_decis == 'n': 
								os.system('cls' if os.name == 'nt' else "printf '\033c'")
								snake_quit_flag = 0
							else:
								print('Invalid input! \n') 
								snake_quit_decis_flg = 0
					else: 
						print('Invalid input! \n')
						snake_quit_flag = 0


			if snake_health <= 0:
				print("""
____   ____.__        __                       ._.
\   \ /   /|__| _____/  |_  ___________ ___.__.| |
 \   Y   / |  |/ ___\   __\/  _ \_  __ <   |  || |
  \     /  |  \  \___|  | (  <_> )  | \/\___  | \|
   \___/   |__|\___  >__|  \____/|__|   / ____| __
                   \/                   \/      \/""") 
				time.sleep(2)
				os.system('cls' if os.name == 'nt' else "printf '\033c'")

##############################################################################################

# Make guardians of each reason, snake being the one for the Delta Forest
# Comment out fights to test

	if classdecision == 's': 
		SnakeBattle('You slash with your knife! The snake loses 10HP', 'You stab your blade! The snake loses 20HP')
		pass
	elif classdecision == 'b': 
		SnakeBattle('You swing your hatchet! The snake loses 10HP', 'You swing bring your hatchet down with all of your might! The snake loses 20HP')
		pass
	elif classdecision == 'm': 
		SnakeBattle('You zap him with lightning! The snake loses 10HP', 'You use all of your strength to shoot a ball of lightning! The snake loses 20HP')
		pass

	printw('You rest for a minute to recover, looking at your fallen foe')
	printw('After your fight, you run back to Loena, out of breath and scared') 
	 
	printw('As sweat runs down your cheek, you approach the gates of Loena')
	
	printw('A crowd comes to meet you, you notice how worried and how relieved they look') 
	time.sleep(2.5)
	
	os.system('cls' if os.name == 'nt' else "printf '\033c'")

	
	printw('Leader Zao: You have vannquished the snake that blocked our path to the Delta Forest!')
	
	printw('Leader Zao: Thank you for your kind service to Loena!')
	 
	printw('Leader Zao: For your service, here is a mana potion and a handsome reward in scrip, the currency here in Loena') 
	printw('<1 Mana potion added to inventory, 200 Scrip added to inventory>') 

	Inventory["Gold:"]=200
	Inventory["Mana Potions:"]=Inventory["Mana Potions:"]+1

	
	printw('Leader Zao: Thank you once again traveler!')
	 
	printw('Leader Zao: Before you get on your way again, there is one thing I must give you')
	 
	printw('Leader Zao: Here is a map of all of Xivryn')
	printw('<Press m to access the map when adventuring>') 
	
	printw('Leader Zao: Now that you have vanquished the Snake outside of our city, the road should be clear')
	
	printw('Leader Zao: Feel free to go and explore anywhere you want to go, our world may be little, but it has a lot to explore!') 
	
	printw('Leader Zao: Also, feel free to return to Loena at any point in time to spend your Scrip on new weapons and training!') 
	 
	mapflg = 0
	while mapflg == 0: 
		map_decis=(input('<Press m to look at the map and decide where to go next> \n')) # Make seperate files for each region
		if map_decis == 'm': 
			mapflg = 1
			
			os.system('cls' if os.name == 'nt' else "printf '\033c'")
			mapopenflg1 = 0
			while mapopenflg1 == 0: 
				OpenMap('WorldMap.txt', 'open')
				close_map = (input('<Press enter to close the map> \n')) 
				if close_map == "": 
					os.system('cls' if os.name == 'nt' else "printf '\033c'")
					mapopenflg1 = 1 
					OpenMap('WorldMap.txt', 'close')
				else: 
					print('Invalid input! \n')
					mapopenflg1 = 0
		else: 
			print('Invalid Input \n')
			mapflg = 0 
		
	print('Map printed successfully')
	print('Game ran successfully')
	time.sleep(5)