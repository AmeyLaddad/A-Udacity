""" insert countries into the country_count dict.
    If the country isn't in the dict already, add it and set the value to 1
    If the country is in the dict, increment its value by one to keep count"""

from countries_list import country_list 

country_counts = {}
for country in country_list:

    if country not in country_counts:
        country_counts[country] = 1
    elif country in country_counts:
        x = 1 + country_counts.get(country)
        country_counts[country] = x
print (country_counts)

