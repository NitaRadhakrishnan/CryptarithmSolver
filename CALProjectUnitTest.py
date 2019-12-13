#!/usr/bin/env python
# coding: utf-8

# In[4]:


import unittest
from clyngor import ASP, solve
#import import_ipynb
def get_solver(filename):
    answers = solve(filename) # Returns the solution in the form of Frozenset objects 
    for answer in answers:
        ls = answer 
        for x in ls: 
            for y in x: 
                if(y!='x'): 
                    solution_list.append(y)
        return(solution_list)
    
def convert_asp_soln_to_list(solution_asp):
    return([list(x) for x in solution_asp])

def compare_solution(solution_asp,user_input):
    count = 0
    for i in solution_asp:
        for x in user_input: 
            if i == x:
                count = count +1 
    if count == len(solution_asp):
        return("Congratulations!Your answer is correct")
        
    else:
        #print(solution_asp)
        return("Oops!Sorry wrong asnwer. Correct answer is as given above ")
solution_list =[]

class TestGameSolution(unittest.TestCase):
    def test_dan_happy_case(self):
        #import GameSetChallenge 
        user_input = [['o',0],['a',2],['n',1],['r',4],['d',9]]
        solution_asp = get_solver("DAN+NAN=NORA.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        self.assertEqual(compare_solution(solution_asp,user_input),"Congratulations!Your answer is correct")

    
    def test_dan_alternate_case(self):
        #import GameSetChallenge 
        user_input = [['o',1],['a',2],['n',3],['r',4],['d',5]]
        solution_asp = get_solver("DAN+NAN=NORA.lp")
        solution_asp = convert_asp_soln_to_list(solution_asp)  #converting frozenset object to list 
        self.assertEqual(compare_solution(solution_asp,user_input),"Oops!Sorry wrong asnwer. Correct answer is as given above ")
        
    def test_invalid_choice(self):
        import GameSetChallenge 
        result = GameSetChallenge.main_program("SPOT+POT")
        self.assertEqual(result, "Oops!sorry, your game does not exist in our current menu")
    
        
if __name__ == '__main__':
    unittest.main()


# In[ ]:




