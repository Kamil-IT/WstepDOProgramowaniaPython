from main import *
random.seed(12)


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val): 
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals


def get_params(r_list, p):
    if p == 1:
        return get_masa(r_list)
    elif p == 2:
        return get_zasieg(r_list)
    elif p == 3:
        return get_rozdzielczosc(r_list)


robots = multiple_robots(10)

param = int(input('masa/zasięg/rozdzielczość: [1,2,3]: '))
nodes = get_params(robots, param)
print(nodes, '\n')
bst = array_to_bst(nodes) # 1
bst.display()
bst.delete(530)
print('delete 530')
bst.display()

bst.insert(33)
bst.display()

bst.delete(648)
print('delete 648')
bst.display()
print('\n')
print(nodes)


print('road to gold')
search(bst, 928)
print(way[0].display())

print('IN order: ', bst.depthFirstSearch_INorder())
print()
print('PRE order:', bst.depthFirstSearch_PREorder())
print()
print('POST order:', bst.depthFirstSearch_POSTorder())
