FROM python:3.11.5-slim-bookworm

RUN apt update && apt install -y protobuf-compiler

WORKDIR /opt/project/

COPY grpc_client/requirements.txt /opt/project/
RUN pip install -r requirements.txt

COPY grpc_client/generate_proto.sh /opt/project/
COPY grpc_client/translator_server.proto /opt/project/
RUN chmod a+x generate_proto.sh && ./generate_proto.sh

COPY grpc_client/ /opt/project/
RUN rm -rf grpc_client_venv

ENTRYPOINT ["python3", "main.py"]
