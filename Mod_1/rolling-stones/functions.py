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
    readers_num = list(map(lambda x: {'artist':x["artist"], 'no_albums':len(find_by_artist(x["artist"]))}, readers))
    num = 0
    for i in list(range(0, len(readers_num))):
        if readers_num[i]["no_albums"] > num:
            num = readers_num[i]["no_albums"]
            max_artist = readers_num[i]
    return max_artist
                     