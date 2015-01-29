# AsyncPy shell
# tom coladonato

# with boilerplate from
# http://stackoverflow.com/questions/9105990/constantly-looking-for-user-input-in-python


import threading
import Queue
import sys
import time

def console(q, stdout_lock):
    while 1:
        raw_input()
        with stdout_lock:
            cmd = raw_input('> ')
        q.put(cmd)
        if cmd == 'quit' or cmd == 'exit':
            break

class Agent():
    run = lambda: None
    def __init__(self, func = None):
        if func:
            self.run = func
        


if __name__ == '__main__':
    console_buffer = Queue.Queue()
    stdout_lock = threading.Lock()

    s = \
    ''' 
    AsyncPy Shell
    =====
    Press Enter to aquire lock
    Input single line python expression or statement to be evaluated or executed

    Input exit to exit

    '''
    s = s.replace('    ', '')
    with stdout_lock:
        print s


    dj = threading.Thread(target=console, args = (console_buffer, stdout_lock))
    time.sleep(0.1)
    dj.start()

    i = 0

    agents = {} #dict of agents to be evaluated once per tick


    while True:
        # if there is a command, handle it
        if not console_buffer.empty():
            cmd = console_buffer.get()
            if cmd == 'quit' or cmd == 'exit':
                break
        
            #determine if statement or expression
            isstatement = False
            try:
                code = compile(cmd, '<stdin>', 'eval')
            except SyntaxError:
                isstatement = True
                code = compile(cmd, '<stdin>', 'exec')
                
            result = None
            with stdout_lock:
                if isstatement:
                    try:
                        exec(cmd) # TODO: sandbox
                    except:
                        e = sys.exc_info()[0]
                        print("ERROR: %s\n"%e)
                else:
                    try:
                        result = eval(cmd) # TODO: sandbox
                    except:
                        e = sys.exc_info()[0]
                        print("ERROR: %s\n"%e)
                if result is not None:
                    print(" ".join(["< ",str(result)]))
                    
        # evaluate all agents and print status display if applicable
        agent_out = ""
        for agent in agents.items():
            try:
                agent_out += '\'' + agent[0] + '\' >: ' + str(agent[1].run()) + '\n'
            except:
                e = sys.exc_info()[0]
                agent_out += str("ERROR: %s\n"%e)
        if agent_out:
            with stdout_lock:
                print "Agent output\n====="
                print agent_out,
                print "=====\n"
        i += 1
        time.sleep(0.5)