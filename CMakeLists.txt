cmake_minimum_required(VERSION 3.16)
project(VOX_OMEGA_QuantumFS VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Enable optimization for release builds
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -march=native")
endif()

# Create executable
add_executable(vox_omega_fs vox_omega_quantum_fs.cpp)

# Include directories if needed
target_include_directories(vox_omega_fs PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

# Link libraries if needed (filesystem requires C++17)
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    target_link_libraries(vox_omega_fs stdc++fs)
endif()

# Installation (optional)
install(TARGETS vox_omega_fs DESTINATION bin)