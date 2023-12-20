from sys import stdin
from queue import Queue

counthigh = countlow = 0
q = Queue()

class Device:
    def __init__(self, type, is_on=False, inputs=None, outputs=[]):
        self.type = type
        self.is_on = is_on
        self.inputs = inputs if inputs is not None else {}
        self.outputs = outputs
    
    def handleinput(self, origin, signal):
        global countlow, counthigh, q
        #print("handle:",self.type,origin, signal)
        self.inputs[origin] = signal
        countlow += (1-signal)
        counthigh += signal
        if self.type[0] == '&':
            if min(self.inputs.values()) > 0:
                for o in self.outputs:
                    q.put((self.type,o,0))
            else:
                for o in self.outputs:
                    q.put((self.type,o,1))
        if self.type[0] == '%':
            if signal == 0:
                if not self.is_on:
                    for o in self.outputs:
                        q.put((self.type,o,1))
                else:
                    for o in self.outputs:
                        q.put((self.type,o,0))
                self.is_on = not self.is_on
        if self.type[0] == 'b':
            for o in self.outputs:
                q.put((self.type,o,signal))

lines = [i.strip() for i in stdin.read().splitlines()]
graph = {}
for line in lines:
    name, outputs = line.split(' -> ')
    name2 = ''.join(name)
    if name[0] in ['&','%']:
        name2 = name[1:]
    graph[name2] = Device(name, False, {}, [x for x in outputs.split(', ')])
for line in lines:
    name, outputs = line.split(' -> ')
    for x in outputs.split(', '):
        x2 = ''.join(x)
        if x[0] in ['&','%']:
            x2 = x[1:]
        if x2 not in graph.keys():
            graph[x2] = Device("-"+x, False, {}, [])
        graph[x].inputs[name] = 0
graph['broadcaster'].inputs['b'] = 0
solution2 = 0
for _ in range(1000):
    q.put(('b','broadcaster',0))
    while q.qsize():
        nextp = q.get()
        graph[nextp[1]].handleinput(nextp[0],nextp[2])
print("Part 1:",countlow*counthigh)
# 238815727638557
