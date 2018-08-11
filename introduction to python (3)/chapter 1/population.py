sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Code that prints True if San Francisco is denser than Rio, and False otherwise
print ("san_francisco_pop_density:",int(san_francisco_pop_density))
print ("rio_de_janeiro_pop_density:",int(rio_de_janeiro_pop_density))

print (san_francisco_pop_density > rio_de_janeiro_pop_density)