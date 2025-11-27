#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0

import sys
import time
import mmap
import tempfile
import os


BLOCK_SIZE = 512


def usage():
    print('Usage: %s file-size test-time')
    sys.exit(1)


def populate_test_file(f, test_sz):
    for i in range(test_sz // BLOCK_SIZE):
        f.write('1' * BLOCK_SIZE)

    f.seek(0)


def validate_args():
    if len(sys.argv) < 3:
        usage()
    file_size = int(sys.argv[1])
    if file_size % BLOCK_SIZE:
        usage()


def test_loop(f, file_size, test_time):
    start_time = time.time()

    while int(time.time() - start_time) < test_time:
        with mmap.mmap(f.fileno(), 0) as m:
            for i in range(file_size):
                m[i] = 0x41


def main():
    print(os.getpid())
    validate_args()
    file_size = int(sys.argv[1])
    test_time = int(sys.argv[2])
    with tempfile.TemporaryFile(mode='w+') as f:
        populate_test_file(f, file_size)
        test_loop(f, file_size, test_time)


if __name__ == '__main__':
    main()
