FROM ubuntu:python
MAINTAINER lijianfeng
ADD web.py /root
EXPOSE 4501
CMD python /root/web.py
