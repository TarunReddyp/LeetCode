class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)
        #sorting capacity array
        capacity.sort()
        count = 0
        for i in range(len(capacity)-1,-1,-1):
            total_apples -= capacity[i]
            count += 1
            if total_apples <=0:
                return count
        return count
