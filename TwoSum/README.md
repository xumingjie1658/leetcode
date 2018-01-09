A easy description for this problem is finding two specific elements which sum is the target number.

we can easily use brute force search to find the two elements. But this solution costs O(n^2) time complexity to traverse the nums array twice. Maybe it will make 'Time Limit Exceeded' in the LeetCode online judge system.

There is an obvious feature that if we choose the first element of sum, we definitely know which element we want to find. So the real process of this algorithm is:

1. choose the first element of sum
2. find another element of sum in the nums array or not
3. if found, return the two index
4. if not found, choose a new first element until the nums array is traversed once

time complexity: n * n (time traverse the nums array * time finding another element)

But if we record all the mapping relations in a map, then we can cut the time finding another element down to O(1). The map building process costs O(n)

So the time complexity is: O(n) + O(n) * O(1) = O(n)

We have a better solution...

More:

Approach #3 (One-pass Hash Table) [Accepted]

It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.

```
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No two sum solution");
}
```