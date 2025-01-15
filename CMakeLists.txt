cmake_minimum_required(VERSION 3.30)
project(Cmain C)

set(CMAKE_C_STANDARD 11)

add_executable(Cmain main.c
        "Quadratic Eq.c"
        "Prime Coprime.c"
        "Even Odd.c"
        Fibionacci.c)
