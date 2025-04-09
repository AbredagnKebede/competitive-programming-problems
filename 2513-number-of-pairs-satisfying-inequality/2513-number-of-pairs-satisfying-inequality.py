class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [a - b for a, b in zip(nums1, nums2)]

        def merge_sort(start, end):
            if start >= end:
                return 0

            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)

            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and arr[i] > arr[j] + diff:
                    j += 1
                count += (end - j + 1)

            # Merge step
            temp = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= end:
                temp.append(arr[j])
                j += 1
            for k in range(len(temp)):
                arr[start + k] = temp[k]

            return count

        return merge_sort(0, len(arr) - 1)
