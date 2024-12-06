import pickle

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = root
        self.enum = 0
        self.max_path = []

    def add_node(self, parent_value, new_value):
        parent = self.find_node(parent_value)
        if parent is not None:
            new_node = TreeNode(new_value)
            parent.children.append(new_node)
            return True
        else:
            return False
        
    def find_node(self, value):
        return self._find_node_recursive(self.root, value)

    def _find_node_recursive(self, node, value):
        if node.value == value:
            return node
        for child in node.children:
            found_node = self._find_node_recursive(child, value)
            if found_node is not None:
                return found_node
        return None
    
    def print_tree(self, node, level=0):
        if not node:
            return
        chunk = '  ' if level == 0 else '|_'
        print("  " * level + chunk + str(node.value))
        for child in node.children:
            self.print_tree(child, level + 1)
    
    def print_max_path(self):
        for level, node in enumerate(self.max_path):
            chunk = '  ' if level == 0 else '|_'
            print("  " * level + chunk + str(node.value))
        
            
    def find_maximum_path(self):
        """
        呼叫self.dfs_find_maximum_path來做tree dfs,
        然後記錄到self.max_path和max_sum裡
        
        Return: 最大總和
        """
        
        self.max_path, max_sum = self.dfs_find_maximum_path(self.root)      # 會回傳最大總和路徑和最大總和
        return max_sum
    
    def dfs_find_maximum_path(self, node: TreeNode): # 會回傳最大總和路徑和最大總和
        """
        node: 
            1. node.value: 此節點的數值
            2. node.children: 此節點的子節點們
            
        max_value: 用來存放最大累積子節點總和的大小
        max_sub_path: 用來紀錄最大總和路徑上的節點們
        """
        
        max_value = -float('inf')
        max_sub_path = []
        
        # 如果他有子節點
        if len(node.children) > 0:
            # START YOUR CODE #

            for child in node.children:                                     # 對每個子節點:
                tmp_path, tmp_value = self.dfs_find_maximum_path(child)       # 得到子節點的最大總和、最大總和路
                if tmp_value > max_value:                                                     # 更新最大總和、最大總和路
                    max_sub_path = tmp_path
                    max_value = tmp_value
                    
            # END YOUR CODE #
            return [node] + max_sub_path, max_value + node.value            # 做完以後會回傳新增現在節點的最大總和路徑與最大總和
        # 如果沒有 (他是leaf node)
        else:
            # 回傳自己的節點還有數值
            return [node], node.value                                       # [node]代表一個只有node的list

    
if __name__ == '__main__':
    with open('test_data.pkl', 'rb') as test_file:
        test = pickle.load(test_file)
        for t in test:    
            root_value = t[0]
            root_node = TreeNode(root_value)
            tree = Tree(root_node)
            for uv in t[1:]:
                tree.add_node(uv[0], uv[1])
            
            print('\nTree shape:')
            tree.print_tree(tree.root)
            print('\nMaximum path:')
            try:
                maximum = tree.find_maximum_path()
                assert maximum != float('-inf')      
                tree.print_max_path()
                print(f'\nMaxima: {maximum}')
                print('你寫對囉!!! 你超電!')
            except:
                print('你寫錯了!')
        
    