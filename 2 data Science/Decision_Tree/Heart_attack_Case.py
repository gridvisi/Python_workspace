

left_leaf,right_leaf = {'Yes':3,'No':1},{'Yes':2,'No':1}
root = {'left':left_leaf,'right':right_leaf}

def Gini_impurity(root):
    ylft,nlft,yrgt,nrgt = 0,0,0,0
    lft,rgt = 0,0
    for key,leaf in root.items():
        if key == 'left':
            for k, v in leaf.items():
                ylft += leaf['Yes']
                nlft += leaf['No']
                lft += v
        elif key == 'right':
            for k, v in leaf.items():
                yrgt += leaf['Yes']
                nrgt += leaf['No']
                rgt += v

    gini_left = 1 - (ylft/(ylft+nlft))**2 - (nlft/(ylft+nlft))**2
    gini_right = 1 - (yrgt / (yrgt + nrgt)) ** 2 - (nrgt / (yrgt + nrgt)) ** 2
    l,r = round(gini_left,3),round(gini_right,3)
    gini_root = round(l * lft/(lft+rgt) + r * rgt/(lft+rgt),3)
    return l,r,gini_root

print(Gini_impurity(root))

# 加权平均 gini_left, gini_right
roots = {}
roots['left'] = Gini_impurity(root)[0]
roots['right'] = Gini_impurity(root)[0]

#age < 39.5
left_leaf,right_leaf = {'Yes':0,'No':1},{'Yes':3,'No':3}
root = {'left':left_leaf,'right':right_leaf}
print('age < 39.5 ',Gini_impurity(root))