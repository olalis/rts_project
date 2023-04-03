FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y nano

RUN cd root
RUN mkdir rts
RUN cd rts
RUN mkdir programs

ENTRYPOINT ["tail", "-f", "/dev/null"]