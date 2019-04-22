# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int("".join(map(str,digits)))
        res=res+1
        list1=list(map(int,str(res)))
        return list1
