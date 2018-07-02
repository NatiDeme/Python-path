import threading

no_of_tabs = 0
identation_expression = r"^([ ]+)?"
conditional_expression = r"^(if|while|elif)[ ]?\(?(True|False|.+)?\)?:"
else_expression = r"^(else)"
elif_expression = r"^(elif)"

line_no = 0
tabcheck = 0
stopMainExec = False

class MyThread (threading.Thread):

    def __init__(self, fileTrackerNo, executedPaths):
        threading.Thread.__init__(self)
        self.fileTrakcerNo
        self.executedPaths = executedPaths

    def run(self):
        file = open("trial.py")
        readLines = file.readlines()
        line_no = 0

        for eachLine in readLines:
            line_no += 1
            if(fileLineNo == self.fileTrackerNo):
                ##Repeat Main code
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
                ##matched_elif = re.match(elif_expression, eachline)
                if(matched_else | matched_elif):
                    tabcheck = tabs
                    stopMainExec = True
                    MyThread(line_no, executed_path)

                elif(stopMainExec == True):
                    continue
                else:
                    self.executedPaths.append(eachline)
            else:
                continue

        print(self.executedPaths)
