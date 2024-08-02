cmake_minimum_required(VERSION 3.28)

set(DEMO_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
file(GLOB_RECURSE demo_src "${DEMO_SRC_DIR}/*.h" "${DEMO_SRC_DIR}/*.cpp")

add_executable(${PROJECT_NAME} ${demo_src})
target_link_libraries(${PROJECT_NAME} PRIVATE 2DGameEngine)

GroupSourcesByFolder(${PROJECT_NAME})
