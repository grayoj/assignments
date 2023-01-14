#!/bin/bash
echo "Cloning the repository for you."
git clone https://github.com/grayoj/assignments.git
echo "Installing all requirements."
echo "install python"
python --version
sudo add-apt-repository --remove ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get remove --purge python2
sudo apt install python3.10
