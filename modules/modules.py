#!/usr/bin/env python3
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
print(log)
def f1():
    print("F1 Execution")

def f2():
    print("F2 Execution")

def f3():
    print("F3 Execution")
if __name__ == '__main__':
    f1()
    f2()
    f3()