str = "Looping"

for item in str:
    print(item)

for i in range(10):
    print(f"looping....{i}")

favourites = ["Red Sauce Pasta", "Apple Pie",
              "Churros", "Tiramisu", "Chocolate Cake"]

# for loop
for idx, item in enumerate(favourites):
    print(idx, item)

# while loop
count = 0
while count < len(favourites):
    print("In while", favourites[count])
    count += 1
