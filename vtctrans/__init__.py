import sys
from vtctrans.varnishtest import VarnishTest

def main():
    vtc  = VarnishTest()
    argv = sys.argv
    argc = len(argv)
    opt  = ''
    if(argv == 1):
        exit

    opt = ' '.join(argv[1:])
    r= vtc.execVarnishTest(opt)
    if(r[0]['result'] != 'passed'):
        exit(1)
