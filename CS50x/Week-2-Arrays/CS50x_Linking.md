# Linking
Linking is the fourth and last step of compilation in C.
In this proccess the compiler fills the missing pieces and rearrages some of the code.
It arranges functions in the right order, links libraries. In case they are third party libraries you need to tell the linker about them through `clang (file.c) -library`.

The result of this proccess is a binary file named `a.out`, to have another name you can use `clang -o (name )(file.c)`
