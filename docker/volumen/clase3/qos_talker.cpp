#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

auto create_qos_policy()
{
  // Configura el objeto QoS
  auto custom_qos = rclcpp::QoS(rclcpp::QoSInitialization::from_rmw(rmw_qos_profile_default));
  custom_qos.reliability(RMW_QOS_POLICY_RELIABILITY_RELIABLE);
  custom_qos.durability(RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL);
  custom_qos.history(RMW_QOS_POLICY_HISTORY_KEEP_ALL);
  // custom_qos.lifespan(5s);
  //custom_qos.keep_last(10);

  return custom_qos;

}

class Publisher_qos : public rclcpp::Node
{
public:
  Publisher_qos() : Node("qos_test")
  {
    // Configuramos el publisher con diferentes QoS
    publisher_ = this->create_publisher<std_msgs::msg::String>("topic_qos", create_qos_policy());
    timer_ = this->create_wall_timer(1s,[this](){this->timer_callback();});
    count_ = 0;
  }

private:
  void timer_callback()
  {
    auto message = std_msgs::msg::String();
    message.data = "Mensaje número: " + std::to_string(count_++);
    RCLCPP_INFO(this->get_logger(), "Se publicó: '%s'", message.data.c_str());
    publisher_->publish(message);
  }

  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Publisher_qos>());
  rclcpp::shutdown();
  return 0;
}
