'''
https://brilliant.org/daily-problems/best-candidate/
In the latest elections for the mayor of Brilliant Village,
\num{12343}12343 citizens voted for one of the six candidates,
and each candidate received a different number of votes.\\[0.8em]
What is the smallest number of votes that could have been cast
for the winning candidate?

2058
2058
2059
2059
2060
2060
2061
2061

'''
votes = 12343
person = 6
average = votes//person

# if smallest win_votes:
#     (votes - smallest)/5 < smallest
#therefore: votes - smallest < 5* smallest
# smallest > votes/6
print(votes/6,votes//6)

'''
The winning candidate will receive a rather small number of votes when the distribution of votes among the six candidates is close to one another. Since \frac{\num{12343}}6 \approx 2057, 
6
12343
​
 ≈2057, when the election is close, we expect each candidate to receive around this many votes.

Since each candidate receives a different number of votes, we expect 20572057 to be in the middle of the pack. For example, the vote distribution could be this:
2055, 2056, 2057, 2058, 2059, 2060.
2055,2056,2057,2058,2059,2060.
However, the sum of these vote totals is \num{12345}12345 — too many by 22 — and thus it doesn't work. So, let's try the following distribution with each number reduced by 1:1:
2054, 2055, 2056, 2057, 2058, 2059
2054,2055,2056,2057,2058,2059
with a total of \num{12339}.12339. But this time there are \num{12343}-\num{12339}=412343−12339=4 votes left to be accounted for. So, we have at hand a variation of the "pigeonhole principle" problem where all 66 pigeonholes (number of candidates) are already occupied, with 44 more pigeons (votes) to fill in under the constraint that the most crowded pigeonhole (winning candidate) has the smallest possible number of pigeons (votes):

Filling 11 out of the 44 remaining votes in the vote total other than 20592059 violates the constraint of "different number of votes," so it must go to 2059,2059, making the number 2060.2060.
Filling 11 out of the now 33 remaining votes in the vote total 20602060 violates the constraint of "the smallest possible vote total" for the winner, so it must go to 20582058 ((making it 2059)2059) by the same logic as above.
Following a similar fashion, we reach the final distribution of votes that will look like
2054, 2055, 2057, 2058, 2059, 2060.
2054,2055,2057,2058,2059,2060.
Note that the smallest two could be (2053, 2056)(2053,2056) rather than (2054, 2055),(2054,2055), making the distribution
2053, 2056, 2057, 2058, 2059, 2060.
2053,2056,2057,2058,2059,2060.
Either way, our answer is 2060.2060.
'''

average = 2057
candiates = [2057] * 6
for i in range(6):
    candiates[i] -= i
print(candiates,votes - sum(candiates),sum(candiates)) #12327

ans = [i+(votes - sum(candiates))//6 for i in candiates]
print(ans,sum(ans))  #12339
#rest of 3 assign candidates[0:3]


