class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        if len(tree) == 0: return 0
        start = new_start = 0
        type_a , type_b = tree[0], -1
        res = 1
        for i in range(1, len(tree)):
            if i == 0: continue
            if type_b == -1 and type_a != tree[i]:
                type_b = tree[i]
            elif tree[i] != type_a and tree[i] != type_b:
                start = new_start
                type_a = tree[i-1]
                type_b = tree[i]

            res = max(res, i-start+1)

            if tree[i] != tree[i-1]: new_start = i

        return res
