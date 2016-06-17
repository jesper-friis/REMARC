#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
import argparse

import softpy
from REMARC.vasp_data import VASP_DATA

#from REMARC.vasptb.outcar import OUTCAR
#from REMARC.vasptb.vaspcalculation import VaspCalculation

v = VASP_DATA('Fe2O3', 'Fe2O3/gasphase/')
g = v.gasphases[1]


with softpy.Storage(driver='hdf5', uri='xxx.h5') as s:
    s.save(g)


def main():
    parser = argparse.ArgumentParser(
        description='Walks through the "ts" subdirectory and checks that ' +
        'all needed directories exists.')
    parser.add_argument('rootdir', nargs='?', default='.',
                        help='Path to root directory.')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Enable verbose output.')
    args = parser.parse_args()

    #tscheck(args.rootdir, verbose=args.verbose)


if __name__ == '__main__':
    main()
