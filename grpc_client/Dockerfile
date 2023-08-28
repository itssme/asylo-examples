FROM python:3.11.5-slim-bookworm

COPY grpc_client/ /opt/project/
WORKDIR /opt/project/
RUN apt update && apt install -y protobuf-compiler

SHELL ["/bin/bash", "-c"]
RUN source grpc_client_venv/bin/activate

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN chmod a+x generate_proto.sh && ./generate_proto.sh

ENTRYPOINT ["grpc_client_venv/bin/python", "main.py"]
