cmake_minimum_required(VERSION 3.28)

project(2DGameEngineDeps LANGUAGES CXX)

set(FETCHCONTENT_QUIET FALSE)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include("FetchContent.cmake")
include("Imgui.cmake")

function(copy_libs path)
    add_custom_command(TARGET imgui_lib POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
    $<$<CONFIG:Release>:${CMAKE_BINARY_DIR}/_deps/${path}>
    $<$<CONFIG:Release>:${CMAKE_BINARY_DIR}/Release>
    )
endfunction()

copy_libs("sdl2-build/Release/SDL2.dll")
copy_libs("sdl2-build/Release/SDL2.lib")
copy_libs("sdl2-build/Release/SDL2main.lib")
