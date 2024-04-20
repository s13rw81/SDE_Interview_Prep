#include <stdio.h>
#include <time.h>

int main()
{
    // Get the current time
    time_t t;
    struct tm *current_time;

    time(&t);
    current_time = localtime(&t);

    // Extract the components of the date
    int day = current_time->tm_mday;
    int month = current_time->tm_mon + 1;  // Months are 0-indexed, so add 1
    int year = current_time->tm_year + 1900;  // Years are years since 1900

    // Print today's date
    printf("Today's date is: %04d-%02d-%02d\n", year, month, day);

    return 0;
}