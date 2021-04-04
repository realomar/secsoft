section	.text
   global_start 
	
_start:	          ;tells linker entry point
   mov	edx,len   ; message length
   mov	ecx,msg   ; nessage being written
   mov	ebx,1     
   mov	eax,4     
   int	0x80      ;system call
	
   mov	eax,1     ;exit program
   int	0x80

section	.data
msg db 'system call test', 0xa
len equ $ - msg   
