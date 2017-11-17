int arrayPacking(int[] a) {
    long res = 0;
    for (int i = a.length-1; i >= 0; i--) {
        res |= a[i];
        res <<= 8;
    }
    res >>= 8;
    return (int) res;
}
