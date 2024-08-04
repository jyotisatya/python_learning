from data import word_meaning_dict , iit_syllabus
#Write a function to count the total number of words in the dictionary
def word_count_dict(section_dict):
    count = 0    
    for section  , object in section_dict.items():
       count = count + len(object)
    return count
       

