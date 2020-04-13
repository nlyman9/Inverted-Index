FROM openkbs/jdk-mvn-py3-x11
COPY . InvIndex
WORKDIR InvIndex/data
CMD [ "python", "InvIndex.py" ]
