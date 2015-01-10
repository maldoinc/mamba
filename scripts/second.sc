for i in 1 -> 10 {
    for j in 1 -> 10 {
        say i * j, " ";

        if j == 5 {
            exit;
        }
    }

    say "\n";
}