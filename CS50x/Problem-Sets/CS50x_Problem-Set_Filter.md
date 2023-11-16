# Filter
[Problem Sets](./CS50x_Problem-Sets.md)

## Bitmap
- A 24-bit BMP file stores a pixel every 24 bits.
- A BPM file has two data structures as headers
    - BITMAPFILEHEADER is 14 bytes long
    - BITMAIINFOHEADER is 40 bytes long
- After the header is the bitmap
    - BMP stores the triples backwards (instead of RGB it is BGR)
        - 8 bits for blue, 8 bits for green, 8 bits for red = 24 bits.
        - Hexadecimal digits are 4 bits long.
- A bitmap can be represented as a 2 dimensional array: `array[row][pixel]`

## Filtering
- A grayscale filter is done by making each value of RGB equal
    - If the original RGB value was high, the new value must also be high. If it was low, it should also be low
- Sepia filter is done my computing new RGB values with the following formula, rounded to the nearest integer.
    ```
    sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
    sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
    sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
    ```
- Reflection is done my rearranging the pixels from left to right
    - Temporary variables are necessary to achieve this.

- Blur is done by averaging the RGB value of each pixel within 1 row 1 column around the original pixel (a 3x3 grid)
    - This is done by nesting loops, looping through every pixel and through the adjacent pixels of every pixel  

- Edge filtering works by creating two new values for each color channel of each pixel, *Gx* and *Gy*
    - *Gx* is a weighted sum of the horizontal adjacent pixels's channels multiplied by the sobel *Gx* kernel
        |-1 |0|+1|
        |---|-|--|
        |-2 |0|+2|
        |-1 |0|+1|
    - *Gy* is a weighted sum of the vertical adjacent pixels's channels multiplied by the sobel *Gy* kernel
        |-1|-2|-1|
        |--|--|--|
        |0 | 0| 0|
        |+1|+2|+1|
        - This is done by looping through every pixel and looping through the adjacent pixels of every pixel, and multiplying their channel values by the *Gx* and *Gy* according to their position.

## Files
### bmp.h
- aliases for primitive data types
- headers structures
- ***RGB Structure of each pixel***

### filters.c
- define filters as "bgrs"
- opens file and stores pixels in a 2D array image
- switch statement calls filter functions
- defines filter functions
    - Each function takes a 2D array image as argument
        - `image[0][0]` represents the first pixel in the first row


## TODO
Implement functions in `helpers.c`:
- [x] Grayscale
- [x] Sepia
- [x] Reflect
- [x] Blur
- [x] Edges
    
