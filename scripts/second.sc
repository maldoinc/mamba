// adds 10
fn add_ten(n){
    // says lol!!
    fn lol(){
        fn getstr(){ ret "lol"; }

        say getstr();
    }

    say lol();

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

fn fib(n){
    if n == 0 or n == 1{ ret n; }

    ret fib(n - 1) + fib(n - 2);
}

for i in 1 -> 10{
    say fib(i), "\n";
}