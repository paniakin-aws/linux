#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0

import subprocess
import time
import tempfile

import _damon_sysfs

TEST_PROGRAM_WSS = 100 * 1024 * 1024

def make_test_file():


def main():
    print('HIIIII!')
    proc = subprocess.Popen(['./wo_stress.py', '%d' % sz_region, '2'])

if __name__ == '__main__':
    main()
