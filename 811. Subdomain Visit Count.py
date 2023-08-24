# Karat Palantir Technologies Intuit
# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, 
# we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com".
# When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is 
# the number of visits to the domain and d1.d2.d3 is the domain itself.

# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.

# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. 
# You may return the answer in any order.
 
# Example 1:

# Input: cpdomains = ["9001 discuss.leetcode.com"]
# Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
# Explanation: We only have one website domain: "discuss.leetcode.com".
# As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        net = defaultdict(int)
        for i in cpdomains:
            rep, domains = i.split(' ')
            rep = int(rep)
            loop_dom = domains.split('.')[::-1]
            tmp = loop_dom[0]
            net[tmp] += rep
            for sub in loop_dom[1:]:
                tmp = f'{sub}.{tmp}'
                net[tmp] += rep
        return [f'{v} {k}' for k, v in net.items()]
        
