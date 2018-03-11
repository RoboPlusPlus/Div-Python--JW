"""Usually iterables have some sort of pattern, or patterns that will make it
easy for us to unpack them. However, sometimes data is a bit more messy, so
we need to make some code to make sense of it. Phone-numbers typically look a certain way so we can
make code to recognize them, and email-adresses have a @ in them, and a "." somewhere after(before any spaces) etc.
basically, we need to make sense of our data.

"""

#By analyzing our messy and mixed data, we might see that they follow one of two patterns

dataset = [
    ('pattern1', 15, 'horse'),
    ('pattern2', 'kamel', 'Likes hot weather', 22),
    ('pattern1', 9, 'duck')
]

#So we make functions to handle the different types of data we have

def do_pattern1(x, y):
    print('pattern 1', x, y)

def do_pattern2(x, y, z):
    print('pattern 2', x, y, z)

        
for tag, *args in dataset:
    if tag == 'pattern1':
        do_pattern1(*args)
    elif tag == 'pattern2':
        do_pattern2(*args)
        
    
