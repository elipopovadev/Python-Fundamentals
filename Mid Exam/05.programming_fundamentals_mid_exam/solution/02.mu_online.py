health = 100
bitcoins = 0
you_are_died = False

dungeons_zode = input().split('|')

for i in range(0, len(dungeons_zode)):
    room = dungeons_zode[i].split(' ')
    command = room[0]
    number = int(room[1])
    
    if command == 'potion':
        if health + number <= 100:
            health += number
            print(f'You healed for {number} hp.')
        elif health + number > 100:
             print(f'You healed for {100 - health} hp.')    
             health = 100      
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        monster = command
        health -= number
        if health <= 0:
            print(f'You died! Killed by {monster}.')
            you_are_died = True
            print(f'Best room: {i + 1}')
            break
        else:
            print(f'You slayed {monster}.')
     
if you_are_died == False:   
    print('You\'ve made it!')
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')
    
