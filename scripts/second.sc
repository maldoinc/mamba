fn fac(n) {
    if n <= 0{
        ret 1;
    }

    ret n * fac(n - 1);
}

n = 5;
say n, "! = ", fac(n);