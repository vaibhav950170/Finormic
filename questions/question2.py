class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        a, b = 0, 0;
        for i in range(len(A)):
            if (A[i] == '(' and A[i + 2] == ')'):
                return 1;
            if (A[i] == '*' or A[i] == '+' or
                A[i] == '-' or A[i] == '/'):
                a += 1;
            if (A[i] == '('):
                b += 1;
        
        if (b > a):
            return 1;
        return 0;