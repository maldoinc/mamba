fn add_ten(n){
    ret n + 10;
}

fn add10_divide(a, b){
    ret add_ten(a) / b;
}

fn fac(n){
    if n <= 0 {
        ret 1;
    }

    ret n * fac(n-1);
}

say add_ten(10), "\n";
say fac(10), "\n";
say add10_divide(10, 4);