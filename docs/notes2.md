# PACKAGES

## DIRECTORY STRUCTURE

### Modularization

Considers modules and packages and files and folders **ALL DIFFERENTLY**

## MODULE

Just a .py file

## PACKAGE

Folder containing .py files


### STRUCTURE

"PROJECTFOLDER" is a package

*We have to explicitly tell python that this folder is meant to be a package.*

Python will look for a file called
"__init__.py"
If this file exists, the folder is a package.

The file can be empty, and in fact, it often is.

```
PROJECTFOLDER
|
|-----tests/
|-----|----__init__.py
|-----|----test1.py
|-----|----test2.py
|-----module1.py (import tests.test1)
|-----module2.py
```


# Linked lists

* Very dynamic

* How our program is stored

## Arrays

```python

lst = [1, 2, 3, 4, 5, 6]
lst.append(7)
first = lst[0]
```


`**[1][2][3][4][5][6]**[][][][][][]`


## Linked Lists

```python
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

LinkedList(Node(1)-> Node(2)-> Node(3)-> None)


0     1         2         3     4 5 6 7      8      9 1011
[][1, link->8][None][3, link->2][][][][][2, link->3][][][]
```


# Binary Trees

## Definition

Data structure that represents a hierarchy of unique nodes

Each node has at most 2 children.

### Terminology

**Root node**: The node at the top of the hierarchy

**Parent node**: any node that has nodes under it

**Child node**: any node that has a parent node

**Leaf node**: any node that has no children

## Examples
- Inorder  **(4, 8, 2, 9, 5, 7)**
    1. Print all nodes on left
    2. Print current node
    3. Print all nodes on right
- Preorder **(2, 4, 8, 5, 9, 7)**
    1. Print current node
    2. Print all nodes on left
    3. Print all nodes on right
- Postorder **(7, 9, 5, 8, 4, 2)**
    1. Print all the nodes on the right
    2. Print all nodes on the left
    3. Print current node

```

           ( 2 )     <-- Root node
Left -->  /     \    <-- Right child/branch
         /       \
       (4)       (5)  <-- Child node of (2)
          \      /  \  , Parent node of (9, 7)
          (8)   /    \
               (9)   (7) <-- Leaf node
                            , child node of (5)
```

## Use cases

Modeling something hierarchial,
anything that has a hierarchy

* File systems

* Family trees

* Substrings

* Implement other tree-like data structures

```
        (  Common Ancestor  )
       /                     \
    (Some guy)             (Someone else)
```

## COMPLEXITIES

* Insert **O(n)**

* Delete **O(n)**

* Search **O(n)**

* Random access **O(n)**

* Traversal **O(n)**
    - Inorder
        1. Print all nodes on left
        2. Print current node
        3. Print all nodes on right

    - Preorder
        1. Print current node
        2. Print all nodes on left
        3. Print all nodes on right

    - Postorder
        1. Print all the nodes on the right
        2. Print all nodes on the left
        3. Print current node


