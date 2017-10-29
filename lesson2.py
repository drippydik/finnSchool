#!/bin/python


#		                 _    _                    _           _               
#		 _ __ ___   __ _| | _(_)_ __   __ _    ___| |__   ___ (_) ___ ___  ___ 
#		| '_ ` _ \ / _` | |/ / | '_ \ / _` |  / __| '_ \ / _ \| |/ __/ _ \/ __|
#		| | | | | | (_| |   <| | | | | (_| | | (__| | | | (_) | | (_|  __/\__ \
#		|_| |_| |_|\__,_|_|\_\_|_| |_|\__, |  \___|_| |_|\___/|_|\___\___||___/
#		                              |___/                                    

# Programs are mostly about making choices:

# This program makes choices about what to do depending on your input (that means what you type)

# Let's make some choices

# First we are going to ask the user to write a number or a letter - input() - is where we write
# our question 

aVariable = input("Write a number or a letter:- ") ### 1 - Variables are cool more about them next
# lesson - but basically in this program we have one variable called - aVaraible - which represents
# your answer 

aVariable = aVariable if len(str( aVariable) ) == 1 else input("just one letter or number please clever clogs:- ")

### 2 This is where the program is making a choice if it needs to ask you another question because
# you typed in something wrong?

if len( str( aVariable) ) == 1 and  aVariable.isalpha(): ### This line is checking if two things are
# 1 if the aVariable is more than one letter / number
# 2 if the variable is in the alphabet - isalpha()
    
    ################################################################
    #    You can delete the two "#" on the lines below which start with print    
    ################################################################
    # print( "len(aVariable) == 1 : " + str( len(aVariable) == 1 ) )
    # print("aVariable.isalpha() : " + str( aVariable.isalpha() ) )  
    ################################################################

    print("################################################################")
    print( aVariable + " is a letter, well done")
    print("################################################################")

elif len( str( aVariable ) ) == 1 and  aVaraiable[:-1].isdigit():
    
    ################################################################
    #    You can delete the two "#" on the lines below which start with print
    ################################################################
    # print( "len(str( aVariable ) ) == 1 : " + str( len( str( aVariable ) ) == 1 ) )
    # print("aVariable.isdigit() : " + str( aVariable.isdigit() ) )  
    ################################################################

    print("################################################################")
    print( aVariable + " is a number, well done")
    print("################################################################")

else: 
    
    ################################################################
    #    You can delete the three "#" on the lines below which start with print
    ################################################################
    # print( "number of letter in aVariable" + str( len(aVariable) ) )
    # print( "please check if a aVariable is not a number or letter" )
    # print(aVariable)
    ################################################################

    print("################################################################")
    print("Either you have typed in too many letters / numbers or you have typed in a symbol!")
    print("################################################################")



# then to test it press "Esc" ==> ":!python lesson2.py" ==> press "return"

# Try the program a few times, entering a letter, a number and a symbol like "£", "$", "&" or "%" 


#         _           _ _                       
#     ___| |__   __ _| | | ___ _ __   __ _  ___ 
#    / __| '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \
#   | (__| | | | (_| | | |  __/ | | | (_| |  __/
#    \___|_| |_|\__,_|_|_|\___|_| |_|\__, |\___|
#                                    |___/      

# If you are not quite understanding this yet or want to make sure you do try the following:

# Press "Esc"  "36" then "gg" then "Delete"
# Press "Esc"  "37" then "gg" then "Delete"
# Press "Esc"  "49" then "gg" then "Delete"
# Press "Esc"  "50" then "gg" then "Delete"
# Press "Esc"  "62" then "gg" then "Delete"
# Press "Esc"  "63" then "gg" then "Delete"
# Press "Esc"  "64" then "gg" then "Delete"

# after press "esc" ==> ":w" ==> "return"

# this saves your program

# then to test your changes press "Esc" ==> ":!python lesson2.py" ==> press "return"

# Lesson Three is about variable types - press ':' and then 'wq' followed by enter to get out to the command
# line then type "vim lesson3.py"
