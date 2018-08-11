prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"

vowel_count = 0
vowels = ['a','e','i','o','u','A','E','I','O','U']

x = 0
while(x<=9):
    Count = prophecy.count(vowels[x])
    x+=1
    vowel_count+=Count

# Print the final count
print(vowel_count)
