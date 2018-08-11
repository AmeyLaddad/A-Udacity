def which_prize(points):
    Number_of_points = points
    
    if (0<Number_of_points<50):
        return "Congratulations! You have won a wooden rabbit!"
    elif (51<Number_of_points<150):
        return "Oh dear, no prize this time."
    elif (151<Number_of_points<180):
        return "Congratulations! You have won a wafer-thin mint!"
    elif (181<Number_of_points<200):
        return "Congratulations! You have won a penguin!"
    

print(which_prize(178))