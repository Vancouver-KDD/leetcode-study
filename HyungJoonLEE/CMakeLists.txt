cmake_minimum_required(VERSION 3.22)
project(HyungJoonLEE C)

set(CMAKE_C_STANDARD 11)
set(Headers common.h)

add_executable(HyungJoonLEE ${PROJECT_SOURCE_DIR}
        2022-07-18-Merge-Intervals.c 2022-07-19-Non-overlapping-Intervals.c 2022-07-21-Linked-List-Cycle.c 2022-07-22-Merge-Two-Sorted-Lists.c)
