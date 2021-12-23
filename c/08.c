1. result = 0, unsigned int沒有負數
2. C = 0xF1F1
3. 
int zero_bit_count(unsigned char n) {
    int cnt = 0;
    for(int i = 0; i < 8; i++){
        if (n & 0x1 == 0)
            cnt++;
        n >>= 1;
    }
    return cnt;
}
4. 