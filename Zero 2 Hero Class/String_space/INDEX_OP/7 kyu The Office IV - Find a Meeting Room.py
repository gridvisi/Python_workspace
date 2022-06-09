'''
https://www.codewars.com/kata/57f604a21bd4fe771b00009c/solutions/python


'''

def meeting(rooms):
    return rooms.index('O') if 'O' in rooms else 'None available!'

def meeting(rooms):
    try:
        return rooms.index('O')
    except ValueError:
        return 'None available!'

