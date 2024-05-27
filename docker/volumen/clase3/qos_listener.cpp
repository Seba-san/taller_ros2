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
  //custom_qos.keep_last(10);
  //custom_qos.deadline(1s);

  return custom_qos;
}

class Subscriber_qos : public rclcpp::Node
{
public:
  Subscriber_qos() : Node("qos_test_subs")
  {
    subscriber_ = this->create_subscription<std_msgs::msg::String>(
      "topic_qos", create_qos_policy(), std::bind(&Subscriber_qos::topic_callback, this, std::placeholders::_1));
    count_ = 0;
    //subscriber_->add_event_handler
  }

private:
  void topic_callback(const std_msgs::msg::String::SharedPtr msg)
  {
    RCLCPP_INFO(this->get_logger(), "Se recibió: '%s', mensaje número %i", msg->data.c_str(),count_);
    count_++;
  }

  std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String>> subscriber_;
  int count_;
};

int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Subscriber_qos>());
  rclcpp::shutdown();
  return 0;
}
