__author__ = 'Administrator'
def quick_sort(lst):

    # 递归终点：未排序列表的长度减至1（就剩一个数，不用再排了）
    if len(lst) <= 1:
        return lst

    else:
        # 假设列表的第0元素为pivot
        pivot = lst[0]

        # 列表推导式：对小于/大于pivot的元素，分别组成两个新列表
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]

        # 合并三个列表
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([3,1,4,1,5,9,2,6,5,3,5,8,9,8]))