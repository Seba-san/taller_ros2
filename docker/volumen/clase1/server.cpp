#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"
#include <memory>

using std::shared_ptr;
using AddTwoInts = example_interfaces::srv::AddTwoInts;
using Logger = rclcpp::Logger;
using Node = rclcpp::Node;
using Request = AddTwoInts::Request;
using Response = AddTwoInts::Response;

void add(const shared_ptr<Request> request, shared_ptr<Response> response) {
    response->sum = request->a + request->b;
}

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = Node::make_shared("add_two_ints_server");
    auto service = node->create_service<AddTwoInts>("add_two_ints", &add);

    rclcpp::spin(node);
    rclcpp::shutdown();
}
