import os
for i in range (1024, 3072, 128):
    # os.remove(f"files/size_{i}.txt")
    with open(f"files/size_{i}.txt", "w") as file:
        file.write("A"*i)