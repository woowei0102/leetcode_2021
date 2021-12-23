#include <stdio.h>

int main() {
    unsigned char map1 = 0x12;
    unsigned char map2 = 0xF4;

    for (int i = 0; i < 4; i++) {
        printf("%x, %x\n", ((map1 >> (4 + i)) & 0x1), ((map2 >> (2 + i)) & 0x1));
        if (((map1 >> (4 + i)) & 0x1) & ((map2 >> (2 + i)) & 0x1)) {
            map2 |= (0x1 << (2 + i));
        } else {
            map2 &= ~(0x1 << (2 + i));
        }
    }

    printf("%02x\n",map2);

    return 0;
}