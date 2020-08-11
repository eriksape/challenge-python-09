from typing import List


class Solution:

    def duplicate_zeros(self, arr: List[int]):

      index = 0
      zeroes = 0
      limit = len(arr) - 1

      while True:
        if arr[index] == 0:
          zeroes += 1
        index += 1
        if index + zeroes >= limit:
          break

      while limit - zeroes >= 0 and zeroes >= 0:
        arr[limit] = arr[limit - zeroes]
        if arr[limit] == 0 and limit - zeroes < index:
          arr[limit - 1] = 0
          limit -= 1
          zeroes -= 1
        limit -= 1

      return arr
 
