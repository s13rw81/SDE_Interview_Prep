# DSA Notes
Data Structures are of two types, linear, non-linear. Examples of linear data structures are, arrays, linked lists, stacks, queues. Examples of non-linear data structures are graphs, and trees.
Linear data structures are of two types, static and dynamic. Static data structures such as an array have a fixed memory size. Non static data structures are queues, stacks, linked lists whose memory can be updated at runtime. Foe example, new nodes can be added to a linked list.

### Factors considered while selecting data structures:
- type of data that needs to be stored
- cost of operations
- memory usage

---
## <u>Non Linear Data Structures</u>

## Tree
A _tree_ data structure is defined as a collection of objects or entities known as _nodes_ that are linked together to represent or simulate hierarchy.
A tree data structure is a non-linear data structure because it does not store data in a sequential manner.
Each node contains some data and the link or reference of other nodes that can be called children. 
```python
class Node:
	def __init__(self, data):
		self.data = data
		self.children = list()
```
- The _root node_ is a special node of a tree that does not have a parent node. It generally contains links to all the roots of its subtrees.
- Number of edges: If there are n nodes, then there would n-1 edges. Each node, except the root node, will have atleast one incoming link known as an edge.
- Depth of node x: The depth of node x can be defined as the length of the path from the root to the node x. One edge contributes one-unit length in the path. So, the depth of node x can also be defined as the number of edges between the root node and the node x. The root node has 0 depth.
- Height of node x: The height of node x can be defined as the longest path from the node x to the leaf node.
- A collection of disjoint trees is called a [forest](https://cdn.programiz.com/sites/tutorial2program/files/forest_0.png).