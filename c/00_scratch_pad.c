# include <stdio.h>
# include <string.h>

int gcd(int a, int b)
{
	while (b != 0)
	{
		int t = a;
		a = b;
		b = t % a;
	}

	return a;
}

int main()
{
	printf("GCD : %d\n", gcd(100,51));
	return 0;

}

