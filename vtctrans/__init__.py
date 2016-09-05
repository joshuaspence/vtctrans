import sys
from vtctrans.varnishtest import VarnishTest

def main():
    vtc  = VarnishTest()
    argv = sys.argv
    argc = len(argv)
    opt  = ''
    if(argv == 1):
        exit

    r= vtc.execVarnishTest(argv[1:])
    if(r[0]['result'] != 'passed'):
        exit(1)
