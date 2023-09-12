import os

w = ["H071231021", "H071231047", "H071231091", "H071231044", "H071231025", "H071231073"]

for i in w:
    os.mkdir(i)
    with open(i + "/readme.md", "w") as f:
        f.write(" ")