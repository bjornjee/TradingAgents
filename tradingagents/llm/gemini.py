from langchain_google_genai import ChatGoogleGenerativeAI
from .base import BaseLLMClient


class GeminiLLMClient(BaseLLMClient):
    """Google Gemini LLM client implementation."""

    def create_llm(
        self, model_name: str, temperature: float = 0.7
    ) -> ChatGoogleGenerativeAI:
        """Create a Gemini LLM instance.

        Args:
            model_name: Name of the model to use
            temperature: Temperature setting for the model

        Returns:
            An instance of ChatGoogleGenerativeAI
        """
        return ChatGoogleGenerativeAI(model=model_name, temperature=temperature)
