// linked list in c
# include <stdio.h>

int main()
{
	int x = 10;
	int *ptr = &x;

	printf("address of %d, is %d\n", x, ptr);
	printf("address of ptr %d, is %d\n", ptr, &ptr);
	printf("data at pointer %d, is %d\n", ptr, *ptr);
	printf("** pointer %d, is %d\n", ptr, **ptr);
	return 0;
}