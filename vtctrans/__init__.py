import sys
from vtctrans.varnishtest import VarnishTest

def main():
    vtc  = VarnishTest()
    argv = sys.argv
    argc = len(argv)
    opt  = ''
    if(argv == 1):
        exit

    results = vtc.execVarnishTest(argv[1:])

    for result in results:
        if (result['result'] != 'passed'):
            exit(1)

    exit(0)
