class Solution:
    def longestMountain(self, arr: list[int]) -> int:

        n = len(arr)
        maxlength = 0

        for i in range(1, n - 1):

            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:

                start = i - 1
                end = i + 1

                while start > 0 or end < n - 1:

                    if (start > 0 and end < n - 1 and
                        arr[start] > arr[start - 1] and
                        arr[end] > arr[end + 1]):

                        start -= 1
                        end += 1

                    elif start > 0 and arr[start] > arr[start - 1]:
                        start -= 1

                    elif end < n - 1 and arr[end] > arr[end + 1]:
                        end += 1

                    else:
                        break

                length = end - start + 1
                maxlength = max(maxlength, length)

        return maxlength