class Solution:
    def fairCandySwap(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        '''
        x is the number Alice would gave to Bob
        y is the number Bob would gave to Alice
        then
        A - x + y = B - y + x
        then
        x - y = (A - B) / 2 = dif
        then
        y = x - dif
        '''
        dif = (sum(A) - sum(B)) // 2
        b = set(B)
        for i in A:
            if i - dif in b:
                return (i, i-dif)
