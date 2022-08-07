cmake_minimum_required(VERSION 3.22)
project(HyungJoonLEE C)

set(CMAKE_C_STANDARD 11)
set(Headers common.h)

add_executable(HyungJoonLEE ${PROJECT_SOURCE_DIR}
        2022-08-02-Longest-Substring-Without-Repeating-Characters.c 2022-08-03-Longest-Repeating-Character-Replacement.c 2022-08-04-Minimum-Window-Substring.c)
