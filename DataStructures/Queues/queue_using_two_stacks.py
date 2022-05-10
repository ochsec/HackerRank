# Enter your code here. Read input from STDIN. Print output to STDOUT
import os

def process(queries):
    Q = [] # Queue stack
    output = [] # The numbers to return to be printed
        
    for q in queries:
        if q[0] == 1:
            # Enqueue
            Q.append(q[1])
        elif q[0] == 2:
            # Dequeue
            Q.pop(0)
        else:
            # Add to output
            output.append(Q[0])
       
    return output
                
if __name__ == '__main__':
    lines = []
    queries = []
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    for i in range(n):
        lines.append(input())
    for l in lines:
        args = l.split(' ')
        args = list(map(int, args))
        queries.append(args)
        
    output = process(queries)
    
    for num in output:
        fptr.write(f"{num}\n")
    fptr.close()
