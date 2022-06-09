'''
https://www.codewars.com/kata/5a68ffe3e626c5e85700002d/train/python

There was an old lady who swallowed a fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a spider;
That wriggled and jiggled and tickled inside her!
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a bird;
How absurd to swallow a bird!
She swallowed the bird to catch the spider;
That wriggled and jiggled and tickled inside her!
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a cat;
Fancy that she swallowed a cat!
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider;
That wriggled and jiggled and tickled inside her!
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady that swallowed a dog;
What a hog, to swallow a dog!
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider;
That wriggled and jiggled and tickled inside her!
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - Perhaps she'll die!
`
There was an old lady who swallowed a goat;
She just opened her throat and swallowed a goat!
She swallowed the goat to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider;
That wriggled and jiggled and tickled inside her!
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a cow;
I don't know how she swallowed a cow!
She swallowed the cow to catch the goat,
She swallowed the goat to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider;
That wriggled and jiggled and tickled inside her!
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a horse;
...She's dead, of course!


Random Tests
100 random test cases
Input: ['cow', 'spider', 'goat', 'cat', 'fly', 'cat', 'spider', 'fly', 'horse']
~~~~~~~~~~~~
: ['horse'] should equal ['spider', 'cat', 'cat', 'spider', 'horse']
Input: ['cat', 'bird', 'spider']
~~~~~~~~~~~~
: ['cat'] should equal ['cat', 'spider']
Input: ['spider', 'goat', 'cow', 'dog', 'cow', 'spider', 'bird', 'goat', 'spider', 'bird', 'horse', 'fly', 'spider', 'cat', 'cat', 'spider', 'cow', 'bird', 'dog', 'spider', 'horse']
~~~~~~~~~~~~
: ['horse'] should equal ['bird', 'bird', 'horse']
Input: ['bird', 'horse', 'fly', 'fly']
~~~~~~~~~~~~
: ['horse'] should equal ['bird', 'horse']
Input: ['cat', 'cow', 'goat', 'cow', 'dog', 'dog', 'cow', 'goat', 'fly', 'cat', 'fly', 'spider', 'cow', 'fly', 'horse', 'horse', 'cow', 'horse', 'cow']
~~~~~~~~~~~~
: ['horse'] should equal ['cat', 'spider', 'horse']
Input: ['cat', 'cow', 'cat']
~~~~~~~~~~~~
: ['cow'] should equal ['cat', 'cow', 'cat']
Input: ['cat', 'cow', 'dog', 'cow', 'goat', 'goat', 'cat']
~~~~~~~~~~~~
: ['cow'] should equal ['cow', 'cow', 'cat']
Input: ['dog', 'dog', 'cat', 'cat', 'cow']
~~~~~~~~~~~~
: ['cow'] should equal ['dog', 'dog', 'cow']
'''

#1st best
predators = {
    "fly": "spider",
    "spider": "bird",
    "bird": "cat",
    "cat": "dog",
    "dog": "goat",
    "goat": "cow",
    "cow": "horse"
}

def old_lady_swallows(animals: list) -> list:
    alive = []
    for animal in animals:
        alive.append(animal)
        alive_set = set(alive)
        alive = [prey for prey in alive if predators.get(prey) not in alive_set]
        if animal == "horse": break
    return alive



from collections import Counter
def old_lady_swallows(animals: list) -> list:
    seq = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse'][::-1]
    eaten = dict(zip(seq[:-1],seq[1:]))
    CuntAnimal = Counter(animals)
    print(eaten)
    print(CuntAnimal)
    for k,v in CuntAnimal.items():
        if k != 'fly' and eaten[k] in CuntAnimal.keys():
            print(eaten.get(k))
            CuntAnimal[eaten[k]] -= 1
    alive = [k for k,v in CuntAnimal.items() if k in seq and v > 1]
    return alive
animals = ["bird", "fly", "spider", "fly"]
animals = ["cow", "horse", "horse"]
print('dict_solve:',old_lady_swallows(animals))

#1st try not perfect
def old_lady_swallows(animals: list) -> list:
    eaten = []
    seq = ['fly','spider','bird','cat','dog','goat','cow','horse']

    for i in animals:
        try:
            x = seq[seq.index(i)-1]
        except:
            x = None
        animals.remove(seq[seq.index(i)-1])
    return animals


#try not perfect 2nd
def old_lady_swallows(animals: list) -> list:
    eaten = []
    seq = ['fly','spider','bird','cat','dog','goat','cow','horse']

    for i in animals:
        try:
            x = seq[seq.index(i) - 1]
        except:
            x = None
        if x in animals:
            eaten.append(seq[seq.index(i)-1])
    return [i for i in animals if i not in eaten]

animals = ["bird", "fly", "spider", "fly"]
print(old_lady_swallows(animals))




animals = ["bird", "fly", "spider", "fly"]
print(old_lady_swallows(animals))

def old_lady_swallows(animals: list) -> list:
    seq = ['fly','spider','bird','cat','dog','goat','cow','horse']
    return [seq[max([seq.index(i) for i in animals])]]
