__author__ = 'Administrator'
'''
int countConnections(person p, int depth) {
    if(depth == 2)
        return 1;
    int count = 0 + depth;
    //to make sure neighbours of the root count themselves
    for each neighbour n of p do {
        count += countConnections(n, depth + 1);
    }
    return count;
}
'''
def countconnect(person,depth):
    if depth == 2:
        return 1
    count = depth
    for (node in )
