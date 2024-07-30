cmake_minimum_required(VERSION 3.28)

project(2DGameEngine LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_CXX_FLAGS_DEBUGEDITOR "${CMAKE_CXX_FLAGS_DEBUG}")
set(CMAKE_C_FLAGS_DEBUGEDITOR "${CMAKE_C_FLAGS_DEBUG}")
set(CMAKE_EXE_LINKER_FLAGS_DEBUGEDITOR "${CMAKE_EXE_LINKER_FLAGS_DEBUG}")
set(CMAKE_SHARED_LINKER_FLAGS_DEBUGEDITOR "${CMAKE_SHARED_LINKER_FLAGS_DEBUG}")

set(ADDITIONAL_INCLUDE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/Tools/CMake")

set(SRC_DIR "${CMAKE_SOURCE_DIR}/Source")
file(GLOB_RECURSE src "${SRC_DIR}/*.h" "${SRC_DIR}/*.cpp")

add_executable(${PROJECT_NAME} ${src})
target_compile_definitions(${PROJECT_NAME} PRIVATE $<$<CONFIG:DebugEditor>:EDITOR=1>)

if(UNIX)
    message(FATAL_ERROR "UNIX not implemented!")
else()
    set(DEPS_PATH "${CMAKE_SOURCE_DIR}/Deps")
    set(DEPS_BIN_PATH "${DEPS_PATH}/bin/_deps")
    set(DEPS_LIBS_PATH "${DEPS_PATH}/bin/Release")

    include_directories("${DEPS_BIN_PATH}/sdl2-src/include")
    set(SDL2_LIBRARIES "${DEPS_LIBS_PATH}/SDL2.lib;${DEPS_LIBS_PATH}/SDL2main.lib")

    set(imgui_lib "${DEPS_LIBS_PATH}/imgui_lib.lib")
    set(imgui_includes "${DEPS_BIN_PATH}/imgui-src")
    
    target_include_directories(${PROJECT_NAME} PRIVATE
        $<$<OR:$<CONFIG:Debug>,$<CONFIG:DebugEditor>>:${imgui_includes}>
    )
    
    target_link_libraries(${PROJECT_NAME} PRIVATE ${SDL_LIBRARIES})
    target_link_libraries(${PROJECT_NAME} PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:DebugEditor>>:${imgui_lib}>)
endif()

include(${ADDITIONAL_INCLUDE_PATH}/Functions.cmake)
GroupSourcesByFolder(${PROJECT_NAME})
