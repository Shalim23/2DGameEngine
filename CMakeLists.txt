cmake_minimum_required(VERSION 3.28)

project(2DGameEngine LANGUAGES CXX)

set(FETCHCONTENT_QUIET FALSE)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_CXX_FLAGS_DEBUGEDITOR "${CMAKE_CXX_FLAGS_DEBUG}")
set(CMAKE_C_FLAGS_DEBUGEDITOR "${CMAKE_C_FLAGS_DEBUG}")
set(CMAKE_EXE_LINKER_FLAGS_DEBUGEDITOR "${CMAKE_EXE_LINKER_FLAGS_DEBUG}")
set(CMAKE_SHARED_LINKER_FLAGS_DEBUGEDITOR "${CMAKE_SHARED_LINKER_FLAGS_DEBUG}")

set(ADDITIONAL_INCLUDE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/Tools/CMake")

include(${ADDITIONAL_INCLUDE_PATH}/FetchContent.cmake)
include(${ADDITIONAL_INCLUDE_PATH}/Imgui.cmake)

set(SDL_LIBRARIES ${SDL_LIBRARIES} SDL2main SDL2 SDL2_image SDL2_ttf)

set(SRC_DIR "${CMAKE_SOURCE_DIR}/Source")
file(GLOB_RECURSE src "${SRC_DIR}/*.h" "${SRC_DIR}/*.cpp")

add_executable(${PROJECT_NAME} ${src})
target_compile_definitions(${PROJECT_NAME} PRIVATE $<$<CONFIG:DebugEditor>:EDITOR=1>)

target_link_libraries("${PROJECT_NAME}" PRIVATE ${SDL_LIBRARIES} nlohmann_json::nlohmann_json)
target_link_libraries("${PROJECT_NAME}" PRIVATE debug imgui_lib)

include(${CMAKE_CURRENT_SOURCE_DIR}/Tools/CMake/GroupSourcesByFolder.cmake)
GroupSourcesByFolder(${PROJECT_NAME})
