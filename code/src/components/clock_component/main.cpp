#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <yarp/os/Network.h>
#include <yarp/os/BufferedPort.h>
#include <yarp/os/Bottle.h>

class ClockRos2Publisher : public rclcpp::Node
{
public:
    ClockRos2Publisher()
        : Node("clock_ros2_publisher")
    {
        publisher_ = this->create_publisher<std_msgs::msg::String>("clock", 10);
        yarp::os::Network yarp;
        if (!yarp.checkNetwork())
        {
            RCLCPP_ERROR(this->get_logger(), "YARP server not available!");
            return;
        }
        yarp_port_.open("/clock_ros2_publisher");
        yarp::os::Network::connect("/clock", "/clock_ros2_publisher");
        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(200), std::bind(&ClockRos2Publisher::timer_callback, this));
    }

private:
    void timer_callback()
    {
        yarp::os::Bottle *input = yarp_port_.read(false);
        if (input != nullptr)
        {
            auto message = std_msgs::msg::String();
            message.data = input->toString();
            RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
            publisher_->publish(message);
        }
    }

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    yarp::os::BufferedPort<yarp::os::Bottle> yarp_port_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    yarp::os::Network yarp;
    auto node = std::make_shared<ClockRos2Publisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
