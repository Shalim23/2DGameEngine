cmake_minimum_required(VERSION 3.28)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(ADDITIONAL_INCLUDE_PATH "${CMAKE_SOURCE_DIR}/Tools/CMake")

set(ENGINE_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
file(GLOB_RECURSE engine_src "${ENGINE_SRC_DIR}/*.h" "${ENGINE_SRC_DIR}/*.cpp")

set(ENGINE "2DGameEngine")

add_library(${ENGINE} STATIC ${engine_src})
target_compile_definitions(${ENGINE} PUBLIC $<$<CONFIG:DebugEditor>:EDITOR=1>)
target_include_directories(${ENGINE} PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/Public")
target_include_directories(${ENGINE} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}")

if(UNIX)
    message(FATAL_ERROR "UNIX not implemented!")
else()
    set(DEPS_PATH "${CMAKE_SOURCE_DIR}/Deps")
    set(DEPS_BIN_PATH "${DEPS_PATH}/bin/_deps")
    set(DEPS_LIBS_PATH "${DEPS_PATH}/bin/Release")

    target_include_directories(${ENGINE} PUBLIC "${DEPS_BIN_PATH}/sdl2-src/include")
    set(SDL2_LIBRARIES "${DEPS_LIBS_PATH}/SDL2.lib;${DEPS_LIBS_PATH}/SDL2main.lib")

    set(imgui_lib "${DEPS_LIBS_PATH}/imgui_lib.lib")
    set(imgui_includes "${DEPS_BIN_PATH}/imgui-src")
    
    target_include_directories(${ENGINE} PRIVATE
        $<$<OR:$<CONFIG:Debug>,$<CONFIG:DebugEditor>>:${imgui_includes}>
    )
    
    target_link_libraries(${ENGINE} PRIVATE ${SDL_LIBRARIES})
    target_link_libraries(${ENGINE} PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:DebugEditor>>:${imgui_lib}>)
endif()

include(${ADDITIONAL_INCLUDE_PATH}/Functions.cmake)
GroupSourcesByFolder(${ENGINE})
