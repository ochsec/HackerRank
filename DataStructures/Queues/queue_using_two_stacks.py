# Enter your code here. Read input from STDIN. Print output to STDOUT
import os

# class Stack:
#     def __init__(self):
#         self.count = 0
#         self.items = {}

#     def __str__(self):
#         if self.is_empty():
#             return ''
#         s = str(self.items[0])
#         for i in range(1, self.count):
#             s = s + ',' + str(self.items[i])
#         return s

#     def push(self, element):
#         self.items[self.count] = element
#         self.count = self.count + 1

#     def pop(self):
#         if self.is_empty():
#             return None
#         self.count = self.count - 1
#         last = self.items[self.count]
#         del self.items[self.count]
#         return last

#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.items[self.count - 1]

#     def size(self):
#         return self.count

#     def is_empty(self):
#         return self.count == 0

#     def clear(self):
#         self.items = {}
#         self.count = 0

def process(queries):
    A = [] # Queue stack
    B = [] # Dequeue stack
    output = [] # The numbers to return to be printed
        
    for q in queries:
        if q[0] == 1:
            # Enqueue
            if len(A) == 0:
                while len(B) != 0:
                    A.append(B.pop())
            A.append(q[1])
        elif q[0] == 2:
            # Dequeue
            if len(B) == 0:
                while len(A) != 0:
                    B.append(A.pop())
            B.pop()
        else:
            if len(B) == 0:
                while len(A) != 0:
                    B.append(A.pop())               
            output.append(B[len(B) - 1])
       
    return output
                
                
if __name__ == '__main__':
    lines = []
    queries = []
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    for i in range(n):
        lines.append(input())

    for l in lines:
        args = l.split(' ')
        args = list(map(int, args))
        queries.append(args)
        
    output = process(queries)
    
    for num in output:
        print(num)
    #     fptr.write(f"{num}\n")
    # fptr.close()