class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse = True)
        total_happy = 0
        for i in range(k):
            if happiness[i] - i <=0:
                break;
            else:
                total_happy += happiness[i] - i
        return total_happy


        
