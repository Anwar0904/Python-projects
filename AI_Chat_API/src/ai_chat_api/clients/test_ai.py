from ai_chat_api.clients.ai_client import AIClient

client = AIClient()

print(client.generate_response("Say hello in one sentence."))
