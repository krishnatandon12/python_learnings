# Print the time taken by a nested loop to run over certain range.

import time
start_time = round((time.time()), 2)
print("start_time", start_time)

# outer_loop
for x in range(1000):
    # inner_loop
    for y in range(1000):
        print(y, end=" ")
    print()

print(round((time.time() - start_time), 2))
