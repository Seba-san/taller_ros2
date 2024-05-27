cmake_minimum_required(VERSION 3.8)
project(test_qos_pkg)

# Default to C++14, adjust if you need a different C++ standard
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# Include directories
include_directories(include)

# Declare executables
add_executable(subscriber_node src/qos_listener.cpp)
add_executable(publisher_node src/qos_talker.cpp)

# Specify libraries to link a library or executable target against
ament_target_dependencies(subscriber_node
  rclcpp
  std_msgs
)
ament_target_dependencies(publisher_node
  rclcpp
  std_msgs
)

# Install targets
install(TARGETS
  subscriber_node
  publisher_node
  DESTINATION lib/${PROJECT_NAME}
)

# Export dependencies
ament_package()

