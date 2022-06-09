'''
Python | Print the initials of a name with last name in full
Given a name, print the initials of a name(uppercase) with last name(with first alphabet in uppercase) written in full separated by dots.

Examples:

Input : geeks for geeks
Output : G.F.Geeks

Input : mohandas karamchand gandhi
Output : M.K.Gandhi
'''


# python program to print initials of a name
def name(s):
    # split the string into a list
    l = s.split()
    new = ""

    # traverse in the list
    for i in range(len(l) - 1):
        s = l[i]

        # adds the capital first character
        new += (s[0].upper() + '.')

        # l[-1] gives last item of list l. We
    # use title to print first character in
    # capital.
    new += l[-1].title()

    return new


# Driver code
s = "mohandas karamchand gandhi"
print(name(s))