# Compiling
Compiling is the second step of compilation in C.
In this stage the already preprocessed code is turned into [Assembly](Assembly) code.

## Example
Take the following C code as example:

```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("Hello, %s\n", answer);
}
```

After being compiled to assembly it will look like this:

```assembly
        .text
        .file   "hello.c"
        .globl  main                            # -- Begin function main
        .p2align        4, 0x90
        .type   main,@function
main:                                   # @main
        .cfi_startproc
# %bb.0:
        pushq   %rbp
        .cfi_def_cfa_offset 16
        .cfi_offset %rbp, -16
        movq    %rsp, %rbp
        .cfi_def_cfa_register %rbp
        subq    $16, %rsp
        xorl    %eax, %eax
        movl    %eax, %edi
        leaq    .L.str(%rip), %rsi
        movb    $0, %al
        callq   get_string@PLT
        movq    %rax, -8(%rbp)
        movq    -8(%rbp), %rsi
        leaq    .L.str.1(%rip), %rdi
        movb    $0, %al
        callq   printf@PLT
        xorl    %eax, %eax
        addq    $16, %rsp
        popq    %rbp
        .cfi_def_cfa %rsp, 8
        retq
.Lfunc_end0:
        .size   main, .Lfunc_end0-main
        .cfi_endproc
                                        # -- End function
        .type   .L.str,@object                  # @.str
        .section        .rodata.str1.1,"aMS",@progbits,1
.L.str:
        .asciz  "What's your name? "
        .size   .L.str, 19

        .type   .L.str.1,@object                # @.str.1
.L.str.1:
        .asciz  "Hello, %s\n"
        .size   .L.str.1, 11

        .ident  "Ubuntu clang version 14.0.0-1ubuntu1"
        .section        ".note.GNU-stack","",@progbits
        .addrsig
        .addrsig_sym get_string
        .addrsig_sym printf
```

**You can generate a assembly file by typing `clang -S (file.c)`**
