import json
import os

INDEX_PATH = "../index/"
TREE_PIC_PATH = "../treePic/"

TYPE_POS = 0
CONTENT_POS = 2


def dfs(filename, indent_no, distfile):
    with open(os.path.join(INDEX_PATH, filename)) as f:
        content = f.readlines()[0]
        distfile.write(" " * indent_no + filename + ": " + content)
        data = json.loads(content)
        if data[TYPE_POS] == "I":
            for entry in data[CONTENT_POS]:
                if entry.endswith(".txt"):
                    dfs(entry, indent_no + 2, distfile)


def displayTree(fname="page06.txt"):
    indent_no = 0
    with open(os.path.join(INDEX_PATH, fname)) as root, open(os.path.join(TREE_PIC_PATH, "Suppliers_sid.txt"), "w") as tree_pic:
        content = root.readlines()[0]
        tree_pic.write(" " * indent_no + fname + ": " + content)
        data = json.loads(content)
        if data[TYPE_POS] == "I":
            for entry in data[CONTENT_POS]:
                if entry.endswith(".txt"):
                    dfs(entry, indent_no + 2, tree_pic)


def displayTable(rel, fname):
    pass


if __name__ == "__main__":
    displayTree()
