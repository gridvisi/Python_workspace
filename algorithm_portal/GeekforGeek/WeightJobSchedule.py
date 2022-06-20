
# https://www.geeksforgeeks.org/weighted-job-scheduling/
'''
Input: Number of Jobs n = 4
       Job Details {Start Time, Finish Time, Profit}
       Job 1:  {1, 2, 50}
       Job 2:  {3, 5, 20}
       Job 3:  {6, 19, 100}
       Job 4:  {2, 100, 200}
Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3
but the profit with this schedule is 20+50+100 which is less than 250.

s = '1287351114'
s = "25238273112731"
#s = '23653514'
roadmap = ['23653514','1287351114',"25238273112731"]
'''

jobs = {
       0:[1, 2, 50, 0],
       1:[3, 5, 20, 0],
       2:[6, 19, 100, 0],
       3:[2, 100, 200, 0]
       }
#[(0, [1, 2, 50, 0]), (1, [3, 5, 20, 0]), (2, [6, 19, 100, 0]), (3, [2, 100, 200, 0])]
jobstart = sorted(jobs.items(),key=lambda x:x[1][1])
print(jobstart)

def recur(jobs):
    prev = 0
    jobstart = sorted(jobs.items(),key=lambda x:x[1][1])[::-1]
    for i,sub in enumerate(jobstart):
        if i == 0:
            key = sub[0]
            jobs[key][3] = sub[1][2]
            prev = key
        else:

            if jobs[sub[0]][1] <= jobs[prev][0]:
                MAX = max(jobstart[:i + 1], key=lambda x: x[1][3])
                print(sub[1][2], 'MAX = ', MAX[1][3])
                jobs[sub[0]][3] += MAX[1][3]
                print('jobs = ',jobs)
            else:
                s = [i for i in jobstart[:i + 1] if jobs[sub[0]][2] <= i[1][0]]
                if s:
                    MAX = max(jobstart[:i + 1], key=lambda x: x[1][3])
                    jobs[sub[0]][3] == sub[1][2] + MAX[1][3]
                else:
                    jobs[sub[0]][3] == sub[1][2]
    return jobs #jobstart

print(recur(jobs))