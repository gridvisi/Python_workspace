from clip_client import Client
# https://clip-as-service.jina.ai/
# https://github.com/jina-ai/clip-as-service
c = Client('grpc://0.0.0.0:51000')
c.profile()