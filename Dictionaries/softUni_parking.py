rows_number = int(input())
online_system = {}
for i in range(rows_number):
    line = input().split()
    command = line[0]
    username = line[1]
  
    if command == "register" and username not in online_system:
        license = line[2]
        online_system[username] = license
        print(f"{username} registered {license} successfully")
    elif command ==  "register" and username in online_system:
        license = line[2]
        print(f"ERROR: already registered with plate number {online_system[username]}")
    elif command == "unregister" and username not in online_system:
        print(f"ERROR: user {username} not found")
    else:
       online_system.pop(username)
       print(f"{username} unregistered successfully")

for key, value in online_system.items():
    print(f"{key} => {value}")
