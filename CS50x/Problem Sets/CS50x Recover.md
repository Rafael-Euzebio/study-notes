# Recover
[[CS50x Problem Sets]]

## JPEGS
- Every JPEG file has a signature on the first 3 bytes

        0xff 0xd8 0xff
- The fourth byte `0xe0`, `0xe1`, `0xe2`, `0xe3`, `0xe4`, `0xe5`, `0xe6`, `0xe7`, `0xe8`, `0xe9`, `0xea`, `0xeb`, `0xec`, `0xed`, `0xee`, or `0xef`
    - That is the same as saying the first four bits (aka the first digit from left to right) of the fourth byte is `1110`

## Storage
- Digital cameras often use a FAT file system that stores every content in blocks of 512 bytes
    - That means a 1 MB photo takes 2048 blocks of 512 bytes
        - $1$ MB  = $1,048,576$ bytes $/$ $512 = 2048$

## Recovering
- It is possible to search for a JPEG signature in a file and, when it is found, write it to another file.  
    - The signature must be stored with a `uint8_t` data type, so it can be checked byte by byte.  
        - After found the contents can be written in chunks of 512 bytes for efficiency.  
