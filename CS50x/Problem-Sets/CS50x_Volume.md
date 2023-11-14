# Volume
[Problem Sets](./CS50x_Problem-Sets.md)

- WAV files have a 44-byte header containing file information. Each byte is a unsigned (non-negative) integer, `uint8_t`
- WAV files contain samples after the header. Each sample is a 2-byte (16 bits) signed integer (positive or negative), `int16_t`
