FROM gcr.io/asylo-framework/asylo

COPY . /opt/project/

WORKDIR /opt/project/

ENTRYPOINT ["bazel", "run", "//grpc_server:grpc_server_sgx_sim",  "--", "--server_max_lifetime=60000", "--port=4242"]
