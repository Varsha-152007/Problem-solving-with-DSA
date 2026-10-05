# Problem: Implement Stack using Queues
# Problem Link: https://leetcode.com/problems/implement-stack-using-queues/description/?envType=problem-list-v2&envId=stack
# Date: 5th Oct 2026
# Time taken to solve: 15 mins

#solution
<
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x: int) -> None:
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

   
    def pop(self) -> int:
        return self.q1.popleft()
        

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return not self.q1
      >

