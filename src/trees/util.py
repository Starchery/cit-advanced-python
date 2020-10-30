# Secret utility to pretty print a tree.
# We did not go over this.
# This is just so we can see what our
# trees look like.

from typing import List, Optional, Tuple
from .tree import Tree, Node


def pretty_print(t: Tree):
    lines = _build_tree_string(t.root, 0, False, "-")[0]
    return "\n" + "\n".join((line.rstrip() for line in lines))


def _build_tree_string(
    root: Optional[Node],
    curr_index: int,
    index: bool = False,
    delimiter: str = "-",
) -> Tuple[List[str], int, int, int]:

    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if index:
        node_repr = f"{curr_index}{delimiter}{root.data}"
    else:
        node_repr = str(root.data)

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = _build_tree_string(
        root.left, 2 * curr_index + 1, index, delimiter
    )
    r_box, r_box_width, r_root_start, r_root_end = _build_tree_string(
        root.right, 2 * curr_index + 2, index, delimiter
    )

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root: int = (l_root_start + l_root_end) // 2 + 1
        line1.append(" " * (l_root + 1))
        line1.append("_" * (l_box_width - l_root))
        line2.append(" " * l_root + "/")
        line2.append(" " * (l_box_width - l_root))
        new_root_start: int = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(" " * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append("_" * r_root)
        line1.append(" " * (r_box_width - r_root + 1))
        line2.append(" " * r_root + "\\")
        line2.append(" " * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = " " * gap_size
    new_box = ["".join(line1), "".join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line: str = l_box[i] if i < len(l_box) else " " * l_box_width
        r_line: str = r_box[i] if i < len(r_box) else " " * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end
