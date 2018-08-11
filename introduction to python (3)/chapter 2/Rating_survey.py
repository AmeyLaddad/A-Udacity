def convert_to_numeric(score_input):
    """ Convert the score to a numerical type."""
    a = float (score_input)
    return a

def sum_of_middle_three(s1,s2,s3,s4,s5):
    """Find the sum of the middle three numbers out of the five given."""
    add_all = s1 + s2 + s3 + s4 + s5
    final = add_all - max(s1,s2,s3,s4,s5) - min (s1,s2,s3,s4,s5)
    return final
    
def score_to_rating_string(score):
    """ Convert the average score, which should be between 0 and 5, into a string rating."""
    if (0 <= score < 1): 	
        return "Terrible"
    elif (1 <= score < 2):
        return "Bad"
    elif (2 <= score < 3):
        return "OK"
    elif (3 <= score < 4):
        return "Good"
    elif (4 <= score <= 5):
        return "Excellent"    
    
    
def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score =  sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
    
print (scores_to_rating(5,"5",'5',3.0,5.0000))