'''
https://blog.csdn.net/jianfpeng241241/article/details/51926420?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param

一 问题引入

在生物学中，经常需要比较两个不同生物的DNA，一个DNA串由由一串称为碱基的的分子组成，碱基有鸟嘌呤，腺嘌呤，胞嘧啶，胸腺嘧啶四中，我们用英文字母的首字母表示四种碱基，那么DNA就是在有限集{A,C,G,T}上的一个字符串。例如某种生物的DNA序列为：S1=ACCGGTCGAGTGCGCGGAAGCCGGCCGAA，S2=GTCGTTCGGAATGCCGTTGCTCTGTAAA，我们比较两个DNA串的原因就是希望确定他们的相似度，作为衡量两个物种相似度的标准。如果一个串是另外一个串的子串，那么它们就是相似的，但是这里彼此都不是彼此的子串。于是我们就有了新的衡量标准：寻找一个新串S3，使得S3中的元素都在S1，S2中出现过，且不要求连续，但是碱基在三个串中出现的顺序一定要相同。可以找到的S3的长度越长，表明两个物种越相似！
二 问题描述
给定两个字符串X[A,B,C,B,D,A,B]和Y[B,D,C,A,B,A],求X和Y的最长公共子序列LCS

三 思路

1 采用暴力破解法: 扫描X所有的可能子串, 取其中一个字符时候,存在 取或不取两种情况, 假设X字符串有M个字符,
则子串个数为2的M次方,

假设Y有N个字符,将M中取出的子串与Y中进行对比,最后的时间复杂度为 N*2^M，  简直是龟速啊。。。

2 简化方案

 2.1 从题目描述中 X = [A,B,C,B,D,A,B] , Y[B,D,C,A,B,A] ,目测最大公共子串为 BDAB , BCAB ,最长为4.

 2.2 假设从一开始就知道X,Y的最大长度为4 ，那么只要关心X为4的子串与Y进行对比,这样效率就提高了.

 2.3 进一步假设X字符串转为char数组后坐标为{0,1,2,3,4.....M} , 同理Y为{0,1,2,3...N}

   假设  i  <= M , j <= N  , c[i][j] =LCS( X,Y)  . // i ,j 为一个int整数  , c[i][j]为 X的char数组{0,1,2,3....i} 和Y的char数组{0,1,2,3...j} 最大公共子串的长度

 // LCS 为 longestcommon subsequence (  最长公共子串 ) 的缩写 .

   那么对于X{0,1,2,3.....M} , Y{0,1,2,3....N}的最大公共子串长度为

   c[i][j] + LCS(X1,Y1)

 其中 X1 的坐标{ i+1,i+2,.....M } ,Y1坐标为{j+1,j+2....N}.

  求最大公共子串长度总结 :  一部分长度( 假设已知)  + 另外一部长度( 需要求的 )

四 公式

最大公共子串公式1

  if (X[i] == Y[j] )   c[i][j] = c[i-1][j-1] + 1

证明 :假设X , Y (见图1) , 在X {0，1，2，...i} , Y {0,1,2,3...j} 中最长公共子串长度为 k ,
那么 在X{0,1,2,3...,i-1} ,Y{0,1,2,3,...,j-1}(见图2)中最长公共子串长度为k-1

问题引入中DNA序列为：
S1= ACCGGTCGAGTGCGCGGAAGCCGGCCGAA ，
S2= GTCGTTCGGAATGCCGTTGCTCTGTAAA,
由该程序求得,最大公共子串为  = GTCGTCGGAAGCCGGCCGAA
'''