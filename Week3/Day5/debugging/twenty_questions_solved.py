import json

f = open('questions.json')   # fix the path, FileNotFounderror
content = f.read()   # add brackets here, TypeError
node = json.loads(content)  # loads instead of reads, Attribute Error

def is_answer(node):
    return len(node) == 1

finished = False

while not finished:     # add colon, SyntaxError
    print(node['text'])    # add parenthesis, SyntaxError

    if is_answer(node):    # indent the whole block ,SemanticError  
        finished = True    # check function name, NameError
    else:
        answer = input()    # taking out one =  , NameError
        if answer.lower() in ['yes', 'y']:   # lower instead of upper, SemanticError
            node = node['yes']   # swap yes and no, SemanticError
        else:
            node = node['no']
