class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def mergeSort(arr):

            # Base Case
            if len(arr) <= 1:
                return arr

            # Divide
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            # Recursively sort both halves
            left = mergeSort(left)
            right = mergeSort(right)

            # Merge the sorted halves
            return merge(left, right)

        def merge(left, right):

            ans = []
            i = 0
            j = 0

            # Compare elements from both arrays
            while i < len(left) and j < len(right):

                if left[i] <= right[j]:
                    ans.append(left[i])
                    i += 1
                else:
                    ans.append(right[j])
                    j += 1

            # Add remaining elements from left
            while i < len(left):
                ans.append(left[i])
                i += 1

            # Add remaining elements from right
            while j < len(right):
                ans.append(right[j])
                j += 1

            return ans

        return mergeSort(nums)