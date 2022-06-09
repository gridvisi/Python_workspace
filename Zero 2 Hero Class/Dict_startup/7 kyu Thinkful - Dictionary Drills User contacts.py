'''
https://www.codewars.com/kata/586f61bdfd53c6cce50004ee/train/python
'''
data = [["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]
def user_contacts(data):
    return dict(i+[None] if len(i) == 1 else i for i in data)

print(user_contacts(data))

#1st
def user_contacts(data):
    return {contact[0]: contact[1] if len(contact) > 1 else None
            for contact in data}

from itertools import zip_longest

def user_contacts(data):
    return dict(zip(*zip_longest(*data)))