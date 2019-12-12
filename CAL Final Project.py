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
        return("Congratulations!Your answer is correct")
        
    else:
        print(solution_asp)
        return("Oops!Sorry wrong asnwer. Correct answer is as given above ")
        
        

#Function to convert frozenset object to list type 
#To make it compatible with type of user's solution, for comparison 
def convert_asp_soln_to_list(solution_asp):
    return([list(x) for x in solution_asp])
   


def main_program(choice):
    #Level 1 puzzles 
    if (choice == "DAN+NAN"):
        print("DAN+NAN=NORA\n")
        print("Complete the solution by providing the numbers for the following letters")
        letters = ['o','d','r','a','n']
        user_input=[]
        #Getting user's solution for each letter and appending them to the user_input list 
        for i in letters: 
            value=input(i)
            item_list =[]
            item_list.append(i)
            item_list.append(int(value))
            user_input.append(item_list)
        #Comparing user's solution and ASP's solution
        solution_asp = get_solver("DAN+NAN=NORA.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        return(compare_solution(solution_asp,user_input))


    if(choice == "DI+IS"):
        print("DI+IS=ILL\n")
        print("Complete the solution by providing the numbers for the following letters")
        letters = ['i','s','l','d']
        user_input=[]
        #Getting user's solution for each letter and appending them to the user_input list 
        for i in letters: 
            value=input(i)
            item_list =[]
            item_list.append(i)
            item_list.append(int(value))
            user_input.append(item_list)
        #Comparing user's solution and ASP's solution
        solution_asp = get_solver("DI+IS=ILL.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        return(compare_solution(solution_asp,user_input))


    if(choice == "LEO+LEE"):
        print("LEO+LEE=ALL \n")
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
        return(compare_solution(solution_asp,user_input))


  
    #Level 2 puzzles 
    if (choice=="EAT+THAT"):
        print("EAT+THAT=APPLE\n")
        print("Complete the solution by providing the numbers for the following letters")
        letters = ['p','a','t','h','l','e']
        user_input=[]
        #Getting user's solution for each letter and appending them to the user_input list 
        for i in letters: 
            value=input(i)
            item_list =[]
            item_list.append(i)
            item_list.append(int(value))
            user_input.append(item_list)
        #Comparing user's solution and ASP's solution
        solution_asp = get_solver("EAT+THAT=APPLE.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        return(compare_solution(solution_asp,user_input))


    if(choice == "SEEM+MEAN"):
        print("SEEM+MEAN=TEAMS\n")
        print("Complete the solution by providing the numbers for the following letters")
        letters = ['t','s','a','e','m','n']
        user_input=[]
        #Getting user's solution for each letter and appending them to the user_input list 
        for i in letters: 
            value=input(i)
            item_list =[]
            item_list.append(i)
            item_list.append(int(value))
            user_input.append(item_list)
        #Comparing user's solution and ASP's solution
        solution_asp = get_solver("SEEM+MEAN=TEAMS.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        return(compare_solution(solution_asp,user_input))


    if(choice == "TESS+SEES"):
        print("TESS+SEES=ELLEN\n")
        print("Complete the solution by providing the numbers for the following letters")
        letters = ['t','e','l','s','n']
        user_input=[]
        #Getting user's solution for each letter and appending them to the user_input list 
        for i in letters: 
            value=input(i)
            item_list =[]
            item_list.append(i)
            item_list.append(int(value))
            user_input.append(item_list)
        #Comparing user's solution and ASP's solution
        solution_asp = get_solver("TESS+SEES=ELLEN.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        return(compare_solution(solution_asp,user_input))


    #Level 3 puzzles 
    if (choice=="AT+EAST+WEST"):
        print("AT+EAST+WEST=SOUTH\n")
        print("Complete the solution by providing the numbers for the following letters")
        letters = ['a','s','e','o','h','t','w','u']
        user_input=[]
        #Getting user's solution for each letter and appending them to the user_input list 
        for i in letters: 
            value=input(i)
            item_list =[]
            item_list.append(i)
            item_list.append(int(value))
            user_input.append(item_list)
        #Comparing user's solution and ASP's solution
        solution_asp = get_solver("AT+EAST+WEST=SOUTH.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        return(compare_solution(solution_asp,user_input))


    if(choice == "CRACK+HACK"):
        print("CRACK+HACK=ERROR\n")
        print("Complete the solution by providing the numbers for the following letters")
        letters = ['e','o','a','c','h','r','k']
        user_input=[]
        #Getting user's solution for each letter and appending them to the user_input list 
        for i in letters: 
            value=input(i)
            item_list =[]
            item_list.append(i)
            item_list.append(int(value))
            user_input.append(item_list)
        #Comparing user's solution and ASP's solution
        solution_asp = get_solver("CRACK+HACK=ERROR.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        return(compare_solution(solution_asp,user_input))


    if(choice == "FOOD+FAD"):
        print("FOOD+FAD=DIETS\n")
        print("Complete the solution by providing the numbers for the following letters")
        letters = []
        user_input=['i','a','t','o','s','e','f','d']
        #Getting user's solution for each letter and appending them to the user_input list 
        for i in letters: 
            value=input(i)
            item_list =[]
            item_list.append(i)
            item_list.append(int(value))
            user_input.append(item_list)
        #Comparing user's solution and ASP's solution
        solution_asp = get_solver("FOOD+FAD=DIETS.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        return(compare_solution(solution_asp,user_input))


    if(choice not in ["FOOD+FAD","CRACK+HACK","AT+EAST+WEST","DAN+NAN","DI+IS","LEO+LEE","EAT+THAT","SEEM+MEAN","TESS+SEES"]):
        return("Oops!sorry, your game does not exist in our current menu")

#User is asked to input the game of choice - input should be in string format 
# Eg: Choose your game to play: EAT+THAT
print('Choose your game to play:')
choice=input()
solution_list =[]
result = main_program(choice)
print(result)

