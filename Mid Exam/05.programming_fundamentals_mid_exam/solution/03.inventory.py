inventory = input().split(', ')

text = input()
while(text != 'Craft!'):
    new_text = text.split(' - ')    
    command = new_text[0]
    item = new_text[1]
    if command == 'Collect' and item not in inventory:
        inventory.append(item)
    elif command == 'Drop' and item in inventory:
        inventory.remove(item)
    elif command == 'Combine Items':
        items = item.split(':')
        old_Item = items[0]
        new_Item = items[1]
        if old_Item in inventory:
            find_index = inventory.index(old_Item)
            inventory.insert(find_index + 1, new_Item)
    elif command == 'Renew' and item in inventory:
        inventory.remove(item)
        inventory.append(item)
    text = input()

print(', '.join(inventory))

        