from fuzzywuzzy import fuzz
from fuzzywuzzy import process



x= input("enter file name you want to search for ")
y= input("list of all options available in the folder to match ")

k= fuzz.token_sort_ratio(x,y)
if k>65:
    print("match found")
#process the next thing 
# repeat the process for finding another file or open the file 


