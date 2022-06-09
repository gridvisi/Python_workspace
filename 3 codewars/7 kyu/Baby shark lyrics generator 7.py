def d():
    return ", doo doo doo doo doo doo"
def baby_shark_lyrics():
    a=["Baby ","Mommy ","Daddy ","Grandma ","Grandpa ","shark","Let's go hunt"]
    b=""
    for i in range(5):
        b+=a[i]+a[5]+d()+'\n'+a[i]+a[5]+d()+'\n'+a[i]+a[5]+d()+'\n'+a[i]+a[5]+'!'
    for i in range(3):
        b+=a[6]+d()+'\n'
    b+=a[6]+'!'+'\n'+"Run away,…"
    return b

print(baby_shark_lyrics())