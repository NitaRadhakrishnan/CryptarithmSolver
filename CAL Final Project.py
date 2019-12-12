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
        return(solution_list)
        

        
#Function to compare user's input with output from ASP solver 
def compare_solution(solution_asp,user_input):
    count = 0
    for i in solution_asp:
        for x in user_input: 
            if i == x:
                count = count +1 
    if count == len(solution_asp):
        print("Congratulations!Your answer is correct\n")
        print(user_input)
    else:
        print("Oops!Sorry wrong asnwer. Correct answer is\n")
        print(solution_asp)
        

#Function to convert frozenset object to list type 
#To make it compatible with type of user's solution, for comparison 
def convert_asp_soln_to_list(solution_asp):
    return([list(x) for x in solution_asp])
   
    
        
#User is asked to input the game of choice - input should be in string format 
# Eg: Choose your game to play: EAT+THAT
print('Choose your game to play:')
choice=input()
solution_list=[]


#Level 1 puzzles 
if (choice == "DAN+NAN"):
    #Getting user's solution
     
    #Function call to solve the puzzle DAN+NAN=NORA
    solution_list=get_solver("DAN+NAN=NORA.lp")
    
    
if(choice == "DI+IS"):
    #Getting user's solution
        
    #Function call to solve the puzzle DI+IS=ILL
    get_solver("DI+IS=ILL.lp")
    
if(choice == "LEO+LEE"):
    
    print("Complete the solution by providing the numbers for the following letters")
    letters = ['o','l','a','e']
    user_input=[]
    #Getting user's solution for each letter and appending them to the user_input list 
    for i in letters: 
        value=input(i)
        item_list =[]
        item_list.append(i)
        item_list.append(int(value))
        user_input.append(item_list)
    
    #Comparing user's solution and ASP's solution
    solution_asp = get_solver("LEO+LEE=ALL.lp")
    solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
    compare_solution(solution_asp,user_input)
   
  
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

    

                    
