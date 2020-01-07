#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stak = []
        self.data=[]

# solution1 fastest
    def push(self, x: int) -> None:
        self.data.append(x)
        if self.min_stak :
            if x < self.min_stak[-1] :
                self.min_stak.append(x)
            else:
                self.min_stak.append(self.min_stak[-1])
        else:
            self.min_stak.append(x)
        
# solution1 fastest
    # def push(self, x: int) -> None:
    #     self.data.append(x)
    #     if self.min_stak and self.min_stak[-1] < x:
    #             self.min_stak.append(self.min_stak[-1])
    #     else:
    #         self.min_stak.append(x)
# solutoin 2
    # def push(self, x: int) -> None:
    #     self.data.append(x)
    #     if len(self.min_stak)==0 or x < self.min_stak[-1]:
    #             self.min_stak.append(x)
    #     else:
    #         self.min_stak.append(self.min_stak[-1])
        

    def pop(self) -> None:
        if self.data:
            self.min_stak.pop()
            return self.data.pop()
        return None
        

    def top(self) -> int:
        if self.data :
            return self.data[-1]
        

    def getMin(self) -> int:
        return self.min_stak[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

