from textwrap import dedent

def greet_madlib():
    print(dedent("""
    **   Greetings from MadLib!   **
    **   To play, enter words     **
    **   Have fun and go crazy    **
    """))



def read():
    with open('assets/default.txt') as stuff:
        stuff = stuff.read()
    listify = list()
    endpoint = 0

    for r in range(stuff.count('{')):
        begin = stuff.find('{', endpoint)+1
        endpoint = stuff.find('}', begin)
        make_word = stuff[begin : endpoint]
        listify.append(make_word)
    return listify
    
def question(listify):
    word_list = list()
    for l in listify:
        prompt = input(f"Enter a {l}: ")
        word_list.append(prompt)

    return word_list

def merge(word_list):
    with open('assets/test.txt') as content:
        body = content.read()

    strings = body.count('{')
    
    for r in range(strings):
        begin = body.find('{', 0)
        endpoint = body.find('}', 0)+1
        body = body[:begin] + word_list[r] + body[endpoint:]
        
    return body

def save(info):
    with open('assets/new.txt', 'a') as t:
        t.write(info)

greet_madlib()
key = read()
word_list = question(key)
new_template = merge(word_list)
print(new_template)
save(new_template)