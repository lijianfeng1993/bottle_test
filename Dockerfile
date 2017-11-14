FROM daocloud.io/python
MAINTAINER lijianfeng
ADD web.py /root
ADD bottle.py /root
EXPOSE 4501
CMD python /root/web.py
