# Addiiton of inf logic to deal with the two edge caes that the partition lies on the boundary 

#The logic here was that there is only one possibel way to merge two sorted array into one (Here we are not merging but without merging we are finding the median) therefore only one valid partition exist ! which can satifsy the len_Left(A+B) = len_Right(A+B) and with that the conditions of ineality tha Left_End_A <= Right_start_B and Left_End_B <= Right_Start_A. 

#So our Binary Search on the samller array basically try to find such partition wh make our parameter that stisfy the length constraines then we try to find the partion that satisflies the inequalities !! and accoridingly which inequality is being breached we update our start or end in the binary search !!

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        A = nums1
        B = nums2

        # Binary search on the smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)

        # Number of elements on the left
        half = (total + 1) // 2

        left = 0
        right = len(A)

        while left <= right:

            # Partition of A
            i = (left + right) // 2

            # Partition of B
            j = half - i

            # Boundary elements of A
            if i > 0:
                Aleft = A[i - 1]
            else:
                Aleft = float("-inf")

            if i < len(A):
                Aright = A[i]
            else:
                Aright = float("inf")

            # Boundary elements of B
            if j > 0:
                Bleft = B[j - 1]
            else:
                Bleft = float("-inf")

            if j < len(B):
                Bright = B[j]
            else:
                Bright = float("inf")

            # Check if partition is valid
            if Aleft <= Bright and Bleft <= Aright:

                if total % 2 == 1:
                    return max(Aleft, Bleft)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # A partition is too far right
            elif Aleft > Bright:
                right = i - 1

            # A partition is too far left
            else:
                left = i + 1
        