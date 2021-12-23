class Solution {
public:
    bool isHappy(int n) {
        if (n < 1) return false;
        set<int> seed;
        while(n != 1) {
            int temp = 0;
            while (n) {
                temp += (n % 10) * (n % 10);
                n /= 10;
            }
            n = temp;
            if (seed.count(n)) break;
            else seed.insert(n);
        }
        return n == 1;

    }
};