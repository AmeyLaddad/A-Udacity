monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 
                   'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 
                   'December': [41, 58]}

yearly_record = list(monthly_takings.values())

def total_takings(yearly_record):
    total_amount = 0
    for x in yearly_record:
        total_amount += sum (x) 
    return "Total yearly collection = ", str (total_amount)
    
print (total_takings(yearly_record))