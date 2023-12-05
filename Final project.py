#Aditya Chunduru
#00335780
#Final Project
#CIS 153 L8
#Program description: An expanded entertainment menu with a bit more fun activities to do. 
import pyjokes 
import re 
#file variables
joke_file_path = "jokes.md"
character_file_path = "favorite_character.md"
game_file_path = "favorite_game.md"
movie_file_path = "favorite_movie.md"
random_jokes = "random_jokes.md"

def joke_file_read(joke_file_path):   
    joke_dict = {} #initializes an empty dictionary to store the jokes
    with open(joke_file_path, "r") as file:
        for line in file: #iterates over each line in the file
            parts = line.strip().split(":")#whitespaces are stripped from the line and then splitted into a list of strings using the colon which stores the result in parts.
            if len(parts) >= 2:#checks if there are 2 elements in the parts list
                key = int(parts[0])#conversion of the first element of parts into an int which is assigned to the key variable. 
                value = parts[1].strip()# The Second element removes whitespace and is assigned to value.
                joke_dict[key] = f"{key}: {value}" #added entry to the dictionary

            else: 
                print(f"invalid line format in {joke_file_path}: {line}") #activates if the line doesn't have two parts.

    return joke_dict

    



joke_dict = joke_file_read(joke_file_path) #function call assigned to joke dict.


def tell_joke(random_jokes): 
    with open(random_jokes, 'a') as file: 
        random_joke = pyjokes.get_joke(language="en", category="all")

        file.write(random_joke + "\n")

        print(random_joke)



def add_joke(): 
    print("1. NASA related joke")
    print("2. Dog jokes")
    print("3. Dinsosaur jokes ")
    print("4. Lawyer jokes")
    print("5. Miscellaneous jokes")
    print("6. exit joke menu")
    try:
        user_input = input("Select a category for the joke (1-6) or press exit to go back to main menu: ")
        

        if user_input.lower() == 6:
            print("Exiting menu")
            return
        
        #\b matches any word boundary such as spaces, dashes, commas, semicolons and more ensures that the 1-5 isn't part of a larger number.
        # [1-5] is a character class matching any single digit from 1 to 5. the digit at this position must be one of these digits.
        if not re.match(r"\b[1-6]\b",user_input):
            print("Invalid input. Enter a valid value between 1 and 6")

        category = int(user_input)

        

        if category not in range (1, 7): 
            print("Unexpected input, enter a value between 1 and 6.")
            return #exiting function if invalid input is detected
        
       
        new_joke = input("Enter a new joke: ")


        with open(joke_file_path, "a") as file: 
            file.write(f"{category}: {new_joke}\n")
    except ValueError: 
        print("Invalid input. Enter a valid value for category")
        

def show_joke_file(joke_file_path):
    with open (joke_file_path, "r") as file: 
        for line in file: 
            print(line.strip())
    
    







def favorite_thing():
    topics = ["Favorite character","Favorite Movie", "Favorite Game"]
       
    

    try: 
        print("0. exit to main program")
        print("1. Favorite character")
        print("2. Favorite Movie")
        print("3. Favorite Game")
        topic_choice = int(input("Choose a topic between 1 and 3.\n "))
       

        favorite_thing_dict = {

            1: favorite_character_analysis,
            2: favorite_movie_analysis,
            3: favorite_game_analysis
        }

        if topic_choice == 0:
            print("returning to the main menu")
            return

        if topic_choice in favorite_thing_dict:
            #favorite_thing_dict[topic_choice]() accesses a function from the favorite_thing_dict using topic_choice as the key before calling the function.
            print(f"You chose {topics[topic_choice - 1]}")#topic_choice 1 retrives the corresponding topic from the list
            favorite_thing_dict[topic_choice]()
        else:
            print("You shall not pass.")
            return
    except ValueError:
        print("Seriously! nice try. You really thought you could get away with entering anything other than a number")
     


def favorite_character_analysis(): 
        character_info = {}
        with open(character_file_path, 'r') as file:
                for line in file: 
                    try:
                        key, value = map(str.strip, line.split(':', 1))
                        character_info[key] = f"{key}: {value}"
                    except ValueError:
                        print(f"Skipping line: {line.strip()}. Expected format: 'key: value' ")
                        continue
            # creates dictionary from key-value pairs. whitespace removed from the lines and splits the line
            # when colon first occurs. the 1 is to ensure that at least one split is performed which makes a list of two elements. 
            # the key and the value(before and after colon)


        while True:
                try:
                    character = input("Welcome to favorite character analysis. Enter your favorite character or enter exit:\n ")

                    if character == "exit":
                        print("exiting...")
                        return

           
            
           



                    if character in character_info: 
                        print(character_info[character.lower()])
                    else: 
                        print("character not in file.")
                
                    addition_status = input(f"Do you want to add character for:{character}? press y to continue: ")

                    if addition_status.lower() == "y": 
                        character_description = input("Enter description: ")

                        character_info[character] = f"{character}: {character_description}"

                        with open(character_file_path, "a") as file:
                            file.write('\n' + character + ': ' + character_description )
                        print("Character successfully added.")

                except ValueError:
                 print("Invalid choice")

      


def favorite_game_analysis(): 
    try: 
        game = input("Welcome to favorite game analysis. Enter your favorite game:\n ")

        with open(game_file_path, 'r') as file:
            game_info = dict(line.strip().split(':', 1) for line in file)



        if game.lower() in game_info: 
            print(game_info[game.lower()])


        else:
            print("Invalid game entered")


    except ValueError: 
        print("Invalid value entered")


def favorite_movie_analysis(): 
        # consider making api call for games not in file.
    try: 
        movie = input("Welcome to favorite movie/anime/show analysis. Enter you favorite movie:\n")

        with open(movie_file_path, 'r') as file:
            #dict converts list of key-value pairs created by split into a dictionary
            #line.strip removes whitespaces from each line
            #line.strip().split(":" , 1) splits each line at the first colon and the 1 is the second argument to split which shows the split should occur once. 
            #if additonal colons in the line are present, they'll be part of a second element.
            movie_info = dict(line.strip().split(':', 1) for line in file)



        if movie.lower() in movie_info: 
            print(movie_info[movie.lower()])


        else:
            print("Invalid movie entered")


    except ValueError:
        print("This is a movie one, what are you doing?")




def adventure_story(): 

    try: 
        print("You have beaten Ashera and mysteriously went to sleep. You now have woken up in the skies of your own home world, you realize that you live on the clouds!")
        print("You find a mysterious cloud shaped key that leads into a door that you don't know where it goes and a mysterious drink. Which do you choose?")
        adventure = input("mysterious drink or cloud key: \n").lower()

        while True: 
            if adventure.lower() == "mysterious drink": 
                print("You have become immortal and are immune to death.")
                break

            elif adventure.lower() == "cloud key":
                print("You have opened up the mysterious door and realize the item was boobytrapped by Ashera. Everyone dies. ")
                break

            else:
                print("Invalid value, please try again.")


    except ValueError: 
        print("Invalid value please try again.")


def adventure_story_menu():
    print("Welcome to the adventure story menu, choose a number between 1 and 2")
   
    try:
        while True:
            print("1. Start adventure")
            print("2. Return to main program.")
            choice = int(input("choose between 1 and 2. "))


            if choice == 1: 
                adventure_story()

            elif choice == 2:
                print("returning to main program")
                break

    except ValueError: 
        print("Invalid input, enter a number")


def trivia(): 
    print("Welcome to python trivia! there will be 5 questions.")
        # consider making api call for trivia database
    questions_and_answers = {
        "What is the capital of France?": "paris\n", 
        "What is the first fire emblem game to be released in the west?": "fire emblem 7\n",
        "What is the latest fire emblem game?": "fire emblem 17\n",
        "How many holes in a straw?": "one\n", 
        "True or false: Radiant dawn has 4 parts to the game.": "true\n"

    }
    #iterate over each question and it's corresponding correct answer in the dictionary.
    for question, correct_answer in questions_and_answers.items(): 

        while True:
            answer = input(question + '\n')

            if answer.lower() == correct_answer: 
                print("That's correct\n")
                break
            else: 
                print("Incorrect, try again")


    print("Congratulations! You completed trivia.")
           

def trivia_menu():
    print("Welcome to trivia, would you like to start?")
    try: 
        while True: 
            
            print("1. Start trivia")
            print("2. Return to main menu ")
            choice = int(input("Enter you choice between 1 and 2: "))

            if choice == 1: 
                trivia()

            elif choice == 2:
                print("returning to main menu")
                break

            else:
                print("Unexpected input. try again,")

    except ValueError:
        print("Invalid input, please enter number")


            
def joke_menu(): 
    print("Welcome to the joke menu. Here are your options\n")
    try:
        while True:
            print("1. Add a joke")
            print("2. Tell me a joke")
            print("3. Show jokes")
            print("4. Show random jokes")
            print("5. Return to main program\n")
            choice = int(input("Choose a number between 1 and 5: \n"))


            if choice == 1: 
                add_joke()
    
            elif choice == 2: 
                tell_joke(random_jokes)
            elif choice == 3:
                show_joke_file(joke_file_path)
            
            elif choice == 4: 
                show_joke_file(random_jokes)
            
            elif choice == 5: 
                print("returning to the main program.")
                break
        
            else:
                print(f"You entered {choice} try again and enter a valid number this time.")

    except ValueError: 
        print("Invalid input")




def main():
    while True:
        print("Hello and welcome to our expanded menu. Here is the list of things to do.")
        print("1: Jokes")
        print("2: What your favorite thing says about you")
        print("3: Choose your own adventure story.")
        print("4: trivia")
        print("5: exit")
        
       
        try: 
            choice = int(input("choose an option between 1 and 5: \n "))

            if choice == 1: 
                joke_menu()

            elif choice == 2: 
                favorite_thing()

            elif choice == 3: 
                adventure_story_menu()

            elif choice == 4: 
                trivia_menu()

            elif choice == 5: 
                print("Exiting the program bye!")
                break

            else: 
                print(f"You entered {choice} You can't just enter any number you want, please enter a number between 1 and 4")

        except ValueError: 
            print(" Invalid Input. Please enter a numeric value for the menu.")
main()



