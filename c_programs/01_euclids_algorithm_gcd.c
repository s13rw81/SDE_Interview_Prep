// calculate the GCD of two numbers using Euclid's Method

# include <stdio.h>
int gcd(int num1, int num2)
{
	while(num2 != 0){

		int t = num1;
		num1 = num2;
		num2 = t % num1;
	}

	return num1;

}

int main()
{

	int res = gcd(100, 1451);
	printf("the gcd is : %d\n", res);
	return 0;

}
