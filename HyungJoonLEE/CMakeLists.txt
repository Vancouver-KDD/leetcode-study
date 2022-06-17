cmake_minimum_required(VERSION 3.22)
project(HyungJoonLEE C)

set(CMAKE_C_STANDARD 11)
set(Headers common.h)

add_executable(HyungJoonLEE ${PROJECT_SOURCE_DIR}
               2022-06-14-Find-Minimum-in-Rotated-Sorted-Array.c 2022-06-15-Search-in-Rotated-Sorted-Array.c 2022-06-16-3Sum.c)
