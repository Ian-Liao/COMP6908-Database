import json
import os

INDEX_PATH = "../index/"


def dfs(filename, indent_no):
    with open(os.path.join(INDEX_PATH, filename)) as f:
        content = f.readlines()[0]
        data = json.loads(content)
        print(" " * indent_no, filename, ": ", data)
        if data[0] == "I":
            for entry in data[2]:
                if entry.endswith(".txt"):
                    dfs(entry, indent_no + 2)


def displayTree(fname="page06.txt"):
    indent_no = 0
    with open(os.path.join(INDEX_PATH, fname)) as f:
        content = f.readlines()[0]
        data = json.loads(content)
        print(" " * indent_no, fname, ": ", data)
        if data[0] == "I":
            for entry in data[2]:
                if entry.endswith(".txt"):
                    dfs(entry, indent_no + 2)


def displayTable(rel, fname):
    pass


if __name__ == "__main__":
    displayTree()
