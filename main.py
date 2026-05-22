import CLImode
import GUImode


def main():
	print("CodeAlpha Python Network Sniffer\n")

	command_line_interface = "1"
	graphical_user_interface = "2"
	user_input = input(
		"Please choose an interface:\n"
		" 1 - Command Line Interface\n"
		" 2 - Graphical User Interface\n"
	).strip()

	if user_input == command_line_interface:
		print("You chose Command Line Interface mode\n")
		CLImode.CommandLinterface()
	elif user_input == graphical_user_interface:
		print("You chose Graphical User Interface mode\n")
		GUImode.GraphicalUinterface()
	else:
		print("Invalid input, please try again later")


if __name__ == "__main__":
	main()
	