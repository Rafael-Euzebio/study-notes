# Reverse

## WAV
- A WAV file is broken into three chunks of data
    - First and second chunk are considered the *header* of the WAV file, it contains 44 bytes
        - The first chunk as information about the file
            - The bytes 0 ~ 7 store the Chunk 1 ID and Size information
            - The bytes 8 ~ 11 in this chunk spell out 'W' 'A' 'V' 'E', to indicate this is a WAV file
        - The second chunk has information about the audio
            - This chunk has information about how many channels there are in the audio, aka if it is *mono* or *stereo*
    - The third chunk is the audio itself.

## Files

### wav.h
- This file contains a `WAVHEADER` structure

## TODO
- [x] 2 Command line arguments; `input.wav` and `output.wav`. Error  = return 1
- [x] Open ´input.wav´ and check if it is a valid file
- [x] Read ´input.wav´ header and store it in `WAVHEADER` struct
- [x] Implement `check_format`; check `input.wav` header to confirm it is really a WAV file.
- [x] Open `output.wav` for writing
- [x] Write the header to `output.wav`
- [x] Implement `get_block_size` to get the size of each block.
    - This can be done by **multiplying the number of channels by bytes per sample**, avaliable in the header
- [x] Read audio data from `input.wav` and write it to `output.wav` in reverse order
    - This must be done by reading the last sample up to the first, until it reaches the header

## Functions 
### fseek
```c
fseek(FILE *stream, long int offset, int whence)
```
fseek changes the file position of a file stream to the given offset  

`FILE *stream` = File pointer  
`long int offset` = number of bytes to offset from whence  
`whence` = The position to where offset is added, it can be 3 different values:
    - `SEEK_SET`: Beggining of the file
    - `SEEK_CUR`: Current position
    - `SEEK_END`: End of the file

### ftell
```c
long int ftell(FILE *stream)
```
Returns the current file position of a file stream

`FILE *stream` = File pointer


