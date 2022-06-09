#https://math.stackexchange.com/questions/2217248/which-answer-in-this-list-is-the-correct-answer-to-this-question

'''
我从我的数学教授那里收到了这道题，作为闲暇时的逻辑测验，虽然我认为我答对了，但他否定了。谁能解释一下正确答案背后的推理？

这个列表中的哪个答案是这个问题的正确答案？

表述1：下面所有的。
表述2：以下都不是。
表述3：上述所有的。
表述4：上面的一个。
表述5：以上都不是。
我想。

2表述和3表述相互矛盾，所以1表述不可能是真的。
2表述否认3表述，但3表述肯定了2表述，所以3表述不可能是真的。
2表述否认4表述，但由于1表述和3表述被证明是假的，4表述不可能是真的。
6表述否认5表述，但反之亦然，所以5表述不可能是真的。
在这一点上，只剩下2表述和6表述可以考虑。我认为选择2表述不会否定1表述
（而且不可能是以下所有的，也不可能是以下所有的），因此我认为答案是6表述。

Which answer in this list is the correct answer to this question?

(a) All of the below.
(b) None of the below.
(c) All of the above.
(d) One of the above.
(e) None of the above.
(f) None of the above.
*/

#include <stdio.h>
#define iff(x, y) ((x)==(y))

int main() {
  printf("a b c d e f\n");
  for (int a = 0; a <= 1; a++)
  for (int b = 0; b <= 1; b++)
  for (int c = 0; c <= 1; c++)
  for (int d = 0; d <= 1; d++)
  for (int e = 0; e <= 1; e++)
  for (int f = 0; f <= 1; f++) {
    int Ra = iff(a, b && c && d && e && f);
    int Rb = iff(b, !c && !d && !e && !f);
    int Rc = iff(c, a && b);
    int Rd = iff(d, (a && !b && !c) || (!a && b && !c) || (!a && !b && c));
    int Re = iff(e, !a && !b && !c && !d);
    int Rf = iff(f, !a && !b && !c && !d && !e);

    int R = Ra && Rb && Rc && Rd && Re && Rf;
    if (R) printf("%d %d %d %d %d %d\n", a, b, c, d, e, f);
  }
  return 0;
}
```
Python code_solution

表述1：下面所有的对的。
表述2：以下都不是对的。
表述3：上述所有的对的。
表述4：上面的一个对的。
表述5：以上都不是对的。

如果1对，那么2错，3错，4对，5错

'''




