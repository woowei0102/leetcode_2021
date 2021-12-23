#include<stdio.h>

void dayToyear(int y, int m, int d, int n) {
    int month[12] = {31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31};
    int i = m % 12 - 1;
    d += n;

    while(d / month[i % 12] && d != month[i % 12]) {
        m++;
        d -= month[i % 12];

        if (m / 12 && m != 12){
            y++;
            m -= 12;
        }
        
        if (y % 4 == 0) month[1] = 29;
        else month[1] = 28;

        i++;
    }
    printf("%4d-%02d-%02d\n", y, m, d);

}


int main() {
    int year = 2024, month = 1, day = 1;
    dayToyear(year, month, day, 59);
}