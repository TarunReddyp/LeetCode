class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        #sorting events by start time
        events.sort()
        n = len(events)
        """ recursive approach
        def solve(ind, count):
            #base cases
            if count == 2 or ind == n:
                return 0
            #choice 1 : skip
            res = solve(ind+1, count)
            #choice 2 : pick
            current_end = events[ind][1]
            #Rule: # Find next index where events[next_ind][0] > events[ind][1]
            next_ind = ind + 1
            while next_ind < n and events[next_ind][0]<=current_end:
                next_ind += 1
            res = max(res, events[ind][2] + solve(next_ind, count + 1))
            return res
        return solve(0,0) 
        """ 
        """
        #applying memoization and changing linear search to binary search
        # creating memo dictionary
        memo = {}
        def solve(ind, count):
            #base cases
            if count == 2 or ind == n:
                return 0
            if (ind,count) in memo :
                return memo[(ind,count)]
            #choice 1 : skip
            res = solve(ind+1, count)
            #choice 2 : pick
            current_end = events[ind][1]
            #Rule: # Find next index where events[next_ind][0] > events[ind][1]
            low = ind+1
            high = n-1
            next_ind = n
            while low<=high:
                mid = (low+high)//2
                if events[mid][0]>current_end:
                    next_ind = mid
                    high = mid-1
                else:
                    low = mid + 1
            res = max(res, events[ind][2] + solve(next_ind, count + 1))
            #storing in memo before returning
            memo[(ind,count)] = res
            return res
        return solve(0,0) 
        """
        """
        #optimising  it using bottom-up DP approach
        #initialise DP table : dp[event_index][picks_left]
        dp = [[0] * 3 for _ in range(n + 1)]
        for ind in range(n - 1, -1, -1):
            for k in range(1, 3):
                 #choice 1 : skip
                skip = dp[ind+1][k]
                #choice 2 : pick
                current_end = events[ind][1]
                current_val = events[ind][2]
                #Rule: # Find next index where events[next_ind][0] > events[ind][1]
                low = ind+1
                high = n-1
                next_ind = n
                while low<=high:
                    mid = (low+high)//2
                    if events[mid][0]>current_end:
                        next_ind = mid
                        high = mid-1
                    else:
                        low = mid + 1
                pick = current_val + dp[next_ind][k-1]
                dp[ind][k] = max(skip,pick)
        return dp[0][2]
        """
        #since number of events are fixed i can simply use 1d dp suffix max approach
        #for each event I pick, what is the best single event I can pick afterward.
        # suffix_max[i] stores the highest value of any single event from index i to n-1
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(events[i][2], suffix_max[i + 1])
        max_sum = 0
        # 3. Iterate through each event and find its best non-overlapping partner
        for ind in range(n):
            current_val = events[ind][2]
            current_end = events[ind][1]
            # choice 1: Only pick the current event
            max_sum = max(max_sum, current_val)
            # choice 2: Pick current event + best available event starting after current_end
            low = ind+1
            high = n-1
            next_ind = n
            while low<=high:
                mid = (low+high)//2
                if events[mid][0]>current_end:
                    next_ind = mid
                    high = mid-1
                else:
                    low = mid + 1
            # If a valid next event exists, add its precomputed max value
            if next_ind < n:
                max_sum = max(max_sum, current_val + suffix_max[next_ind])
        return max_sum




    
      
        

        

        
