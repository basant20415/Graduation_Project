cmake_minimum_required(VERSION 3.0)

project(uart2)  # Project name

set(CMAKE_CXX_STANDARD 17)

# Include directories
include_directories(includes utils)

# Source files
set(SOURCE
    src/uart2.cpp
)

# Create the executable
add_executable(${PROJECT_NAME} ${SOURCE})

# Install the executable
install(TARGETS ${PROJECT_NAME} RUNTIME DESTINATION bin)
