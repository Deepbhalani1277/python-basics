import os

if (not os.path.exists("modules/data")):
    os.mkdir("modules/data")

# for i in range(1,100):
    # os.mkdir(f"modules/data/data{i}")
    # os.rmdir(f"Data{i}")
    # os.rename(f"modules/data/data{i}", f"modules/data/day{i}")
    # os.rmdir(f"modules/data/day{i}")
folders = os.listdir("modules/data")
for i in folders:
    print(os.listdir(f"modules/data/{i}"))