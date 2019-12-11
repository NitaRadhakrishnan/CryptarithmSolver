#!/usr/bin/env python
# coding: utf-8

# In[3]:


from clyngor import ASP, solve

print("\n\n MENU:\n\n")

print("\nLevel 1:\n")
print("\n1. DAN+NAN=NORA\n")
print("\n2. DI+IS=ILL\n")
print("\n3. LEO+LEE=ALL\n")

print("\nLevel 2:\n")
print("\n1. EAT+THAT=APPLE\n")
print("\n2. SEEM+MEAN=TEAMS\n")
print("\n3. TESS+SEES=ELLEN\n")

print("\nLevel 3:\n")
print("\n1. AT+EAST+WEST=SOUTH\n")
print("\n2. CRACK+HACK=ERROR\n")
print("\n3. FOOD+FAD=DIETS\n")



#Function to calculate the solution for the given problem and print the solution 
def get_solver(filename):
    answers = solve(filename) # Returns the solution in the form of Frozenset objects 
    for answer in answers:
        ls = answer 
        for x in ls: 
            for y in x: 
                if(y!='x'): 
                    solution_list.append(y)
        print("\nYour solution is:\n")
        print(solution_list) # Print solution in appropriate format 
        
        
#User is asked to input the game of choice - input should be in string format 
# Eg: Choose your game to play: EAT+THAT
print('Choose your game to play:')
choice=input()
solution_list=[]


#Level 1 puzzles 
if (choice=="DAN+NAN"):
    #Function call to solve the puzzle DAN+NAN=NORA
    get_solver("DAN+NAN=NORA.lp")
if(choice == "DI+IS"):
    #Function call to solve the puzzle DI+IS=ILL
    get_solver("DI+IS=ILL.lp")
if(choice == "LEO+LEE"):
    #Function call to solve the puzzle LEO+LEE=ALL
    get_solver("LEO+LEE=ALL.lp")
    
#Level 2 puzzles 
if (choice=="EAT+THAT"):
    #Function call to solve the puzzle EAT+THAT=APPLE
    get_solver("EAT+THAT=APPLE.lp")
if(choice == "SEEM+MEAN"):
    #Function call to solve the puzzle SEEM+MEAN=TEAMS
    get_solver("SEEM+MEAN=TEAMS.lp")
if(choice == "TESS+SEES"):
    #Function call to solve the puzzle TESS+SEES=ELLEN
    get_solver("TESS+SEES=ELLEN.lp")
    
#Level 3 puzzles 
if (choice=="AT+EAST+WEST"):
    #Function call to solve the puzzle AT+EAST+WEST=SOUTH
    get_solver("AT+EAST+WEST=SOUTH.lp")
if(choice == "CRACK+HACK"):
    #Function call to solve the puzzle CRACK+HACK=ERROR
    get_solver("CRACK+HACK=ERROR.lp")
if(choice == "FOOD+FAD"):
    #Function call to solve the puzzle TESS+SEES=ELLEN
    get_solver("FOOD+FAD=DIETS.lp")

    

                    


# In[ ]:





# In[ ]:




