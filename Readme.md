Aditya Chunduru
00335780
Final Project
CIS 153 L8

Program description: 

An expanded entertainment menu with a bit more fun activities to do. This program includes, jokes, trivia, favorite things and scrabble. Core python programming concepts used were, file operations, dictionarys, functions, regular expressions, string manipulation and more. In addition, API and JSON were used in this project. An API call to query online movie database to be exact

This project took me a journey of revisiting old topics and discovering new concepts of Python programming. Im glad that i can finally be proud of what i made. I think my biggest learning curve was making the api calls. I hope whoever decides to try out this program enjoys it. 


Future Work: 

If i had more time and/or knowledge, the things i would've done is:
1.) Adding a timer to my scrabble function. 
2.) Make api calls to my trivia function and game function to make it more comprehensive.
3.) I would have also improved my adventure story to prompt the user for their name and possibly even something with save files as well. Possibly leverage generative AI to make story scripting more advanced
4.) I would have learned about pseudocode and would have also learned how to make my program detect duplicate jokes if a user enters in a joke that's already on the file. 

Modules needed to run the program:
1.) random: for random number generation.
2.) re: for regex.
3.) colorama: color coded outputs to the terminal
4.) requests: for API
5.) functools: for function calls that take parameters in dictionaries


Instructions on how to operate the program: 


The program starts with displaying the main menu which include, jokes, favorite things, adventure story, trivia and scrabble with numbered 1-6 with 6 being to exit the program. Each of the options in turn display corresponding submenus. All the interactions include storing inputs captured in their respecive files except for adventure story and scrabble. The exciting part is the program makes an api call to online movie database so the user can pretty much ask about any movie there is. In case the movie isn't found online, program will prompt user to enter their own description which gets stored in the local file. 
Program follows color coded prompts: 
1.) Main menu is displayed in default font color.
1.1)Jokes menu is displayed in red, trivia menu in blue, adventure story menu in yellow and favorite thing menu in green
2.) Input prompts follow a white highlighted background and green text.
3.) Outputs follow black highlighted background and lightcyan text.
4.) 


Prerequesites to run the program:

1.)Make sure the attached files are in the directory that the code file is in. otherwise this code won't work unless you create a text file yourself and assign a variable to that text file. 

2.)For adding jokes, I recommend having a separate webpage where you can look for a new joke to add thats related to your selected category, it the category selected was miscellaneous, then go ahead with that. 

3.)There will also be a point where you are prompted with entering the letter "y" for adding a description about a game or movie pressing anything else other than y at this point will just take you back to either the start of the function if you're using a while loop or if not, it will take you back to the start of the program. 

4.)I also recommend to enter all the movie title names, game names in all lowercase or remember if you used capital letters at anytime when entering in the name of a game because you might run the risk of errors due to possible case sensitivity. 


Works cited:
https://www.goodhousekeeping.com/life/entertainment/a41779929/corny-jokes/
https://www.paralegaledu.org/blog/20-lawyer-jokes-you-should-never-tell/
https://www.rover.com/blog/dog-jokes/
https://www.rd.com/article/dinosaur-jokes/
https://worstjokesever.com/nasa

Works cited for concepts covered outside of class:
https://www.geeksforgeeks.org/print-colors-python-terminal/?ref=header_search
https://www.dataquest.io/blog/python-api-tutorial/
https://www.geeksforgeeks.org/response-url-python-requests/?ref=header_search
https://www.geeksforgeeks.org/functools-module-in-python/




