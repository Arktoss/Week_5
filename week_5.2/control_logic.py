char_name = input("What is your name: ").title()

def welcome_screen():
    if(char_name == "Ninja"):
        print("Hello Warrior ...")
    if (char_name == "Bob"):
        print("I bet you like to build things.")
    if(char_name != "Bob" and char_name != "Ninja" ):
        print("Hmmm... I don't think we've met.")
    if(char_name == "Bob" or char_name == "Ninja"):
        print("I figured one of you two would show up")

welcome_screen()
