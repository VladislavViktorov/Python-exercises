from entities import Character
from errors import InvalidCommand

class Menu:
    def print_menu(self):
        print("1. Create a new character")
        print("2. Create weapon of an already existing character")
        print("3. Create additional weapon of an already existing character")
        print("4. Delete all characters")
        print("5. Delete an existing character")
        print("6. Exit")

    def command_create_character(self, name, sex, ch_class):
        pass

    def run(self):
        # infinite menu loop
        while True:  
            # print the menu
            # ...

            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:
                # process the user's choice
                if choice == "1":                    
                    # ask the user to input the necessary command parameters
                    name = input("Enter the character name (alpha-numeric): ")
                    sex = input("Enter the sex of the character")
                    mainweapon = input("Enter the main weapon of the character")
                    additionalweapon = input("Enter the additional weapon of the character")
                    gameclass = input("Enter the class of the character")


                    # ...

                    # char = self.command_create_character(....)
                    
                    # ...
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
