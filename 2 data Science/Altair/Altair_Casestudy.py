
## Altair 上手基础
'''
Altair是一个用于Python的统计数据可视化库。它提供了一个简单易懂的语法来创建静态和互动的可视化。

我最喜欢的是Altair的数据转换和过滤功能。它提供了灵活多变的方法来转换和过滤数据，同时创建一个数据可视化。

在这个意义上，Altair也可以被视为一个数据分析工具。我们将通过3个例子来展示Altair如何加速探索性数据分析过程。

我们将使用Kaggle网站上的墨尔本住房数据集的一个小样本作为例子。我们首先导入库并读取数据集。
[Melbourne Housing Snapshot | Kaggle]
(https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot/code)

```
'''
import numpy as np
import pandas as pd
import altair as alt

cols = ['Type', 'Price', 'Distance', 'Date', 'Landsize', ' Regionname']
melb = pd.read_csv(
   "D:/data_science/dataset/melb_data.csv", usecols = cols, parse_dates = ['Date']
).sample(n=1000).reset_index(drop=True)
melb.head()

'''

例子1
我们将创建一个条形图，显示每个地区的平均房价。一种选择是通过使用Pandas的函数来计算平均值，然后绘制结果。
然而，我们可以用Altair一次完成。

'''

alt.Chart(melb).mark_bar().encode(
   x = 'Regionname', y = 'avg_price:Q'
).transform_aggregate(
   avg_price = 'mean(Price)', groupby = ['Regionname']
).properties(
   height = 300, width = 500
)


'''

语法以一个顶级的Chart对象开始，后面是绘图类型。encode函数用于指定在传递给Chart对象的数据框架中绘制什么。
你可能已经注意到了，y编码不是数据框架中的一个列。它是聚合列，在下一步使用transform_aggregate函数进行计算。y 编码中的 "Q "字母代表数量。
属性函数用于调整可视化的属性。下面是上面的代码所产生的图。

![image.png](https://upload-images.jianshu.io/upload_images/184712-158417901b2d25d6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
(图片由作者提供)

例2
距离栏表示房子到中心商业区的距离。假设我们想为距离超过3英里的房子创建前面例子中的情节。
我们可以通过在代码中实现transform_filter函数来轻松完成这一任务。
```
alt.Chart(
  melb, height=300, width=500
).mark_bar().encode(
  x = 'Regionname', y = 'avg_price:Q'
).transform_filter(
  alt.FieldGTPredicate(field='Distance', gt=3)
).transform_aggregate(
  avg_price = 'mean(Price)',groupby = ['Regionname']
)

```

FieldGTPredicate处理 "大于 "条件。Altair还提供了其他条件的谓词，如 "等于"、"小于"、"范围 "等等。
在前面的例子中，我们使用属性函数来调整大小。在这个例子中，同样的操作是在图表对象内部完成的。
下面是过滤后的数值的柱状图。
![image.png](https://upload-images.jianshu.io/upload_images/184712-0784305493cbeb20.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

(图片由作者提供)

例三
这个例子涉及到一个查找操作，类似于Pandas的合并函数。
考虑到我们有另一个数据框架，包含了这些房子的主人的一些信息。
```
melb['OwnerId'] = np.arange(1,1001)
df = pd.DataFrame({
  'OwnerId': melb['OwnerId'],
  'Age': np.random.randint(20, 40, size=1000),
  'Salary': np.random.randint(5000, 10000, size=1000)
})
df.head()
```
![image.png](https://upload-images.jianshu.io/upload_images/184712-ac3b392cc735095a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

我们在原来的数据框架中增加了一个id列，并创建了一个新的数据框架，其中包含客户的id、年龄和工资信息。

我们想绘制出每种房屋类型的业主的平均工资。我们可以用Pandas函数来合并数据框，按房屋类型对数据点（即行）进行分组，并计算出平均值。
另一个选择是使用Altair的查找转换，如下所示。

```
alt.Chart(
  df, height=300, width=500
).mark_bar().encode(
  x = 'mean(Salary):Q', y = 'Type:O'
).transform_lookup(
  lookup='OwnerId',
  from_=alt.LookupData(data=melb, key='OwnerId', fields=['Type'])
)
```
lookup参数指的是用于合并的列。下面是生成的图。
![image.png](https://upload-images.jianshu.io/upload_images/184712-c126a4199185b0e8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

(图片由作者提供)
总结
我们已经做了3个例子，展示了Altair的转换和过滤能力。关于这些操作，Altair也是一个数据分析和操作的工具。
当然，Pandas在此类操作上要强大得多。然而，在创建可视化的同时，能够进行基本的数据处理操作，为Altair增加了重要价值。
我们只做了柱状图的例子，但转换功能可以适当地扩展到任何其他图。


## Altair: 用于Python的统计可视化库
实用的入门指南

Soner Yıldırım
3 天前-5 分钟阅读

https://unsplash.com/
照片：Isaac Smith on Unsplash
Altair是一个Python的统计可视化库。它的语法简洁易懂，正如我们将在例子中看到的那样。用Altair创建交互式可视化也非常简单。

Altair在数据转换方面非常灵活。在创建可视化时，我们可以应用许多不同类型的转换。这使得该库在探索性数据分析方面更加有效。

我认为Altair的特别之处在于比其他一些流行的Python数据可视化库（如Matplotlib和Seaborn）更重的统计方面。

在这篇文章中，我们将创建一些基本的图来熟悉Altair的语法和结构。我们还将看到在创建图的过程中是如何实现数据转换的。

我们首先要导入Altair。如果你使用的是Google Colab，它已经被安装，可以直接导入。如果没有，你可以使用pip轻松地安装它。

我们将使用一个保险数据集，你可以从Kaggle获得。我们将把数据集读入一个Pandas数据框。
下载地址 [Medical Cost Personal Datasets | Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance)

```
import Altair as ALTAL
import numpy as np
import pandas as pdinsurance = pd.read_csv("/content/insurance.csv")
insurance.head()

```

(图片由作者提供)
这个数据集包含了一些关于某保险公司的客户和保险收费金额的衡量标准（即特征）。
散点图
散点图主要用于可视化两个数字变量之间的关系。
```
(alt.
  Chart(insurance).
  mark_circle(size=40).
  encode(x='charge', y='bmi').
  properties(height=400, width=500))
```

我把每个步骤放在一个单独的行中，以强调类似链式的操作。我们首先将数据传递给一个顶层的图表对象。数据可以是Pandas数据框的形式，也可以是指向json或csv文件的URL字符串。

第二行描述了可视化的类型（例如：mark_circle，mark_line，等等）。编码函数指定在给定的数据框架中绘制什么。因此，我们在编码函数中写的任何东西都必须与数据框架相连。最后，我们使用properties函数来指定绘图的某些属性。
下面是用上述代码创建的图。

(图片由作者提供)
我们可以使绘图的内容更加丰富。例如，我们可以在编码函数中使用颜色参数，根据一个分类变量来分离数据点。它类似于Seaborn的色调参数。
我们还可以通过在结尾处添加交互式函数来使图表具有交互性。
```
(alt.
  Chart(insurance).
  mark_circle(size=50).
  encode(x='charges', y='bmi', color='smoker').
  properties(height=400, width=500).
  interactive())
```


(作者提供的GIF)
可以为这个图添加更多的功能。我们可以使用工具提示参数，当我们在点上悬停时显示额外的变量。这就像Seaborn的hover参数一样。
```
(alt.
  Chart(insurance).
  mark_circle(size=50).
  encode(x='charges', y='bmi', color='smoker', tooltip=
  ['age','sex']).
  properties(height=400, width=500).
  interactive())

```

(作者提供的GIF)
条形图
在创建可视化的过程中，Altair使得实现数据转换变得简单而高效。例如，我们可以创建一个条形图，显示区域列中每个类别的平均收费。
```
(alt.
  Chart(insurance).
  mark_bar().
  encode(x='region', y='mean(charges):Q').
  properties(height=300, width=400))
```


(图片由作者提供)
我们将转换指定为一个字符串（'mean(charges):Q'），这相当于以下语法:
```
y=alt.X(field='charge', aggregate='mean', type='quantitative')
insurance[['region','charges']].groupby('region').mean()

```

让我们用Pandas的groupby函数来计算同样的平均数以确认结果。
insurance[['地区','收费']].groupby('地区').mean()

(图片由作者提供)
结果与预期相同。我们在可视化中实现了这个计算。

直方图
直方图主要用于可视化连续变量的分布。它将连续变量的数值范围划分为离散的仓，并显示每个仓中存在多少个数值。
下面的代码将创建一个bmi变量的直方图。
```
(alt.
  Chart(insurance).
  mark_bar()。
  encode(alt.X('bmi:Q', bin=True), y='count()')。
  properties(height=300, width=500))
```

(图片由作者提供)

我们使用make_bar函数与数据转换步骤来创建一个直方图。在encode函数中，我们将bmi变量的值范围划分为离散的bin，并计算每个bin中的数据点数量。

图的网格
在同一个可视化中创建多个图是非常简单的。
我们首先需要将这些图分配给变量，然后用这些变量来组合图或创建一个图的网格。
```
p1 = (alt.
        Chart(insurance).
        mark_bar().
        encode(x='region', y='mean(charges):Q').
        properties(height=200, width=300))p2 = (alt.
        Chart(insurance).
        mark_bar().
        encode(alt.X('bmi:Q', bin=True), y='count()').
        properties(height=200, width=300))
```
一旦我们有了这些变量，我们就可以使用逻辑运算符来组合它们。
p1 | p2

(图片由作者提供)
p1 & p2

(图片由作者提供)
正如你所看到的，这就像数学运算一样，可以将图画组合起来。p1 + p2 语法将合并同一图中的图，但它在我们的例子中并不合适。如果我们有一个直线图和一个柱状图，这将是一个可以考虑的选项。
我们可以通过这种方式组合几个图来创建一个网格图。例如，(p1 & p2) | (p3 & p4) 创建一个由4个图组成的网格（2行和2列）。

总结
这篇文章可以看作是对Altair的一个介绍。这个库提供的功能还有很多。
我最喜欢Altair的地方是数据转换的便捷性和简单性。它也促进了数据分析过程。
在Altair系列的第二部分，我重点介绍了过滤和数据转换在可视化中的应用。
我将会写更多关于Altair的教程。敬请关注这个库的更多高级功能。
谢谢您的阅读。如果您有任何反馈，请告诉我

'''