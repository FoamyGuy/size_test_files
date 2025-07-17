import os
for i in range (3072, (1024*6)+1, 128):
    # os.remove(f"files/size_{i}.txt")
    with open(f"files/size_{i}.txt", "w") as file:
        file.write("A"*i)