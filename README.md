# What is this?
This tool is used for taking screenshots of webpages

# Install Python Packages
Website for screenshotting websites. Lines to install all required packages follows.

Assuming you're using Debian (like you said you were)
```
pip install jinja2=3.0.0 quart selenium
```

# Python 3.11.1 installation for debian:
```
cd /tmp/
wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
tar -xzvf Python-3.11.1.tgz
cd Python-3.11.1/

apt update
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev

./configure --enable-optimizations
make -j `nproc`
```
Give it a test:
```
python3.11 -V
```
You should get:
```
Python 3.11.1
```

# Making python 3.11 default
```
sudo ln -s /usr/local/bin/python
sudo ln -s /usr/local/bin/python3.11 /usr/local/bin/python
```
Again, test it.
```
python -V
```
You should get:
```
Python 3.11.1
```

# Install Firefox
```
apt-get update
apt-get install firefox-esr
```

i don't know how to test this one

# Running it
hypercorn --bind 127.0.0.1:5000 main

# Credits

This screenshotting website utility was made for [BGP.TOOLS](https://bgp.tools) by [Ryan G](https://erate.rs) (eraters) https://github.com/eraters