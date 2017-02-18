class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root is not None:
            #print(self.getHeight(root.right),self.getHeight(root.right),max(self.getHeight(root.right),self.getHeight(root.left)) + 1)
            return max(self.getHeight(root.right),self.getHeight(root.left)) + 1
        else:
            return -1

    def levelOrder(self,root):
        if root.left is not None:
            print(root.left.data, end=' ')
        if root.right is not None:
            print(root.right.data, end=' ')
        if root.left is not None:
            self.levelOrder(root.left)
        if root.right is not None:
            self.levelOrder(root.right)
        
#    def levelOrder(self,root):
#        print(root.data, end=' ')
#        self._levelOrder(root)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)


           
