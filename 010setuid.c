#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char ** const argv) {
	//setgid(999);
	//setuid(999);
	//seteuid(999);
	//setegid(999);
	setreuid(999, 999);
	//setregid(999, 999);
	//execvp("/bin/sh", NULL);
	//execvp("/tmp/sh", NULL);
	system(argv[1]);
}