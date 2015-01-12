## $(name)
$(name) is a simple dynamic typed, (turing complete :: todo) programming language

### Features ###
* Variables (duh)
* Functions
* Flow control statements
* Loops (for, inf loop, while)
* Loop exit statement
* Compound operators

### Data types ###
* Integer
* Float
* String
* Boolean

### TODO ###
* Arrays
* Modules


### Language description ###

#### Variables ####

variables are dynamically typed immediately declared upon use `number = 42;`

#### Functions ####

functions are declared via the following grammar

    fn func_name( [<arguments>,] ){
        < statements >
    }

    fn random(){
        ret 4;
    }

return value is specified with the `ret` keyword which, as expected, immediately halts function execution upon being called. Functions can have their private functions which are inaccessible to the outer scope.

#### Flow control ####

$(name) supports `if` statements for flow control via the following syntax

    if < expression > {
        < statements >
    }

nb: Brackets are mandatory, while parenthesis on the expression are optional


### Loops ###

$(name) supports two kind of loops, `for` and `while`

** for syntax **

    for variable in low -> high {
        < statements >
    }

nb: loop indexes are inclusive

** while syntax **

    while < expression > {
        < statements >
    }

there is also the alternative `for` syntax

    for {
        < statements >
    }

which acts as an infinite loop (which internally is expressed as a `while true {}` statement)

All loops can be prematurely exited via the `exit` statement when necessary







