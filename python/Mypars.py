import re

no_of_tabs = 0
identation_expression = r"^([ ]+)?"
conditional_expression = r"^(if|while|elif)[ ]?\(?(True|False|.+)?\)?:"
else_expression = r"^(else)"
elif_expression = r"^(elif)"

file = open("trial.py")
readLines = file.readlines()
executed_paths = []
line_no = 0
tabcheck = 0
stopMainExec = False

for eachline in readLines:
    line_no += 1
    eachline = eachline.strip()
    matched = re.match(identation_expression, eachline).groups()
    
    if matched[0] is not None:
        tabs = len(matched[0])
    else:
        tabs = 0

    if(tab < tabcheck):
        stopMainExec = False
        
    ##matched_conditional = re.match(conditional_expression, eachline).groups()
    matched_else = re.match(else_expression, eachline)
    matched_elif = re.match(elif_expression, eachline)
    if(matched_else | matched_elif):
        tabcheck = tabs
        MyThread(line_no, executed_paths)
        stopMainExec = True

    elif(stopMainExec == True):
        continue
    else:
        executed_paths.append(eachline)

print(executed_paths)
