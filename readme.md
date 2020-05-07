# Starter Kit of Mobility Intervention of Epidemics Challenge

## 1. Download the starter-kit.

```
git clone https://github.com/prescriptive-analytics/starter-kit.git
```

## 2. Preparation

##### 2.1 Install boost library and make sure you have libboost path added to your system path

- Mac OS: `brew install boost`

- Linux:

    - Installation with `sudo apt-get install libboost-dev`
    - Locate libboost_system.so with `locate libboost_system.so`
    - Add the last step paths to your system path with `export PATH={your paths}:$PATH`

- Windows: Please refer to [install-boost-build](https://www.boost.org/doc/libs/1_73_0/more/getting_started/windows.html#install-boost-build)

##### 2.2 Specify python environment

Make sure you have compatible python environment that marches with the simulator. Currently, we support the following versions of python:

- Mac OS: python 3.6, 3.7
- Linux: python 3.6


## 3. Start running the code by running `python example.py`.

For other provided intervention templates and APIs, please visit the [documation](https://hzw77-demo.readthedocs.io/en/latest/introduction.html)

## 4. For submission, please run `python submit.py`, make sure:

- You are running the simulation for 840 time steps (60 simulation days in simulator). 

- The experiments will be run for 10 times. All the log will go into one file `sub_xxx.txt`.

- Please upload the `sub_xxx.txt` to the website.
