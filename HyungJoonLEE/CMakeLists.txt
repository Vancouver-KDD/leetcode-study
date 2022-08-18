cmake_minimum_required(VERSION 3.22)
project(HyungJoonLEE C)

set(CMAKE_C_STANDARD 11)
set(Headers common.h)

add_executable(HyungJoonLEE ${PROJECT_SOURCE_DIR}
        2022-08-02-Longest-Substring-Without-Repeating-Characters.c 2022-08-03-Longest-Repeating-Character-Replacement.c 2022-08-04-Minimum-Window-Substring.c 2022-08-08-Valid-Palindrome.c 2022-08-09-Longest-Palindromic-Substring.c 2022-08-10-Palindromic-Substrings.c 2022-08-11-Maximum-Depth-of-Binary-Tree.c 2022-08-12-Same-Tree.c)
