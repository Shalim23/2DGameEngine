cmake_minimum_required(VERSION 3.28)

project(2DGameEngineDemo LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(ADDITIONAL_INCLUDE_PATH "${CMAKE_SOURCE_DIR}/Tools/CMake")

set(DEMO_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
file(GLOB_RECURSE demo_src "${DEMO_SRC_DIR}/*.h" "${DEMO_SRC_DIR}/*.cpp")

add_executable(${PROJECT_NAME} ${demo_src})
target_link_libraries(${PROJECT_NAME} PRIVATE 2DGameEngine)

include(${ADDITIONAL_INCLUDE_PATH}/Functions.cmake)
GroupSourcesByFolder(${PROJECT_NAME})
