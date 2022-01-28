def check_winner(_dict):
    for key, value in _dict.items():
        if value < 250:
            continue
        _dict[key] -= 250
        if key == "shards":
            print("Shadowmourne obtained!")
        elif key == "fragments":
            print("Valanyr obtained!")
        elif key == "motes":
            print("Dragonwrath obtained!")
        return True
    return False

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
    
           
dict_items = {"shards": 0, "fragments": 0, "motes": 0}
dict_junk = {}
winner = False
while not winner: 
    line = input().split()  
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        item = line[i +1].lower()
                       
        if item in dict_items.keys():
           dict_items[item] += quantity
        else:
            if item not in dict_junk:
                dict_junk[item] = 0
            dict_junk[item] += quantity
            
        winner = check_winner(dict_items)
        if winner:
            break
               
sorted_dict_items = order_dict_keys(dict_items) # sorting is not included in Judge
sorted_dict_junk = order_dict_junk(dict_junk)
print_sorted_dict(sorted_dict_items)
print_sorted_dict(sorted_dict_junk)      
          