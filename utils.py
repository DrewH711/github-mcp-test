from pydantic_ai.models import Model
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.azure import AzureProvider
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider
from anthropic import AsyncAnthropicFoundry
from os import getenv

def load_model(name : str = "KimiK2.6") -> Model:

    openai_endpoint = "https://dashboard-eastus2-resource.services.ai.azure.com/openai/v1"
    token = getenv("FOUNDRY_API_KEY")

    if name.lower() == "kimi-k2.6":
        return OpenAIChatModel(
            'Kimi-K2.6', 
            provider = AzureProvider(
                azure_endpoint=openai_endpoint,
                api_key=token
                ),
            settings = {
                "thinking" : True,
                "max_tokens" : 3000,
                "temperature" : 0.5
                }
        )

    elif name.lower() == "chatgpt":
        return OpenAIChatModel(
            'gpt-chat-latest',
            provider = AzureProvider(
                azure_endpoint=openai_endpoint,
                api_key=token
                ),
            settings = {
                "thinking" : True,
                }
        )
    
    elif name.lower() == "claude":
        foundry_client = AsyncAnthropicFoundry(
            api_key=token,
            base_url="https://dashboard-eastus2-resource.services.ai.azure.com/anthropic"
        )

        return AnthropicModel(
            'claude-opus-4-8',
            provider = AnthropicProvider(anthropic_client=foundry_client)
        )


    else:
        raise Exception("Invalid model name. Available models are kimi-k2.6, chatgpt, or claude")