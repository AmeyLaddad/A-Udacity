def comp_answer(my_answers,answers,results,num):
    if my_answers[num] == answers[num]:
        results[num] = True
    elif my_answers[num] != answers[num]:
        results[num] = False

def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple 
    choice quiz and returns the results.
    """
    results= []
    x = 0    
    while x< len(results):
        comp_answer(my_answers,answers,results,x)        
    count_correct = 0
    count_incorrect = 0

    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1        
      
         
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."