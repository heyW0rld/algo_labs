class RBTreeNode:
    def __init__(self):
        self.parent = None
        self.val = None
        self.left = None
        self.right = None
        self.color = "black"  

    def __repr__(self) -> str:
        
        if self.parent:
            parent_val = f'parent: ( {self.parent.color} {self.parent.val} )'
        else:
            parent_val = 'ROOT'

        current_val = f'current: ( {self.color} {self.val} )'

        if self.left and self.right:
            left_right_val = f' [{self.left.color} {self.left.val} <- | -> {self.right.color} {self.right.val}]'
        elif self.left:
            left_right_val = f'[ {self.left.color} {self.left.val} <- | -> None]'
        elif self.right:
            left_right_val = f'[None <- | -> {self.right.color} {self.right.val}]'
        else:
            left_right_val = f'[None <- | -> None]'

        return parent_val + ' -> ' + current_val + ' -> ' + left_right_val


class RBTree:
    def __init__(self):
        self.root = None

    def insert(self, _val: int):
        
        pred = None
        curr = self.root
        while curr:
            pred = curr

            if curr.val == _val:
                return

            if curr.val > _val:
                curr = curr.left
            else:
                curr = curr.right

        
        node = RBTreeNode()
        node.val = _val

        if pred is None:  
            self.root = node
            return

        node.color = "red"
        node.parent = pred
        if pred.val > _val:
            pred.left = node
        else:
            pred.right = node

        
        self.insert_fixup(_node=node)

    def left_rotate(self, _node: RBTreeNode):
        x = _node
        y = x.right

        x_parent = x.parent
        if x_parent is None:
            self.root = y
        else:
            if x is x_parent.left:
                x_parent.left = y
            else:
                x_parent.right = y
        y.parent = x_parent
        x.parent = y

        b = y.left
        if b:
            b.parent = x

        x.right = b
        y.left = x

    def right_rotate(self, _node: RBTreeNode):
        x = _node
        y = x.left

        x_parent = x.parent
        if x_parent is None:
            self.root = y
        else:
            if x is x_parent.left:
                x_parent.left = y
            else:
                x_parent.right = y
        x.parent = y
        y.parent = x_parent

        b = y.right
        if b:
            b.parent = x
        x.left = b
        y.right = x

    def insert_fixup(self, _node: RBTreeNode):
        z = _node
        try:
            while z.parent and (z.parent.color == "red"):
                if z.parent == z.parent.parent.left:
                    y = z.parent.parent.right
                    if y and (y.color == "red"):
                        z.parent.color = "black"
                        y.color = "black"
                        z.parent.parent.color = "red"
                        z = z.parent.parent
                    else:
                        if z == z.parent.right:
                            z = z.parent
                            self.left_rotate(_node=z)
                        z.parent.color = "black"
                        z.parent.parent.color = "red"
                        self.right_rotate(_node=z.parent.parent)
                else:
                    
                    y = z.parent.parent.left
                    if y and (y.color == "red"):
                        z.parent.color = "black"
                        y.color = "black"
                        z.parent.parent.color = "red"
                        z = z.parent.parent
                    else:
                        if z == z.parent.left:
                            z = z.parent
                            self.right_rotate(_node=z)
                        z.parent.color = "black"
                        z.parent.parent.color = "red"
                        self.left_rotate(_node=z.parent.parent)

            self.root.color = "black"
        except:
            exit(-9)

    def tree_minimum(self, node):
        assert not self.empty()

        while node.left:
            node = node.left
        return node

    def tree_maximum(self, node):
        assert not self.empty()

        while node.right:
            node = node.right
        return node

    def min(self):
        if self.root:
            return self.tree_minimum(self.root).val
        else:
            return None

    def max(self):
        if self.root:
            return self.tree_maximum(self.root).val
        else:
            return None

    def empty(self):
        if self.root:
            return False
        else:
            return True

    def rb_transplant(self, u, v):
        if u.parent is None:
            
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if not v is None:
            v.parent = u.parent

    def rb_delete_fixup(self, x):
        while x is not self.root and x.color == 'black':
            if x is x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def rb_delete(self, _val: int):
        
        if _val not in self:
            return

        
        z = self.root
        while z.val != _val:
            if z.val > _val:
                z = z.left
            else:
                z = z.right

        
        empty_x = RBTreeNode()
        empty_x.color = 'black'

        y = z
        y_original_color = y.color
        if (z.left is None) and (z.right is None):
            x = empty_x
            x.parent = z.parent
            z.right = x
            self.rb_transplant(z, z.right)
        elif z.left is None:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right is None:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color

            
            
            if y.right:
                
                x = y.right
            else:
                
                x = empty_x
                x.parent = y
                y.right = x

            if y.parent is z:
                
                
                x.parent = y
            else:
                
                
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            
            
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'black':
            self.rb_delete_fixup(x)

        if empty_x.parent:
            
            self.rb_transplant(empty_x, None)

    def rec_print_tree(self, node):
        print(node)
        if node.left:
            self.rec_print_tree(node.left)
        if node.right:
            self.rec_print_tree(node.right)

    def rec_print_sort_tree(self, node):
        if node.left:
            self.rec_print_sort_tree(node.left)

        
        print(node.val, end=' ')

        
        if node.right:
            self.rec_print_sort_tree(node.right)

    def print_tree(self):
        if self.root:
            self.rec_print_tree(self.root)
        else:
            print('Empty tree')

    def print_sort_tree(self):
        if self.root:
            self.rec_print_sort_tree(self.root)
        else:
            print('Empty tree')

    

    def __contains__(self, item):
        curr = self.root
        while curr:
            if curr.val == item:
                return True

            if curr.val > item:
                curr = curr.left
            else:
                curr = curr.right

        return False

def main():
    tree = RBTree()
    nodes_vals = [9, 10, 3, 2, 6, 7, 5, 8, 11,
                  1, 4, 12, 13, 15, 14, 16]
    
    for val in nodes_vals:
        print("val = ", val)
        tree.insert(val)

    tree.print_tree()
    print()

    tree.rb_delete(11)

    tree.print_tree()

    print()
    print()
    print('Check 100:', 100 in tree)
    print('Check 12:', 12 in tree)

    print('Min item:', tree.min())
    print('Max item:', tree.max())

    tree.print_sort_tree()


if __name__ == '__main__':
    main()