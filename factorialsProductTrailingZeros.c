int factorialsProductTrailingZeros(int l, int r) {
    int a=0,s=0;
    a = (l-1)/5 + (l-1)/25;
    for (;l<=r;l++) {
        //a=0;
        if (l%5==0) a++;
        if (l%25==0) a++;
        s+=a;
    }
    return s;
}
