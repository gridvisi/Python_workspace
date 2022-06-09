# A Python implementation of the Banker's Algorithm in Operating Systems using
# Processes and Resources
# {
# "Author: "Biney Kingsley (bluedistro@github.io), bineykingsley36@gmail.com",
# "Date": 28-10-2018
# }
"""
The Banker's algorithm is a resource allocation and deadlock avoidance algorithm
developed by Edsger Dijkstra that tests for safety by simulating the allocation of
predetermined maximum possible amounts of all resources, and then makes a "s-state"
check to test for possible deadlock conditions for all other pending activities,
before deciding whether allocation should be allowed to continue.
[Source] Wikipedia
[Credit] Rosetta Code C implementation helped very much.
 (https://rosettacode.org/wiki/Banker%27s_algorithm)

全文分四部分：

什么是银行家算法？
银行家算法中的数据结构
银行家算法自然语言描述
银行家算法流程图表示
一、什么是银行家算法？
银行家算法是操作系统的经典算法之一，用于避免死锁情况的出现。

它最初是为银行设计的（因此得名），通过判断借贷是否安全，然后决定借不借。

在银行中，客户申请贷款的数量是有限的，每个客户在第一次申请贷款时要声明完成该项目所需的最大资金量，在满足所有贷款要求时，客户应及时归还。银行家在客户申请的贷款数量不超过自己拥有的最大值时，都应尽量满足客户的需要。
用在操作系统中，银行家、出借资金、客户，就分别对应操作系统、资源、申请资源的进程。

每一个新进程进入系统时，必须声明需要每种资源的最大数目，其数目不能超过系统所拥有的的资源总量。当进程请求一组资源时，系统必须首先确定是否有足够的资源分配给该进程，若有，再进一步计算在将这些资源分配给进程后，是否会使系统处于不安全状态如果不会才将资源分配给它，否则让进程等待。
二、银行家算法中的数据结构
为了实现银行家算法，在系统中必须设置这样四个数据结构：

1）Available向量：系统中可利用的资源数目

2）Max矩阵：每个进程对每种资源的最大需求

3）Allocation矩阵：每个进程已分配的各类资源的数目

4）Need矩阵：每个进程还需要的各类资源数

其中三个矩阵间存在下述关系：

Need[i,j] = Max[i,j] - allocation[i, j]
三、银行家算法自然语言描述
将银行家算法的逻辑转化为自然语言：

设Requesti是进程Pi的请求向量，如果Requesti［j］=K，表示进程Pi需要K个Rj类型的资源。当Pi发出资源请求后，系统按下述步骤进行检查：

(1) 若 Requesti[j] ≤ Need[i,j]，转向(2)，否则认为出错（因为它所需的资源数目已超过它所宣布的最大值）。

(2) 若 Requesti[j] ≤ Available[j]，转向(3)，否则须等待（表现为进程Pi受阻）。

(3) 系统尝试把资源分配给进程Pi，并修改下面数据结构中的数值：

Available[j] = Available[j] – Requesti[j]
Allocation[i,j] = Allocation[i,j] + Requesti[j]
Need[i,j] = Need[i,j] –Requesti[j]
(4) 试分配后，执行安全性算法，检查此次分配后系统是否处于安全状态。若安全，才正式分配；否则，此次试分配作废，进程Pi等待。

四、银行家算法流程图表示
最后，用流程图表示银行家算法。此前介绍过如何用流程图描述算法，这里不再赘述，有需要的可以移步查看▼
"""

from __future__ import annotations

import time

import numpy as np

test_claim_vector = [8, 5, 9, 7]
test_allocated_res_table = [
    [2, 0, 1, 1],
    [0, 1, 2, 1],
    [4, 0, 0, 3],
    [0, 2, 1, 0],
    [1, 0, 3, 0],
]
test_maximum_claim_table = [
    [3, 2, 1, 4],
    [0, 2, 5, 2],
    [5, 1, 0, 5],
    [1, 5, 3, 0],
    [3, 0, 3, 3],
]


class BankersAlgorithm:
    def __init__(
        self,
        claim_vector: list[int],
        allocated_resources_table: list[list[int]],
        maximum_claim_table: list[list[int]],
    ) -> None:
        """
        :param claim_vector: A nxn/nxm list depicting the amount of each resources
         (eg. memory, interface, semaphores, etc.) available.
        :param allocated_resources_table: A nxn/nxm list depicting the amount of each
         resource each process is currently holding
        :param maximum_claim_table: A nxn/nxm list depicting how much of each resource
         the system currently has available
        """
        self.__claim_vector = claim_vector
        self.__allocated_resources_table = allocated_resources_table
        self.__maximum_claim_table = maximum_claim_table

    def __processes_resource_summation(self) -> list[int]:
        """
        Check for allocated resources in line with each resource in the claim vector
        """
        return [
            sum(p_item[i] for p_item in self.__allocated_resources_table)
            for i in range(len(self.__allocated_resources_table[0]))
        ]

    def __available_resources(self) -> list[int]:
        """
        Check for available resources in line with each resource in the claim vector
        """
        return np.array(self.__claim_vector) - np.array(
            self.__processes_resource_summation()
        )

    def __need(self) -> list[list[int]]:
        """
        Implement safety checker that calculates the needs by ensuring that
        max_claim[i][j] - alloc_table[i][j] <= avail[j]
        """
        return [
            list(np.array(self.__maximum_claim_table[i]) - np.array(allocated_resource))
            for i, allocated_resource in enumerate(self.__allocated_resources_table)
        ]

    def __need_index_manager(self) -> dict[int, list[int]]:
        """
        This function builds an index control dictionary to track original ids/indices
        of processes when altered during execution of method "main"
            Return: {0: [a: int, b: int], 1: [c: int, d: int]}
        >>> (BankersAlgorithm(test_claim_vector, test_allocated_res_table,
        ...     test_maximum_claim_table)._BankersAlgorithm__need_index_manager()
        ...     )  # doctest: +NORMALIZE_WHITESPACE
        {0: [1, 2, 0, 3], 1: [0, 1, 3, 1], 2: [1, 1, 0, 2], 3: [1, 3, 2, 0],
         4: [2, 0, 0, 3]}
        """
        return {self.__need().index(i): i for i in self.__need()}

    def main(self, **kwargs) -> None:
        """
        Utilize various methods in this class to simulate the Banker's algorithm
        Return: None
        >>> BankersAlgorithm(test_claim_vector, test_allocated_res_table,
        ...    test_maximum_claim_table).main(describe=True)
                 Allocated Resource Table
        P1       2        0        1        1
        <BLANKLINE>
        P2       0        1        2        1
        <BLANKLINE>
        P3       4        0        0        3
        <BLANKLINE>
        P4       0        2        1        0
        <BLANKLINE>
        P5       1        0        3        0
        <BLANKLINE>
                 System Resource Table
        P1       3        2        1        4
        <BLANKLINE>
        P2       0        2        5        2
        <BLANKLINE>
        P3       5        1        0        5
        <BLANKLINE>
        P4       1        5        3        0
        <BLANKLINE>
        P5       3        0        3        3
        <BLANKLINE>
        Current Usage by Active Processes: 8 5 9 7
        Initial Available Resources:       1 2 2 2
        __________________________________________________
        <BLANKLINE>
        Process 3 is executing.
        Updated available resource stack for processes: 5 2 2 5
        The process is in a safe state.
        <BLANKLINE>
        Process 1 is executing.
        Updated available resource stack for processes: 7 2 3 6
        The process is in a safe state.
        <BLANKLINE>
        Process 2 is executing.
        Updated available resource stack for processes: 7 3 5 7
        The process is in a safe state.
        <BLANKLINE>
        Process 4 is executing.
        Updated available resource stack for processes: 7 5 6 7
        The process is in a safe state.
        <BLANKLINE>
        Process 5 is executing.
        Updated available resource stack for processes: 8 5 9 7
        The process is in a safe state.
        <BLANKLINE>
        """
        need_list = self.__need()
        alloc_resources_table = self.__allocated_resources_table
        available_resources = self.__available_resources()
        need_index_manager = self.__need_index_manager()
        for kw, val in kwargs.items():
            if kw and val is True:
                self.__pretty_data()
        print("_" * 50 + "\n")
        while need_list:
            safe = False
            for each_need in need_list:
                execution = True
                for index, need in enumerate(each_need):
                    if need > available_resources[index]:
                        execution = False
                        break
                if execution:
                    safe = True
                    # get the original index of the process from ind_ctrl db
                    for original_need_index, need_clone in need_index_manager.items():
                        if each_need == need_clone:
                            process_number = original_need_index
                    print(f"Process {process_number + 1} is executing.")
                    # remove the process run from stack
                    need_list.remove(each_need)
                    # update available/freed resources stack
                    available_resources = np.array(available_resources) + np.array(
                        alloc_resources_table[process_number]
                    )
                    print(
                        "Updated available resource stack for processes: "
                        + " ".join([str(x) for x in available_resources])
                    )
                    break
            if safe:
                print("The process is in a safe state.\n")
            else:
                print("System in unsafe state. Aborting...\n")
                break

    def __pretty_data(self):
        """
        Properly align display of the algorithm's solution
        """
        print(" " * 9 + "Allocated Resource Table")
        for item in self.__allocated_resources_table:
            print(
                f"P{self.__allocated_resources_table.index(item) + 1}"
                + " ".join(f"{it:>8}" for it in item)
                + "\n"
            )
        print(" " * 9 + "System Resource Table")
        for item in self.__maximum_claim_table:
            print(
                f"P{self.__maximum_claim_table.index(item) + 1}"
                + " ".join(f"{it:>8}" for it in item)
                + "\n"
            )
        print(
            "Current Usage by Active Processes: "
            + " ".join(str(x) for x in self.__claim_vector)
        )
        print(
            "Initial Available Resources:       "
            + " ".join(str(x) for x in self.__available_resources())
        )
        time.sleep(1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

p = BankersAlgorithm
print(p)