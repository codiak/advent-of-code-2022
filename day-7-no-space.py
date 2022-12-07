from utils import fetchInput
from string import ascii_lowercase
import time
import re

page = fetchInput("https://adventofcode.com/2022/day/7/input")
text_data = page.text

# text_data = """
# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# """

text_rows = list(re.split('\n', text_data))

class Node(object):
    # path = ''
    # size = 0
    # parent = None
    # children = []

    def __init__(self, path, size, parent):
        self.path = path
        self.size = size
        self.parent = parent
        self.children = []

    def __str__(self):
        return '<%s, %d>' % (self.path, self.size)

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return self.children

# root_node = { 'path': "/", 'size': 0, 'children': [], 'parent': None }
root_node = Node('/', 0, None)

# Find all of the directories with a total size of at most 100000.
# What is the sum of the total sizes of those directories?
current_node = root_node
sizes = {}
# def processStep(txt):
#     if re.match("^$ ls", txt):
#         # update nodes
#     elif re.match("^$ cd ..", txt):
#         # go up
#     elif re.match("^$ cd", txt):
#         # set node
#     elif re.match('^\d+', txt:
#         # add file node
#     elif re.match("^dir\w", txt):
#         # add directory node
#     else:
#         print("Empty line or done?")

def updateSizes():
    dir_size = 0
    for child in current_node.get_children():
        dir_size += getattr(child, 'size')
    print(f'Update "{current_node}" size to: {dir_size}')
    setattr(current_node, 'size', dir_size)
    parent = getattr(current_node, 'parent')
    if parent:
        # if getattr(parent, 'path') == '/':
        parent_path = getattr(parent, 'path')
        sizes[f'{parent_path}/{getattr(current_node, "path")}'] = dir_size

i = 0
# build tree
while i < len(text_rows):
    txt = text_rows[i]
    i += 1
    if re.match("^\$ ls", txt):
        # update nodes
        continue
    elif re.match("^\$ cd \\.\\.", txt):
        # before going up, update sizes
        updateSizes()
        # go up
        print('Go up')
        current_node = getattr(current_node, 'parent')
    elif re.match("^\$ cd \/", txt):
        # root
        continue
    elif re.match("^\$ cd", txt):
        updateSizes()
        # set node
        go_to = txt.split()[2]
        print(f'Go to: {go_to}')
        for child in current_node.get_children():
            if getattr(child, 'path') == go_to:
                current_node = child
    elif re.match('^\d+', txt):
        # add file node
        parts = txt.split()
        print(f'Add file: {parts[1]}')
        # new = { 'path': parts[1],
        #         'size': int(parts[0]),
        #         'children': [],
        #         'parent': current_node }
        new = Node(parts[1], int(parts[0]), current_node)
        # current_node['children'].append(new)
        current_node.add_child(new)
    elif re.match("^dir\s", txt):
        # add directory node
        parts = txt.split()
        print(f'Add dir: {parts[1]}')
        new = { 'path': parts[1],
                'size': 0,
                'children': [],
                'parent': current_node }
        new = Node(parts[1], 0, current_node)
        # current_node['children'].append(new)
        current_node.add_child(new)
    else:
        print(f"Empty line or done? {txt}")
        updateSizes()

# traverse tree and update sizes


print(root_node)
print(sizes)

total_small = 0
for key, value in sizes.items():
    print(value)
    if value < 100000:
        total_small += value

print(f"<100000 total: {total_small}")
