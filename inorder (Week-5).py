class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key
def printInorder(root):

	if root:
		printInorder(root.left)
		print(root.val)
		printInorder(root.right)
		

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Inorder traversal of binary tree is:")
printInorder(root)


'''OUTPUT-
Inorder traversal of binary tree is:
4
2
5
1
3
'''
