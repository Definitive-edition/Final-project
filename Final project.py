#Aditya Chunduru
#00335780
#Final Project
#CIS 153 L8
#Program description: An expanded entertainment menu with a bit more fun activities to do. 
import random
import re
import colorama 
from colorama import Fore, Back, Style
import requests
from functools import partial

#file variables
joke_file_path = "jokes.md"
character_file_path = "favorite_character.md"
game_file_path = "favorite_game.md"
movie_file_path = "favorite_movie.md"
trivia_file = "trivia_questions.md"

#this function makes an api call to find out about a given movie
#Api provider is: https://search.imdbot.workers.dev/
#movie name is to be passed as parameter for example: "usage":"pass a 'q' as a query string parameter","info":"
#make sure requests package is installed put in 'pip install requests on command prompt'
#import requests 

#function definition which takes movie_name as parameter
def query_online_movie_database(movie_name): 
    #variable initialization with url
    movieDbApiUrl = "https://search.imdbot.workers.dev/"
    #empty dictionary called movie_params to store parameters for API request
    movie_params = {}
    #key value pair added where key is 'q and value is movie name passed to the function
    movie_params['q'] = movie_name 
    #sends a get request to the movie database API using requests library with params being used to include the query parameters in the request
    movie_response = requests.get(movieDbApiUrl, params=movie_params)
    #prints information about API response including response object
    print(f"This is the API response: {movie_response}")

    #checks if the HTTP code is 200 which means the request was successful
    if movie_response.status_code == 200:
        #extracts the description field from the JSON content of API response and is assigned to movieRespDescription
        movieRespDescription = movie_response.json()['description']
        #prints the count of movie search results in string format
        print ("Movie search results count: " + str(len(movieRespDescription)))
        #start of loop over each movie result in movieRespDescription
        for mResult in movieRespDescription:
            #extraction of the movie title, year and actors from each result in loop
            title = mResult['#TITLE']
            year = mResult['#YEAR']
            actors = mResult['#ACTORS']
            #movie details for each result in string format
            print ('Movie: ', str(title),  'Year: ', str(year),  'Actors:', str(actors))
    #closed HTTP response connection and returns movieRespDescription which has info about the search results
    movie_response.close()
    return movieRespDescription
    


#this function tells a joke for a selected category. Takes file path of jokes file, reads the file and based on the selected joke category
#it displays a random joke based on category input
#function defintion with pJoke_file_path as parameter
def tell_joke(pJoke_file_path):
    #initilize empty list to store jokes
    joke_list = []
    #all these lines print a menu using color codes from the colorama library. user prompted to select category or exit.
    print("\n") 
    print(f"{Fore.RED}1. NASA related joke")
    print(f"{Fore.RED}2. Dog jokes")
    print(f"{Fore.RED}3. Dinsosaur jokes ")
    print(f"{Fore.RED}4. Lawyer jokes")
    print(f"{Fore.RED}5. Miscellaneous jokes")
        #user prompted to input category number or type exit to go back to main menu
    user_input = input(f"{Back.WHITE},{Fore.GREEN}Select a category for the joke (1-5): ")
        #creates a regular expression pattern concatenating the user's input with the '^' character which indicates the start of a line.
    regPattern = f"^{user_input}:"
        #opens the joke file in read mode using with to properly close after reading
    with open(pJoke_file_path, 'r') as file:
            #these next few lines loop through each line in the file applying the regex pattern to find lines that match the input of the user. the line is added to joke_list if match found.
            joke_pattern = re.compile(regPattern)
            for line in file: 
                match = joke_pattern.search(line)
                if match: 
                    joke_list.append(match.string) 

                #if joke list is not empty, this statement will run
            if joke_list:
                    #random index generated within valid range of indices for the list. Joke selected from list using random index and assigned to selected_joke
                    #which is then printed using color codes. Note that the -1 is to make sure that the generated random index is within the bounds of the list
                    # the 0 is the starting point for the range for random index generation
                randomJokeIndex = random.randint(0, len(joke_list) - 1)
                selected_joke = joke_list[randomJokeIndex]
                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Here is your joke: {joke_list[randomJokeIndex]}")
                    #returns the selcted joke value
                return selected_joke
                #else block executed if the list is empty which means no jokes were found for selected category and returns none
            else: 
                print("No Jokes found for selected category")
                return None
  
       

#function that displays submenu for jokes. User can add joke for a selected category. The jokes entered will be saved in jokes.md
def add_joke():
    print('\n') 
    print(f"{Fore.RED}1. NASA related joke")
    print(f"{Fore.RED}2. Dog jokes")
    print(f"{Fore.RED}3. Dinsosaur jokes ")
    print(f"{Fore.RED}4. Lawyer jokes")
    print(f"{Fore.RED}5. Miscellaneous jokes")
    print(f"{Fore.RED}6. exit joke menu")
    #category input for the joke with input being taken as string

    user_input = input(f"{Back.WHITE},{Fore.GREEN}Select a category for the joke (1-6) or press exit to go back to main menu: ")
        

    if user_input.lower() == '6':
        print("Exiting menu")
        return
        
        
        #regular expression to remove color codes
        # \x1b is the an escape code to remove color coding
        # \[ is a literal character
        # [0-9;*] this part of the pattern is a character class 
        #m is a literal character to mark the end of a color code.
    user_input_without_color = re.sub(r'\x1b\[[0-9;]*m', '', user_input)
        #\b matches any word boundary such as spaces, dashes, commas, semicolons and more ensures that the 1-6 isn't part of a larger number.
        #[1-6] is a character class matching any single digit from 1 to 6. the digit at this position must be one of these digits.
    if not re.match(r"\b[1-6]\b",user_input_without_color):
        print("Invalid input. Enter a valid value between 1 and 6")
        return
        #input converted to int for further processing
    category = int(user_input_without_color)

        

    if category not in range (1, 7): 
        print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Unexpected input, enter a value between 1 and 6.")
        return #exiting function if invalid input is detected
        
        #new joke entry for specified category
    new_joke = input("Enter a new joke: ")

        #opens the file in append mode and appends the created joke with it's category to the file and prints the sucess message.
    with open(joke_file_path, "a") as file: 
        file.write(f"{category}: {new_joke}\n")
        print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX} Joke added.")

        





#This function is called from jokes submenu for show all jokes option.
#Opens file path passed in the parameter in read mode and prints to the terminal the contents of the file
def show_joke_file(joke_file_path):
    with open (joke_file_path, "r") as file: 
        for line in file: 
            print(line.strip())
    
    






#this is the main program for engaging user on favorite things. User can choose favorite character, movie and games
def favorite_thing():
    #list created containing three strings with each string representing a different category
    topics = ["Favorite character","Favorite Movie", "Favorite Game"]

    try:
        print('\n') 
        print(f"{Fore.GREEN}1. Favorite character")
        print(f"{Fore.GREEN}2. Favorite Movie")
        print(f"{Fore.GREEN}3. Favorite Game")
        print(f"{Fore.GREEN}4. exit to main program")
        #takes user input for topic and converts it into integer
        topic_choice = int(input("Choose a topic between 1 and 4.\n "))
       
        #alternative to if-else using dictionary. number 2 uses the functools module and the partial library to partially apply the favorite_movie_analysis with movie_file_path as a parameter
        favorite_thing_dict = {

            1: favorite_character_analysis,
            2: partial(favorite_movie_analysis, movie_file_path),
            3: favorite_game_analysis
        }

        if topic_choice == 4:
            print(f"{Fore.GREEN}returning to the main menu")
            return

        if topic_choice in favorite_thing_dict:
            #favorite_thing_dict[topic_choice]() accesses a function from the favorite_thing_dict using topic_choice as the key before calling the function.
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}You chose {topics[topic_choice - 1]}")#topic_choice 1 retrives the corresponding topic from the list
            #calls the function with user's choice from dictionary
            favorite_thing_dict[topic_choice]()
        else:
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}You shall not pass.")
            return
    except ValueError:
        print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Seriously! nice try. You really thought you could get away with entering anything other than a number")
     

#this function is for character analysis within favorite things submenu. 
#this function will take user input for a character and displays brief description of the character
#Alternatively, user can add a character to the file.
def favorite_character_analysis(): 
        #empty dictionary created to store information about favorite characters
        character_info = {}
        #opens the file in read mode
        with open(character_file_path, 'r') as file:
                #iterates over each line in file
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
        #character and character_choice variables intiialized
        character = None
        character_choice = False
        print ("Welcome to favorite character analysis.")
        #while loop start until character_choice becomes True
        while character_choice is not True:
                #user input taken for favorite character or type exit
                    character = input(f"{Back.WHITE},{Fore.GREEN}Enter your favorite character or enter exit:\n ")

                    #if user enters exit, character_choice is set to True
                    if character == "exit":
                        print("exiting...")
                        character_choice = True
                        return
                    #check if character entered is in character_info
                    if character in character_info: 
                        print(Back.BLACK + Fore.LIGHTCYAN_EX + character_info[character.lower()])

                        

                    else: 
                        print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX} character not in file.")

                        #ask user if they want to add character to file
                        addition_status = input(f"{Back.WHITE},{Fore.GREEN} Do you want to add character for:{character}? press y to continue: ")
                        #if user presses y , it will take input for description
                        if addition_status.lower() == "y": 
                            character_description = input(f"{Back.WHITE},{Fore.GREEN} Enter description: ")

                            # character_info dictionary updated with the new character and description and appends this information to file.
                            character_info[character] = f"{character}: {character_description}"

                            with open(character_file_path, "a") as file:
                                file.write('\n' + character + ': ' + character_description )
                                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX} Character successfully added.")

               

      

#function to display about a game or add a game description
def favorite_game_analysis():  
        #takes user input for favorite game
        game = input(f"{Back.WHITE},{Fore.GREEN}Welcome to favorite game analysis. Enter your favorite game:\n ")

        #opens file in read mode and uses dictionary comprehension to make game_info dictionary from lines of file. Every line stripped of leading and trailing whitespaces,
        #split at first colon ':' creating key-value pairs.
        with open(game_file_path, 'r') as file:
            game_info = dict(line.strip().split(':', 1) for line in file)


        #checks if entered game is in the game_info dictionary. If found, info about game printed
        if game.lower() in game_info: 
            print(game_info[game.lower()])

        #if game isn't found, error message printed.
        else:
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Game not in file")

        #asks user to add game description for entered game. press y to proceed
            addition_status = input(f"{Back.WHITE},{Fore.GREEN}Do you want to add game description for: {game}? press y to continue: ")
        #add description and rating
            if addition_status.lower() == "y": 
                game_description = input(f"{Back.WHITE},{Fore.GREEN}Enter description: ")
                game_rating = input(f"{Back.WHITE},{Fore.GREEN} Enter rating out of 10: ")
                #game_info dict with new game and description and appends info to file.
                game_info[game] = f"{game}: {game_description}, Rating: {game_rating}"

                with open(game_file_path, "a") as file:
                    file.write('\n' + game + ': ' + game_description + ', Rating: ' + game_rating)
                    print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Game successfully added.")



#function to display about a movie
def favorite_movie_analysis(movie_file_path): 
        # consider making api call for games not in file.
    #takes user input for favorite movie inside of try block   
    try: 
        movie = input(f"{Back.WHITE},{Fore.GREEN}Welcome to favorite movie/anime/show analysis. Enter your favorite movie:\n")

        #opens file in read mode and reads its contents line by line. For each line, it splits the line at first colon and creates key-value pair in movie_info dictionary.
        with open(movie_file_path, 'r') as file:
            movie_info = {}



            for line in file: 

                key, value = map(str.strip, line.split (':', 1))

                movie_info[key] = value 

        #If entered movie is found in the local file, info about movie and genre is printed
        if movie in movie_info: 
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Information about your favorite movie '{movie}':")
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}description: {movie_info[movie]}")


        #movie not found in local file. Make an api call to online movie database.
        #if not found online, then ask to enter your own description about the movie and add to local file.
        else: 
            #making an api call
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX} Checking for the movie in online movie database.")
            movie_info = query_online_movie_database(movie)
            
            #if online database doesn't have information about movie and prompts user to provide description and adds movie info to local file
            if len(movie_info) < 1: 

                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Sorry, information about '{movie}' not available")
                description = input(f"{Back.WHITE},{Fore.GREEN}Please provide a description for '{movie}: '")

                with open(movie_file_path, 'a') as file: 
                    file.write(f"\n{movie}: {description}")
                    print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Information about '{movie}' has been added to the file")

    #FileNotFoundError if file isn't found and prints error message
    except FileNotFoundError:
        print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}File not found at {movie_file_path}")
    #catches other exceptions as a generic exception class and prints an error message with the exception details.
    except Exception as e: 
        print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}An error occured: {e}")



#function for authoring an adventure story
def adventure_story():  
        print("\n")
        print(f"{Fore.YELLOW}You have beaten Ashera and mysteriously went to sleep. You now have woken up in the skies of your own home world, you realize that you live on the clouds!")
        print(f"{Fore.YELLOW}You find a mysterious cloud shaped key that leads into a door that you don't know where it goes and a mysterious drink. Which do you choose?")
        adventure = None

        while adventure not in ["mysterious drink", "cloud key"]:
            adventure = input(f"{Back.WHITE},{Fore.GREEN}mysterious drink or cloud key: \n").lower()

            if adventure == "mysterious drink": 
                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}You drink the mysterious liquid and feel a surge of power that gives you intense pressure around your body and you drop dead but later find out you've become immune to death")

                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}An an immortal, you explore the cloud world, discovering all the hidden wonders of the sacred land.")
                break


            elif adventure == "cloud key": 
                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}You use the cloud-shaped key to open the mysterious door, only to find out it was boobytrapped by Ashera. The trap is triggered and everyone in the cloud world perishes. ")

                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}The consequences of your choice weighs far heavily than you envisioned as you find yhourself alone in the now desolate cloud world ")

                break

#main menu for adventure story
def adventure_story_menu():
    print("\n") 
    print(f"{Fore.YELLOW}Welcome to the adventure story menu, choose a number between 1 and 2")
   
    try:
        while True:
            print("\n")
            print(f"{Fore.YELLOW}1. Start adventure")
            print(f"{Fore.YELLOW}2. Return to main program.")
            choice = int(input(f"{Back.WHITE},{Fore.GREEN}choose between 1 and 2. "))


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
    #calls a function called load_questions with trivia_file as parameters.
    questions_and_answers = load_questions(trivia_file)
    #iteration over questions and answers loaded from trivia_file with each iteration represents a single trivia question and it's correct answer.
    for question, correct_answer in questions_and_answers.items(): 
        #sets number of attempts to 3 and enters a while loop that continues until the user either answer's correctly or runs out of attempts taking user input for answer to the current question
        attempts = 3
        while attempts > 0:    
        
            answer = input(question + '\n')
            #checks if user's answer matches correct answer and prints a message and moves on to next question
            if answer.lower() == correct_answer.lower(): 
                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}That's correct\n")
                break
            #if answer is incorrect, decrementation of the attempt counter, prints error message and continues the loop which inlcudes the number of remaining attempts
            else: 
                attempts -= 1
                # attempts > 1 is evaluated and if true, returns the string 'attempts' which means there's more than 1 attempt remaining. if false, it returns the 'attempt' string
                #meaning there's only 1 attempt left.
                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Incorrect, try again {attempts} {'attempts' if attempts > 1 else 'attempt'} remaining")

                #if attempts have run out and reach 0, prints message and shows correct answer.
                if attempts == 0:
                    print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX} You've run out of attempts, the correct answer is {correct_answer}\n")


    print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Congratulations! You completed trivia.")
           
#trivia main menu
def trivia_menu():
    print("\n") 
    print(f"{Fore.BLUE}Welcome to trivia, would you like to start?")
    while True: 
        print(f"{Fore.BLUE}1. Start trivia")
        print(f"{Fore.BLUE}2. Return to main menu ")
        choice = int(input("Enter you choice between 1 and 2: "))

        if choice == 1: 
            trivia()

        elif choice == 2:
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}returning to main menu")
            break

        else:
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Unexpected input. try again,")


#main menu for jokes          
def joke_menu(): 
    print("\n") 
    print("Welcome to the joke menu. Here are your options\n")

    choice = 0 #choice initialization before loop
    try:

        

        while choice != 4:
            print(f"{Fore.RED}1. Add a joke")
            print(f"{Fore.RED}2. Tell me a joke")
            print(f"{Fore.RED}3. Show all jokes")
            print(f"{Fore.RED}4. Return to main program\n")
            choice = int(input("Choose a number between 1 and 4: \n"))


            if choice == 1: 
                add_joke()
    
            elif choice == 2: 
                tell_joke(joke_file_path)
            elif choice == 3:
                show_joke_file(joke_file_path)
            
            elif choice == 4: 
                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}returning to the main program.")
                break
        
            else:
                print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}You entered {choice} try again and enter a valid number this time.")

    except ValueError: 
        print("Invalid input")



#calculates the score of given word based on values of letters in english alphabet using a generator expression within the sum function calculating the scores of each letter
def str_manipulation(word):
    # ord(letter) - ord('a') + 1 calculates a score for each letter in lowercase version of word
    #ord letter returns unicode point of the character letter
    # ord() function gets numeric value associated with character.
    #ord(a) provides unicode code point of the lower case letter a
    #ord letter - ord('a') is 1 representing that the b is the second letter in the alphabet.
    #ord(letter) - ord('a') + 1 adds 1 to the result making sure that the letter 'a' has a score of 1 
    score  = sum((ord(letter) - ord('a') + 1) for letter in word.lower())
    return score

def scrabble(): 
    #Letter scores based on letters of words entered
    letter_scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 3, 'g': 6, 'h': 7, 'i': 8, 'j':0 }
    #player scores is a list keeping track of the scores of two players
    player_scores = [0, 0]
    #integer of 0 or 1 indicating which player's turn it is. It starts with player 1 with the index of 0.
    current_player = 0
    #infinite loop until the player exits. Each iteration prompts the current player to enter a word.
    while True: 
        word = input(f"{Back.WHITE},{Fore.GREEN}Player {current_player + 1}, enter a word (or 'exit' to end the game): ")

        #if plater enters exit(not case sensitive), the game ends and the final results are printed and the loop is exited
        if word.lower() == "exit":
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Game over. Final scores:")
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Player 1: {player_scores[0]} points")
            print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Player 2: {player_scores[1]} points")
            break

            #str_manipulation takes word as parameter and is assigned to  calculate the score for the entered word and then added to the total score of the current player.
        score = str_manipulation(word)
        player_scores[current_player] += score
        print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX}Score for {word}: {score} points")
        print(f"{Back.BLACK}, {Fore.LIGHTCYAN_EX} Total score for Player {current_player + 1}: {player_scores[current_player]} points\n")
        #switches the current player for the next iteration of the loop.
        current_player = 1 - current_player



#main program where code starts
def main():
    choice = 0
    colorama.init(autoreset = True)

    while choice != 6:
        print(f"{Fore.RESET}Hello and welcome to our expanded menu. Here is the list of things to do.")
        print("1: Jokes")
        print("2: favorite thing")
        print("3: Choose your own adventure story.")
        print("4: trivia")
        print("5: Scrabble")
        print("6: exit")
        
       
        try: 
            choice = int(input(f"{Back.WHITE},{Fore.GREEN}choose an option between 1 and 6: \n "))

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



