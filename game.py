#!/usr/bin/python
from system import Game, Player
	
class SmallTown(Game):
	def __init__(self, player):
		self.player = player	
		self.talked_to_cornwall = False
		
		print "Welcome to Small Town!"
		print "The smallest town in the entire game."
	
	def entrance(self, silent=False):
		if not silent:
			print "%s, You are standing at the main gate" % self.player.name
			print "In front of you is a wooden sign."
		
		command = self.command("look at sign", "go north")
		
		if command == "look at sign":
			print "The sign reads..."
			print "You enjoy pastry, as do I. Let's all fly."
			self.entrance(True)

		elif command == "go north":
			self.town_center()
	
	def town_center(self, silent=False):
		if not silent:
			print "On your EAST is BBO McGee's fine dining"
		
			if not self.talked_to_cornwall:
				print "On your WEST is a house, you can't really see what it is. It appears to be a house."
			else:
				print "On your WEST is CORNWALL's house, he enjoys lemon tarts and red lolly."
		
		command = self.command("go south", "go west", "go east")
		
		if command == "go south":
			self.entrance()
			
		elif command == "go west":
			print "You knock on the door. *knock* *knock*"
			if not self.talked_to_cornwall:
				print "A hilarious looking man answers the door"
				print "CORNWALL: HI I AM CORNWALL. WHY U KNOCK ON DOOR?"
			else:
				print "CORNWALL: HI AGAIN, I LIKE U, BYE"
				print "CORNWALL closes his door."
				print "He seems to have dropped a small OBJECT"
				self.cornwall_object()
				
			self.cornwall_house()
			
		elif command == "go east":
			#print "Nothing happens over here yet"
			print "This place hasn't been programmed yet."
			self.town_center(True)

	def cornwall_house(self):
		command = self.command("talk to cornwall", "go east")
		
		if command == "talk to cornwall":
			
			if self.talked_to_cornwall:
				print "CORNWALL is gone"
			else:
				print "CORNWALL: I LIKE LEMON TARTS AND RED LOLLY"
				print "The door slams shut."
				self.talked_to_cornwall = True
			
			self.cornwall_house()
			
		elif command == "go east":
			print "You walk east.."
			self.town_center()
	
	def cornwall_object(self):
		command = self.command("look at object", "pick up amulet", "pick up object")
		
		if command == "look at object":				
			print "You do a hand stand to get a better view."
			print "It appears to be an AMULET"
			print "Something is written on it, you try to read it..."
			print "It says:"
			print "Bob's AMULET"
			print "You feel the overpowering urge to posses the AMULET, You feel you *must* have it!"
			self.cornwall_object()
			
		elif command == "pick up object":
			print "You are hesitant and decide you need a closer look"
			self.cornwall_object()
				
		elif command == "pick up amulet":
			print "You pick up the AMULET"
			print "The game is won, You found the AMULET!"
			
			
			#self.add_inventory("AMULET")

class Beginning(Game):
	def __init__(self):
		print "Greetings adventurer!\n"
		self.player = Player(raw_input("And by what name shall you be known?: "))
		#NAME = raw_input("And by what name shall you be known?: ")
		self.introduction()
		
	def introduction(self):
		print "Greetings %s!" % self.player.name
		print "You are standing on a narrow path surrounded by thick shrubs and tall trees."
		print "The path runs NORTH."
		
		command = self.command("go north")

		if command == "go north":
			print "You are greeted by the sight of a small township"
			SmallTown(self.player).entrance()


Beginning()

