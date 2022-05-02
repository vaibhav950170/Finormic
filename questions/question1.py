class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        A.sort()
        n = len(A)
        closest = A[0] + A[1] + A[n - 1]
        for i in range(0, n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                current_sum = A[i] + A[j] + A[k]
                if current_sum <= B:
                    j += 1
                else:
                    k -= 1
                if abs(closest - B) > abs(current_sum - B):
                    closest = current_sum
        return closest