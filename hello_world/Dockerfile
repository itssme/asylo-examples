FROM gcr.io/asylo-framework/asylo

COPY . /opt/project/

WORKDIR /opt/project/

# build below in run command, problem is that the build cache is not used otherwise
#RUN bazel build //hello_world

ENTRYPOINT ["bazel", "run", "//hello_world", "--", "--names='Test1, Test2'"]
