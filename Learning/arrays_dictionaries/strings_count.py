# paragraph with more sentences
para_string = """
The sun set over the horizon, casting a warm golden hue across the landscape. 
Birds chirped softly as they settled in for the night, their melodies blending with the gentle rustle of leaves. 
A cool breeze stirred, carrying the fragrance of blooming flowers from the nearby garden. 
Families strolled along the path, enjoying the tranquility of the evening. 
The first stars began to appear, heralding the arrival of night.

In the heart of the city, the hustle and bustle of daily life continued unabated. 
Cars honked as they navigated through the traffic, and the sidewalks were crowded with people rushing to their destinations.
Street vendors called out, offering their goods to passersby who stopped briefly to browse. 
Neon signs flickered above the storefronts, adding a vibrant glow to the urban scene. Despite the frenetic pace,
there was an undeniable rhythm to the city’s energy.
"""
# Split the sentences with '.'
split_text=para_string.split('.')

# find the length of 

max = 0
s_index = -1

for index, sentence in enumerate(split_text):
    sentence_array = sentence.split()
    length = len(sentence_array)
    if length > max:
        max = length
        s_index = index


print (split_text[1], max)

#max=17,index=2
