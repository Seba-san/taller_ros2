#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/transform_broadcaster.h"
#include "geometry_msgs/msg/transform_stamped.hpp"
#include "tf2/LinearMath/Quaternion.h"

class FixedTFBroadcaster : public rclcpp::Node
{
public:
    FixedTFBroadcaster() : Node("fixed_tf2_broadcaster")
    {
        broadcaster_ = std::make_shared<tf2_ros::TransformBroadcaster>(*this);
        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(100),
            std::bind(&FixedTFBroadcaster::timer_callback, this));
    }
private:
    void timer_callback()
    {
        geometry_msgs::msg::TransformStamped t;
        // Fill in the header
        t.header.stamp = this->get_clock()->now();
        t.header.frame_id = "completar";
        t.child_frame_id = "completar";
        // Set the translation
        t.transform.translation.x = 0.0;
        t.transform.translation.y = 0.0;
        t.transform.translation.z = 0.0;
        // Set the rotation (no rotation here)
        tf2::Quaternion q;
        q.setRPY(0, 0, 0);  // Roll, Pitch, Yaw
        t.transform.rotation.x = q.x();
        t.transform.rotation.y = q.y();
        t.transform.rotation.z = q.z();
        t.transform.rotation.w = q.w();
        // Send the transformation
        broadcaster_->sendTransform(t);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    std::shared_ptr<tf2_ros::TransformBroadcaster> broadcaster_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<FixedTFBroadcaster>());
    rclcpp::shutdown();
    return 0;
}
