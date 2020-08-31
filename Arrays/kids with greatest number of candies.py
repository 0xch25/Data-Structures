'''Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation:
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids.
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.
Kid 3 has 5 candies and this is already the greatest number of candies among the kids.
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies.
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. '''


def kidsWithCandies(candies,extraCandies):
    result = []
    m = max(candies)
    for i in range(len(candies)):
        if (candies[i] + extraCandies) < m:
            result.append('false')
        else:
            result.append('true')
    return result

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies,extraCandies))