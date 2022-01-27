import sys

def check_winner():
    winner = False
    if dict_keys["shards"] >= 250:
        winner = True
        print("Shadowmourne obtained!")
        dict_keys["shards"] -= 250     
    elif dict_keys["fragments"] >= 250:
        winner = True
        print("Valanyr obtained!")
        dict_keys["fragments"] -= 250
    elif  dict_keys["motes"] >= 250:
        winner = True
        print("Dragonwrath obtained!")
        dict_keys["motes"] -= 250
    return winner

def order_dict_keys(dict_keys):
    # Order by quantity (value) in descending order, then by name (key) in ascending order
    sorted_dict = dict(sorted(dict_keys.items(), key = lambda x: (-x[1], x[0])))
    return sorted_dict
   
def order_dict_junk(dict_junk):  
    # Order by key in alphabetical order.
    sorted_dict = dict(sorted(dict_junk.items(), key = lambda x: x[0]))
    return sorted_dict

def print_sorted_dict(sorted_dict):
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
    
           
dict_keys = {"shards": 0, "fragments": 0, "motes": 0}
dict_junk = {}
winner = False
while True: 
    line = input().split()  
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        item = line[i +1].lower()
        if winner == True:
          sorted_dict_keys = order_dict_keys(dict_keys)
          sorted_dict_junk = order_dict_junk(dict_junk)
          print_sorted_dict(sorted_dict_keys)
          print_sorted_dict(sorted_dict_junk)
          sys.exit()
                          
        if item == "shards":
            dict_keys["shards"] += quantity        
        elif item == "fragments": 
            dict_keys["fragments"] += quantity
        elif item == "motes":
            dict_keys["motes"] += quantity
        winner = check_winner()
               
        if item != "shards" and item != "fragments" and item != "motes":
         if item not in dict_junk:
             dict_junk[item] = quantity
         else:
             dict_junk[item] += quantity
    

        
            