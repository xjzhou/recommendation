# -*- coding: utf-8 -*-
import sys
from preprocess import Channel
from workflow.cf_workflow import run as user_cf
from workflow.lfm_workflow import run as lfm
from workflow.prank_workflow import run as prank


def manage():
    arg = sys.argv[1]
    if arg == 'preprocess':
        Channel().process()
    elif arg == 'cf':
        user_cf()
    elif arg == 'lfm':
        #lfm()
        print('lfm耗时过长，暂停使用')
    elif arg == 'prank':
        prank()
    else:
        print('Args must in ["preprocess", "cf", "lfm"，"prank"].')
    sys.exit()


if __name__ == '__main__':
    manage()
