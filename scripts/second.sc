fn insert(src, sub, pos){
    ret substr(src, 0, pos) + sub + substr(src, pos, len(src));
}

say upper(insert("hello world", ":) ", 4)), "\n";

say replace("aldo", "a", "ma");