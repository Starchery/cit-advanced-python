# Binary Search Trees

## Definition

A binary tree with the following constraints.

#### ORDERING
> Every node must satisfy these properties:
>
> * The left subtree of a node only contains *lesser numbers* than that node's.
> * The right subtree of a node only contains *greater numbers* than that node's.

#### RECURSIVE
> Each subtree must also be a valid binary search tree.

## Examples

```
            (2)__
                 \
                  \
                  (4)__
                       \
                        \
                        (8)
                       __|__
                      /     \
                     (5)    (9)
                       \
                       (7)
```


```
            (5)
          ___|___
         /       \
        /         \
      (2)         (8)
         \        /  \
         (4)    (7)  (9)
```

```
            (5)
          ___|___
         /       \
        /         \
      (2)         (8)
     /   \        /  \
   (1)   (4)    (7)  (9)
        /       /
      (3)     (6)
```


## Use cases

Efficient searching, insertion, deletion on trees

## COMPLEXITIES

* Insert **O(height)**

* Delete **O(height)**

* Search **O(height)**
    * How to look for a word in the dictionary?
        1. start in the middle
        2. if the target word is LOWER than the words you see,
            * check the left half of the book and repeat
        3. if the target word is GREATER than the words you see,
            * check the right half of the book and repeat
        4. if you're staring at the word
            * congrats.
    * In each step of the problem, we're narrowing our search

    * **The maximum amt. of steps we take
    is the same as the height of the tree**

* Random access **O(height)**

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
