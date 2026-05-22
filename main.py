import CLImode
import GUImode


print("CodeAlpha Python Network Sniffer\n")

commandLineInterface="1"
graphicalUserInterface="2"  
userInput=input("please choose an interface\n 1- Command_line_Interface\n 2- graphical_User_interface\n")


if  userInput==commandLineInterface:
	print("you choose Command_line_Interface mode\n")
	CLImode.CommandLinterface()

	
elif userInput==graphicalUserInterface:
	print("you choose graphical_User_interface mode\n")
	GUImode.GraphicalUinterface()
else:
	print("invalid input please try again later")
	