import sys

class Game():
	def __init__(self, player):
		self.player = player

	def command(self, *args, **kwargs):
		self.valid = False
		
		while self.valid == False:
			if kwargs.get('text'):
				input = raw_input("\n%s " % kwargs.get('text'))
			else:
				input = raw_input("\n> ")
		
			for arg in args:
				if arg == input:
					self.valid = True
					
			# handle reserved commands
			if not self.valid:
				self.__system(input)
		
		return input

	def __system(self, input):
		s = input.split()
		
		if input == "help":
			print "  GO <DIRECTION>"
			print "  LOOK AT <OBJECT>"
			print "  PICK UP <OBJECT>"
			print "  TALK TO <WHO>"
			print "  SAVE"
			
		elif input == "go north":
			print "You can't move north"
		
		elif input == "go south":
			print "You can't move south"
		
		elif input == "go east":
			print "You can't move east"
		
		elif input == "go west":
			print "You can't move west"
			
		elif " ".join(s[0:2]) == "look at" and len(s) == 2:
			print "Look at what?"
			
		elif " ".join(s[0:2]) == "look at" and len(s) >= 3:
			print "I can't see %s" % " ".join(s[2:])
			
		elif " ".join(s[0:2]) == "talk to" and len(s) == 2:
			print "Talk to who?"
			
		elif " ".join(s[0:2]) == "talk to" and len(s) >= 3:
			print "I can't talk to %s" % " ".join(s[2:])
			
		elif " ".join(s[0:2]) == "pick up" and len(s) == 2:
			print "Pick up what?"
			
		elif " ".join(s[0:2]) == "pick up" and len(s) >= 3:
			print "I can't pick up %s" % " ".join(s[2:])
		
		elif input == "save":
			print "Saving... (Not really)"
			
		elif input == "quit" or input == "exit":
			print "Goodbye, %s" % self.player.name
			sys.exit()
			
		else:
			print "Unknown command '%s'" % input


class Player:
	def __init__(self, name):
		self.name = name
		self.inventory = {}

	def add_item(self, item):
		self.inventory
