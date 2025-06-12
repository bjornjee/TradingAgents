from langchain_openai import ChatOpenAI
from .base import BaseLLMClient


class OpenRouterLLMClient(BaseLLMClient):
    """OpenRouter LLM client implementation."""

    def create_llm(self, model_name: str, temperature: float = 0.7) -> ChatOpenAI:
        """Create an OpenRouter LLM instance.

        Args:
            model_name: Name of the model to use
            temperature: Temperature setting for the model

        Returns:
            An instance of ChatOpenAI configured for OpenRouter
        """
        return ChatOpenAI(
            base_url=self.config['base_url'], model=model_name, temperature=temperature
        )
