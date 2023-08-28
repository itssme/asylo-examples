import grpc
import translator_server_pb2  # Import the generated proto classes
import translator_server_pb2_grpc  # Import the generated grpc classes


def main():
    channel = grpc.insecure_channel('grpc_server:4242')
    client = translator_server_pb2_grpc.TranslatorStub(channel)
    request = translator_server_pb2.GetTranslationRequest(input_word="kubernetes")
    response = client.GetTranslation(request)
    print("Translated word:", response.translated_word)


if __name__ == '__main__':
    main()
