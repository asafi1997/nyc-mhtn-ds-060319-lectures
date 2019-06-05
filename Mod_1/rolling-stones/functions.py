#Reading CSV

import csv

file = 'data.csv'
with open(file) as fh:
    reader = csv.DictReader(fh, delimiter=',') 
    readers = []
    for row in reader:
        readers.append(row)
        
################
#Searching
###############

#Find By Name

def find_by_name(album):
    
    for i in list(range(0, len(readers))):
        if album == readers[i]["album"]:
            return (readers[i])     
    return None
        
        
        
#Find By Rank 
def find_by_rank(num):
    for i in list(range(0, len(readers))):
        if num == readers[i]["number"]:
            return (readers[i])    
    return None


#Find by Year
def find_by_year(year):
  
    x = []
    for i in list(range(0, len(readers))):
        if year == readers[i]["year"]:
            x.append(readers[i])   
    return x


#Find by Years
def find_by_years(year_min,year_max):
  
    x = []
    for i in list(range(0, len(readers))):
        if int(readers[i]["year"]) >= year_min and int(readers[i]["year"]) <= year_max:
            x.append(readers[i])   
    return x


#Find by Ranks
def find_by_ranks(num_min,num_max):
    x = []
    for i in list(range(0, len(readers))):
        if int(readers[i]["number"]) >= num_min and int(readers[i]["number"]) <= num_max:
            x.append(readers[i])   
    return x


#################
#All Functions
#################

#All Titles 

def all_titles():
    return list(map(lambda x: x['album'], readers))

#All Artists

def all_artists():
    return list(map(lambda x: x['artist'], readers))
    

#################
#Questions to Answer
#################

#Artist with Most Albums

def find_by_artist(artist):
  
    x = []
    for i in list(range(0, len(readers))):
        if artist == readers[i]["artist"]:
            x.append(readers[i])   
    return x

def artist_most_albums():
    readers_num = {}
    for i in range(len(readers)):
        reader = {readers[i]["artist"]: len(find_by_artist(readers[i]["artist"]))}
        readers_num.update(reader)
        
    num = 0 
    for key in readers_num:
        if readers_num[key] > num:
            num = readers_num[key]
            max_artist = {key:readers_num[key]}
#     return max_artist
            
    max_artist_list = {}
    for key in readers_num:
        if readers_num[key] == num: 
            artist = {key:readers_num[key]}
            max_artist_list.update(artist)
    return max_artist_list


#For Most Popular Word

def list_of_words(readers):
    list_words = []
    for i in range(len(readers)):
        list_words.append(readers[i]['album'].split())
    return list_words

def find_by_word(word):
    x = []
    list_words = list_of_words(readers)
    for i in list(range(0, len(readers))):
        if word in list_words[i]:
            x.append(word)   
    return x

def most_word():
    list_words = list_of_words(readers)
    words_num = {}
    for i in range(len(list_words)):
        for j in range(len(list_words[i])):
            word = {list_words[i][j]: len(find_by_word(list_words[i][j]))}
            words_num.update(word)
    
    num = 0 
    for key in words_num:
        if words_num[key] > num:
            num = words_num[key]
            max_word = {key:words_num[key]}
#     return max_artist
            
    max_word_list = {}
    for key in words_num:
        if words_num[key] == num: 
            wordx = {key:words_num[key]}
            max_word_list.update(wordx)
    return max_word_list
 
    
                     