FROM ubuntu
RUN apt update
RUN apt install python3.10 -y
RUN apt install python3-pip -y
WORKDIR /db
COPY requirementsdB.txt .
RUN pip3 install -r requirementsdB.txt
COPY dB.py .
CMD ["python3.10","db.py"]
