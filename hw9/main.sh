nasm -f elf hw9.asm
ld -m elf_i386 -s -o runscript hw9.o
./runscript