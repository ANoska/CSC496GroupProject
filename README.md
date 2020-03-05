# CSC496GroupProject
Source code for CSC 496 Spring 2020 group project on evaluating the performance of containerization in cloud computing.

## Team Members
* Laura Gomez
* Kyree Fuller
* Lipika Chandrashekar
* Austin Noska

## Selected Benchmarks for performance
* https://github.com/thewmf/kvm-docker-comparison original project for reference
* SysBench with MySQL
* Memory Bandwidth STREAM Benchmark
* Network bandwidth measured with nuttcp
* The HPC-Linpack Benchmark

These benchmarks were chosen because together they offer a well rounded evaluation of performance. These 4 benchmarks will give us a perspective on high performance computing, memory, & networking capabilities.

### Selected Platform
* Docker

### HPC-Linpack Benchmark
High performance computing is useful in the cloud in many different scenarios. Whether it be providers having to partition a large amount of physical resources to fulfill requests, or consumers deploying computationally intensive applications, the integrity of a system's HPC is very important. The Linpack benchmark measures a system's HPC capabilities by seeing how fast it solves dense n X n systems of linear equations of the form Ax = B.

Our plan is to mimic the original experiment, but to make a few modifications.  
* We will be using the latest version of the Intel Math Kernel Library (https://software.intel.com/en-us/articles/intel-mkl-benchmarks-suite).
* Our Dockerfile base image will be based on BusyBox (https://www.busybox.net/) instead of Ubuntu as the maintainer of the original project recommends.  

These modifications should bring the dependencies up to date. As for deployment we will be modifying the original Dockerfile and bash script to provide automatic installation and execution of the benchmark and the results will be outputted for users to see.


### SysBench with MySQL
MySQL is a popular relation database that is widely used in the cloud and typically Stresses memory, IPC, filesystem, and networking subsystem. The SysBench will help us benchmark the performance of MySQL service under intensive load.  This will require us to create a MySQL container connected to a network, and also create another container instance that will run MySQL command line client against the original container.

We will use the original project as a blue print to guide us through this process. We will need to do some research to install MySQL as well as SysBench package. We will need to create two containers through docker and create the network through cloudlab. We will need to do research since the original project might be out of date.

### STREAM Benchmark
Memory bandwidth is the rate in which data can be read from or stored into computer memory. The STREAM Benchmark is a program that measures memory bandwidth when performing simple operations on arrays of a single dimension called "Vectors".  

The main determinate of the performance of a system is the system's bandwidth to memory. We plan to update sections of the github repository maintained by Ram Rajamony "thewmf/kvm-docker-comparison/Stream" to guide us through the process of automating the installation process of our experiment. This section of the experiment will allow us to investigate how bandwidth to memory impacts the performance of a system in a contained environment. 

### Network Bandwidth with nuttcp
Network bandwidth is the rate at which data flows over the network. This is a measure of throughput (amount per second) rather than speed (distance traveled per second).
For this project we will be using the nuttcp tool to measure network bandwidth between two systems connected over a network using docker and CloudLab. We will create two separate containers through docker for this. With the help of CloudLab we will attach both the containers on the host to a bridge and then connect the bridge to a network for testing. As mentioned above, we will also be using the pre existing github repository containing Experiments for the ISPASS 2015 poster "An Updated Performance Comparison of Virtual Machines and Linux Containers" as a reference and make modifications to it wherever required.
