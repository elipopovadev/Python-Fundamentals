import re

pattern = re.compile("^>>([A-Za-z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)$")
text = input()
all_furniture = {}

while text != "Purchase":
    if pattern.match(text):
       matches = pattern.finditer(text)
       for match in matches:
          furniture = match.group(1)
          price = float(match.group(2))
          quantity = int(match.group(3))
          if furniture not in all_furniture:
              all_furniture[furniture] = []
              all_furniture[furniture].append(price)
              all_furniture[furniture].append(quantity)
          else:
              all_furniture[furniture][0] = price
              all_furniture[furniture][1] += quantity
    text = input()
 
print("Bought furniture:")   
total_sum = 0
for key, value in all_furniture.items():
    print(f"{key}")
    total_sum += value[0] * value[1]
print(f"Total money spend: {total_sum:.2f}")
