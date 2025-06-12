from typing import Dict, Any, List, Tuple
from .base import BaseLLMClient
from .openrouter import OpenRouterLLMClient
from .gemini import GeminiLLMClient


class LLMFactory:
    """Factory for creating LLM instances from different providers."""

    _providers = {
        'openrouter': OpenRouterLLMClient,
        'gemini': GeminiLLMClient,
    }

    @classmethod
    def register_provider(cls, name: str, provider_class: type[BaseLLMClient]):
        """Register a new LLM provider.

        Args:
            name: Name of the provider
            provider_class: Provider class that implements BaseLLMClient
        """
        cls._providers[name] = provider_class

    @classmethod
    def create_llm(
        cls,
        config: Dict[str, Any],
        provider: str,
        model_name: str,
        temperature: float = 0.7,
    ) -> BaseLLMClient:
        """Create an LLM instance from the specified provider.

        Args:
            config: Configuration dictionary
            provider: Name of the LLM provider
            model_name: Name of the model to use
            temperature: Temperature setting for the model

        Returns:
            An LLM instance

        Raises:
            ValueError: If the provider is not supported
        """
        if provider not in cls._providers:
            raise ValueError(f'Unsupported LLM provider: {provider}')

        client = cls._providers[provider](config)
        return client.create_llm(model_name, temperature)
