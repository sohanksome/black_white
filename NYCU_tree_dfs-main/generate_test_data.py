import random
import pickle

def generate_test_data(num_nodes):
    root_value = random.randint(1, 1000)
    test_data = [root_value]    
    # print(root_value)
    nodes = list(range(1, num_nodes + 1))
    random.shuffle(nodes)
    
    tree = {root_value: []}
    
    for i in range(num_nodes - 1):
        parent = random.choice(nodes[:i+1])
        new_node = nodes[i+1]
        if parent in tree:
            tree[parent].append(new_node)
            tree[new_node] = []
            test_data.append((parent, new_node))
        else:
            # 如果 parent 不在树中，则选择其他节点作为 parent
            other_parent = random.choice(list(tree.keys()))
            # print('other_parent', other_parent)
            tree[other_parent].append(new_node)
            tree[new_node] = []
            test_data.append((other_parent, new_node))
    
    return test_data

# 生成多个测试案例
def test_data(num_test_cases):
    test_data = []
    for _ in range(num_test_cases):
        num_nodes = random.randint(2, 30)
        test_case = generate_test_data(num_nodes)
        test_data.append(test_case)
    return test_data

if __name__ == '__main__':
    with open('test_data.pkl', 'wb') as file:
        pickle.dump(test_data(5), file)
