# Binary
Binary is the numeral system a computer uses to represent information
Everything is represented by 0's and 1's, these are called "bits"

It uses the base 2 numeral-system, where every digit is multiplied by 2<sup>n</sup>

## Representation

To represent numbers the following calculation is performed:
> x<sup>2<sup>n</sup></sup>

Where:
- x = 0 or 1, if it's 0 the result is always 0
- n = n is restricted to non negative values, the first being 1 and 2, and then 2 multiplied by a certain number of times (0, 1, 2, 4, 8, 16, 32, 64, 128, 256....)

Then the results are summed up, giving the final number

### Examples

> 000 =  0<sup>2<sup>2</sup></sup>0<sup>2<sup>1</sup></sup>0<sup>2<sup>0</sup></sup> = 0<sup>4</sup>0<sup>2</sup>0<sup>1</sup>  = 0+0+0 = 0

> 001 = 0<sup>4</sup>0<sup>2</sup>1<sup>1</sup> = 0+0+1 =  1
> 000 = 0<sup>4</sup>1<sup>2</sup>0<sup>1</sup> = 0+2+0 = 2
> 000 =  0<sup>4</sup>1<sup>2</sup>1<sup>1</sup> = 0+2+1 =  3
> 000 =  1<sup>4</sup>0<sup>2</sup>0<sup>1</sup> = 4+0+0 =  4
.....
> 111 = 1<sup>4</sup>1<sup>2</sup>1<sup>1</sup> = 4+2+1 = 7

To represent the number 8 an additional digit (aka an additional bit) is required
> 1000 = 8+0+0+0 = 8
