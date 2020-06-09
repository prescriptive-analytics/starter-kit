FROM ubuntu:16.04


# install Anaconda Python 3.7
# `Anaconda3-2020.02-Linux-x86_64.sh` required
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

COPY ./Anaconda3-2020.02-Linux-x86_64.sh /tmp/
RUN /bin/bash /tmp/Anaconda3-2020.02-Linux-x86_64.sh -b -p /opt/conda && \
    rm /tmp/Anaconda3-2020.02-Linux-x86_64.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc

RUN apt update && \
    apt-get install -y build-essential libboost-all-dev cmake



