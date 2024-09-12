#!/bin/bash

# 定义网络配置文件路径
CONFIG_FILE="/etc/sysconfig/network-scripts/ifcfg-eth0"

# 提示用户输入新的 IPv4 和 IPv6 地址
read -p "请输入新的 IPv4 地址（例如：192.168.1.125）注意不要加/24: " NEW_IPV4
read -p "请输入新的 IPv6 地址（例如：2a01:4f8:221:38d9::125）注意不要加/26: " NEW_IPV6

# 使用 sed 命令替换文件中的 IPv4 和 IPv6 地址
sudo sed -i "s|IPADDR=.*|IPADDR=\"$NEW_IPV4\"|g" $CONFIG_FILE
sudo sed -i "s|IPV6ADDR=.*|IPV6ADDR=\"$NEW_IPV6\"|g" $CONFIG_FILE

# 提示用户文件已修改
echo "网络配置文件已修改为："
echo "IPv4: $NEW_IPV4"
echo "IPv6: $NEW_IPV6"

# 重启网络服务以应用更改
sudo systemctl restart network

echo "网络配置已应用并重启。"
