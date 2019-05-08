#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:31:37 2019

@author: matteomacchini
"""

# needed to use modules/scripts from parent folder
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import backtrader as bt

if __name__ == '__main__':
    cerebro = bt.Cerebro()

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())