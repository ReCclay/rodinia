#!/usr/bin/python

import sys

inbytes = [
0x3d, 0x72, 0x63, 0x7b, 0x30, 0x25, 0x24, 0x2c,
0x4f, 0x78, 0x5e, 0x74, 0x33, 0x70, 0x3c, 0x52,
0x27, 0x2b, 0x6c, 0x34, 0x22, 0x32, 0x45, 0x57,
0x46, 0x2f, 0x7c, 0x6f, 0x47, 0x4a, 0x28, 0x79,
0x61, 0x2d, 0x65, 0x26, 0x6b, 0x66, 0x75, 0x73,
0x2e, 0x09, 0x50, 0x20, 0x42, 0x7e, 0x77, 0x60,
0x4b, 0x3e, 0x36, 0x5d, 0x3a, 0x23, 0x51, 0x37,
0x41, 0x43, 0x31, 0x39, 0x56, 0x67, 0x68, 0x48,
0x5b, 0x38, 0x2a, 0x6e, 0x40, 0x64, 0x4c, 0x35,
0x69, 0x76, 0x7a, 0x5f, 0x44, 0x7d, 0x29, 0x3f,
0x58, 0x55, 0x6a, 0x6d, 0x62, 0x53, 0x59, 0x5a,
0x3b, 0x54, 0x5c, 0x71, 0x21, 0x49, 0x4e, 0x4d,
];

outbytes = [
0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37,
0x38, 0x39, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66,
0x67, 0x68, 0x69, 0x6a, 0x6b, 0x6c, 0x6d, 0x6e,
0x6f, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76,
0x77, 0x78, 0x79, 0x7a, 0x41, 0x42, 0x43, 0x44,
0x45, 0x46, 0x47, 0x48, 0x49, 0x4a, 0x4b, 0x4c,
0x4d, 0x4e, 0x4f, 0x50, 0x51, 0x52, 0x53, 0x54,
0x55, 0x56, 0x57, 0x58, 0x59, 0x5a, 0x21, 0x22,
0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a,
0x2b, 0x2c, 0x2d, 0x2e, 0x2f, 0x3a, 0x3b, 0x3c,
0x3d, 0x3e, 0x3f, 0x40, 0x5b, 0x5c, 0x5d, 0x5e,
0x5f, 0x60, 0x7b, 0x7c, 0x7d, 0x7e, 0x20, 0x09,
];

with open(sys.argv[1], "r") as input_file:
    data = input_file.read()
    result = []
    for char in data:
        code = ord(char)
        if code in inbytes:
            idx = inbytes.index(ord(char))
            code = outbytes[idx]
        result.append(chr(code))
    print "".join(result)