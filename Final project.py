#Aditya Chunduru
#00335780
#Final Project
#CIS 153 L8
#Program description: An expanded entertainment menu with a bit more fun activities to do. 
import random
import re 
from colorama import Fore, Back, Style
import requests
from functools import partial

#file variables
joke_file_path = "jokes.md"
character_file_path = "favorite_character.md"
game_file_path = "favorite_game.md"
movie_file_path = "favorite_movie.md"
random_jokes = "random_jokes.md"
trivia_file = "trivia_questions.md"

#this function tells a joke for a selected category. Takes file path of jokes file, reads the file and based on the selected joke category
#it displays a random joke in the category.
def tell_joke(pJoke_file_path):
    joke_list = [] 
    print(f"{Fore.RED}1. NASA related joke")
    print(f"{Fore.RED}2. Dog jokes")
    print(f"{Fore.RED}3. Dinsosaur jokes ")
    print(f"{Fore.RED}4. Lawyer jokes")
    print(f"{Fore.RED}5. Miscellaneous jokes")
    print(f"{Fore.RED}6. exit joke menu")

    try:
        user_input = input("Select a category for the joke (1-6) or press exit to go back to main menu: ")
        regPattern = "^" + user_input

        with open(pJoke_file_path, 'r') as file:
            joke_pattern = re.compile(regPattern)
            for line in file: 
                #print(f"current line in joke file {line}")
                match = joke_pattern.search(line)
                if match: 
                    joke_list.append(match.string) 

       # print(f"Size of joke_list: {len(joke_list)}")
        randomJokeIndex = random.randint(0, len(joke_list))
        selected_joke = joke_list[randomJokeIndex]
        print(f"{Fore.RED}Here is your joke: {joke_list[randomJokeIndex]}")

        return selected_joke
    
    except ValueError: 
        print("Invalid value")
       

#function that displays submenu for jokes. User can add joke for a selected category. The jokes entered will be saved in jokes.md
def add_joke(): 
    print(f"{Fore.RED}1. NASA related joke")
    print(f"{Fore.RED}2. Dog jokes")
    print(f"{Fore.RED}3. Dinsosaur jokes ")
    print(f"{Fore.RED}4. Lawyer jokes")
    print(f"{Fore.RED}5. Miscellaneous jokes")
    print(f"{Fore.RED}6. exit joke menu")
    try:
        user_input = input("Select a category for the joke (1-6) or press exit to go back to main menu: ")
        

        if user_input.lower() == '6':
            print("Exiting menu")
            return
        
        #\b matches any word boundary such as spaces, dashes, commas, semicolons and more ensures that the 1-5 isn't part of a larger number.
        # [1-6] is a character class matching any single digit from 1 to 6. the digit at this position must be one of these digits.
        user_input_without_color = re.sub(r'\x1b\[[0-9;]*m', '', user_input)

        if not re.match(r"\b[1-6]\b",user_input_without_color):
            print(f"{Fore.RED}Invalid input. Enter a valid value between 1 and 6")
            return

        category = int(user_input_without_color)

        

        if category not in range (1, 7): 
            print(f"{Fore.RED}Unexpected input, enter a value between 1 and 6.")
            return #exiting function if invalid input is detected
        
       
        new_joke = input("Enter a new joke: ")


        with open(joke_file_path, "a") as file: 
            file.write(f"{category}: {new_joke}\n")
    except ValueError: 
        print("Invalid input. Enter a valid value for category")
        





#This function is called from jokes submenu for show all jokes option.
#Opens file path passed in the parameter in read mode and prints to the terminal the contents of the file
def show_joke_file(joke_file_path):
    with open (joke_file_path, "r") as file: 
        for line in file: 
            print(line.strip())
    
    






#this is the main program for engaging user on favorite things. User can choose favorite character, movie and games
def favorite_thing():
    topics = ["Favorite character","Favorite Movie", "Favorite Game"]
       
    

    try: 
        print(f"{Fore.GREEN}0. exit to main program")
        print(f"{Fore.GREEN}1. Favorite character")
        print(f"{Fore.GREEN}2. Favorite Movie")
        print(f"{Fore.GREEN}3. Favorite Game")
        topic_choice = int(input("Choose a topic between 1 and 3.\n "))
       
        #alternative to if-else using dictionary instead
        favorite_thing_dict = {

            1: favorite_character_analysis,
            2: partial(favorite_movie_analysis, movie_file_path),
            3: favorite_game_analysis
        }

        if topic_choice == 0:
            print("returning to the main menu")
            return

        if topic_choice in favorite_thing_dict:
            #favorite_thing_dict[topic_choice]() accesses a function from the favorite_thing_dict using topic_choice as the key before calling the function.
            print(f"{Fore.GREEN}You chose {topics[topic_choice - 1]}")#topic_choice 1 retrives the corresponding topic from the list
            favorite_thing_dict[topic_choice]()
        else:
            print("You shall not pass.")
            return
    except ValueError:
        print("Seriously! nice try. You really thought you could get away with entering anything other than a number")
     

#this function is for character analysis within favorite things submenu. 
#this function will take user input for a character and displays brief description of the character
#Alternatively, user can add a character to the file.
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

        character = None

        while character is not True:
                try:
                    character = input("Welcome to favorite character analysis. Enter your favorite character or enter exit:\n ")

                    if character == "exit":
                        print("exiting...")
                        return
                    if character in character_info: 
                        print(Fore.GREEN, character_info[character.lower()])
                    else: 
                        print(f"{Fore.GREEN}character not in file.")
                
                    addition_status = input(f"{Fore.GREEN}Do you want to add character for:{character}? press y to continue: ")

                    if addition_status.lower() == "y": 
                        character_description = input("Enter description: ")

                        character_info[character] = f"{character}: {character_description}"

                        with open(character_file_path, "a") as file:
                            file.write('\n' + character + ': ' + character_description )
                        print(f"{Fore.GREEN}Character successfully added.")

                except ValueError:
                 print(f"{Fore.GREEN}Invalid choice")

      

#function to display about a game or add a game description
#consider making an api call to online games database
def favorite_game_analysis(): 
    try: 
        game = input(f"{Fore.GREEN}Welcome to favorite game analysis. Enter your favorite game:\n ")

        with open(game_file_path, 'r') as file:
            game_info = dict(line.strip().split(':', 1) for line in file)



        if game.lower() in game_info: 
            print(game_info[game.lower()])


        else:
            print(f"{Fore.GREEN}Game not in file")

        addition_status = input(f"{Fore.GREEN}Do you want to add game description for: {game}? press y to continue: ")

        if addition_status.lower() == "y": 
            game_description = input("Enter description: ")

            game_info[game] = f"{game}: {game_description}"

            with open(game_file_path, "a") as file:
                file.write('\n' + game + ': ' + game_description )
                print(f"{Fore.GREEN}Game successfully added.")

        

        


    except ValueError: 
        print(f"{Fore.GREEN}Invalid value entered")

#function to display about a movie
def favorite_movie_analysis(movie_file_path): 
        # consider making api call for games not in file.
    try: 
        movie = input(f"{Fore.GREEN}Welcome to favorite movie/anime/show analysis. Enter you favorite movie:\n")

        with open(movie_file_path, 'r') as file:
            movie_info = {}



            for line in file: 

                key, value = map(str.strip, line.split (':', 1))

                movie_info[key] = value 


        if movie in movie_info: 
            print(f"{Fore.GREEN}Information about your favorite movie '{movie}':")
            print(f"{Fore.GREEN}Genre: {movie_info[movie]}")


        else: 
            print(f"{Fore.GREEN}Sorry, information about '{movie}' not available")

            description = input(f"{Fore.GREEN}Please provide a description for '{movie}'")



            movie_info[movie] = description


            with open(movie_file_path, 'a') as file: 
                file.write(f"\n{movie}: {description}")
                print(f"{Fore.GREEN}Information about '{movie}' has been added to the file")



    except FileNotFoundError:
        print(f"File not found at {movie_file_path}")

    except Exception as e: 
        print(f"An error occured {e}")



#function for authoring an adventure story
#consider incorporating an AI module for script generation
def adventure_story(): 

    try: 
        print(f"{Fore.YELLOW}You have beaten Ashera and mysteriously went to sleep. You now have woken up in the skies of your own home world, you realize that you live on the clouds!")
        print(f"{Fore.YELLOW}You find a mysterious cloud shaped key that leads into a door that you don't know where it goes and a mysterious drink. Which do you choose?")
        

        while True:
            adventure = input(f"{Fore.YELLOW}mysterious drink or cloud key: \n").lower()

            if adventure == "mysterious drink": 
                print(f"{Fore.YELLOW}You drink the mysterious liquid and feel a surge of power that gives you intense pressure around your body and you drop dead but later find out you've become immune to death")

                print(f"{Fore.YELLOW}An an immortal, you explore the cloud world, discovering all the hidden wonders of the sacred land.")
                break


            elif adventure == "cloud key": 
                print(f"{Fore.YELLOW}You use the cloud-shaped key to open the mysterious door, only to find out it was boobytrapped by Ashera. The trap is triggered and everyone in the cloud world perishes. ")

                print(f"{Fore.YELLOW}The consequences of your choice weighs far heavily than you envisioned as you find yhourself alone in the now desolate cloud world ")

                break
        


    except ValueError: 
        print("Invalid value please try again.")

#main menu for adventure story
def adventure_story_menu():
    print(f"{Fore.YELLOW}Welcome to the adventure story menu, choose a number between 1 and 2")
   
    try:
        while True:
            print(f"{Fore.YELLOW}1. Start adventure")
            print(f"{Fore.YELLOW}2. Return to main program.")
            choice = int(input("choose between 1 and 2. "))


            if choice == 1: 
                adventure_story()

            elif choice == 2:
                print("returning to main program")
                break

    except ValueError: 
        print("Invalid input, enter a number")

#function for trivia
#consider adding file based trivia and then look for trivia api.

#function definiton that takes trivia_file as parameter which is the path to the trivia questions file
def load_questions(trivia_file):
    #initializes an empty dictionary which stores the loaded trivia questions
    questions_and_answers = {}
    #opens the file in read mode using a with statement which ensures it properly closes after reading.
    with open(trivia_file, 'r') as file: 
        #iterates over each line in the opened file
        for line in file: 
            #splits the line at colon and removes whitespaces using str.strip which results in two elements, the question and answer.
            question, answer = map(str.strip, line.split(':', 1))
            #key_value pair to the question and answers dictionary where the key is the question and the value is the answer
            questions_and_answers[question] = answer
    #closes file automatically by returning the dictionary
    return questions_and_answers




def trivia(): 
    print(f"{Fore.BLUE}Welcome to trivia! there will be 5 questions.")
    # consider making api call for trivia database
    questions_and_answers = load_questions(trivia_file)

    for question, correct_answer in questions_and_answers.items(): 
        while True:
            answer = input(question + '\n')

            if answer.lower() == correct_answer.lower(): 
                print(f"{Fore.BLUE}That's correct\n")
                break
            else: 
                print(f"{Fore.BLUE}Incorrect, try again")


    print(f"{Fore.BLUE}Congratulations! You completed trivia.")
           
#trivia main menu
def trivia_menu():
    print(f"{Fore.BLUE}Welcome to trivia, would you like to start?")
    while True: 
        print(f"{Fore.BLUE}1. Start trivia")
        print(f"{Fore.BLUE}2. Return to main menu ")
        choice = int(input("Enter you choice between 1 and 2: "))

        if choice == 1: 
            trivia()

        elif choice == 2:
            print(f"{Fore.BLUE}returning to main menu")
            break

        else:
            print(f"{Fore.BLUE}Unexpected input. try again,")


#main menu for jokes          
def joke_menu(): 
    print("Welcome to the joke menu. Here are your options\n")

    choice = 0 #choice initialization before loop
    try:

        

        while choice != 4:
            print(f"{Fore.RED}1. Add a joke")
            print(f"{Fore.RED}2. Tell me a joke")
            print(f"{Fore.RED}3. Show all jokes")
            print(f"{Fore.RED}4. Return to main program\n")
            choice = int(input("Choose a number between 1 and 5: \n"))


            if choice == 1: 
                add_joke()
    
            elif choice == 2: 
                tell_joke(joke_file_path)
            elif choice == 3:
                show_joke_file(joke_file_path)
            
            elif choice == 4: 
                print(f"{Fore.RED}returning to the main program.")
                break
        
            else:
                print(f"{Fore.RED}You entered {choice} try again and enter a valid number this time.")

    except ValueError: 
        print("Invalid input")



#calculates the score of given word based on values of letters in english alphabet using a generator expression within the sum function calculating the scores of each letter
def str_manipulation(word):
    score  = sum((ord(letter) - ord('a') + 1) for letter in word.lower())
    return score

def scrabble(): 
    #Letter scores based on letters of words entered
    letter_scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 3, 'g': 6, 'h': 7, 'i': 8 }
    #player scores is a list keeping track of the scores of two players
    player_scores = [0, 0]
    #integer of 0 or 1 indicating which player's turn it is. It starts with player 1 with the index of 0.
    current_player = 0
    #infinite loop until the player exits. Each iteration prompts the current player to enter a word.
    while True: 
        word = input(f"{Fore.PURPLE}Player {current_player + 1}, enter a word (or 'exit' to end the game): ")

        #if plater enters exit(not case sensitive), the game ends and the final results are printed and the loop is exited
        if word.lower() == "exit":
            print(f"{Fore.PURPLE}Game over. Final scores:")
            print(f"{Fore.PURPLE}Player 1: {player_scores[0]} points")
            print(f"{Fore.PURPLE}Player 2: {player_scores[1]} points")
            break

            #str_manipulation takes word as parameter and is assigned to score to calculate the score for the entered word and then added to the total score of the current player.
        score = str_manipulation(word)
        player_scores[current_player] += score
        print(f"{Fore.PURPLE}Score for {word}: {score} points")
        print(f"{Fore.PURPLE}Total score for Player {current_player + 1}: {player_scores[current_player]} points\n")
        #switches the current player for the next iteration of the loop.
        current_player = 1 - current_player



#main program where code starts
def main():
    choice = 0

    while choice != 6:
        print(f"{Fore.RESET}Hello and welcome to our expanded menu. Here is the list of things to do.")
        print("1: Jokes")
        print("2: What your favorite thing says about you")
        print("3: Choose your own adventure story.")
        print("4: trivia")
        print("5: Scrabble")
        print("6: exit")
        
       
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
                scrabble()

            elif choice == 6: 
                print("Exiting the program bye!")

            else: 
                print(f"You entered {choice} You can't just enter any number you want, please enter a number between 1 and 4")

        except ValueError: 
            print(" Invalid Input. Please enter a numeric value for the menu.")
main()



