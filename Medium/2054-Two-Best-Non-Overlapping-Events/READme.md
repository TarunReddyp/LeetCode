# 2054. Two Best Non-Overlapping Events

## 🚀 Problem Description
You are given a 2D integer array of events where `events[i] = [startTime, endTime, value]`. You can choose at most **two non-overlapping events** to attend such that the sum of their values is maximized. 

Two events are non-overlapping if the start time of one is strictly greater than the end time of the other.

[View Problem on LeetCode](https://leetcode.com/problems/two-best-non-overlapping-events/)

## 🧠 My Approach Evolution

### 1. Recursive with Memoization
- **Logic**: Use a `solve(index, count)` function. At each event, we either "Pick" or "Skip." If we pick, we use binary search to find the next valid event index.
- **Complexity**: O(Nlog N) time | O(N) space.

### 2. Bottom-Up Dynamic Programming
- **Logic**: Transition the recursive logic into a 2D table `dp[n+1][3]`. This avoids recursion depth issues and is more iterative.
- **Complexity**: O(N \log N) time | O(N) space.

### 3. Optimized Suffix Maximum (Current Solution)
- **Logic**: Sort events by start time. Precompute a `suffix_max` array where `suffix_max[i]` stores the highest value event from index `i` to the end. For each event, we binary search for the first valid following event and add its precomputed max value.
- **Complexity**: O(N \log N) time | O(N) space.

## 📊 Performance
- **Time Complexity**: O(NlogN) due to sorting and binary search lookups.
- **Space Complexity**: O(N) to store the suffix maximum array.
