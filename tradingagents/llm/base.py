from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from langchain.chat_models.base import BaseChatModel


class BaseLLMClient(ABC):
    """Abstract base class for LLM clients."""

    def __init__(self, config: Dict[str, Any]):
        """Initialize the LLM client with configuration.

        Args:
            config: Configuration dictionary containing LLM settings
        """
        self.config = config

    @abstractmethod
    def create_llm(self, model_name: str, temperature: float = 0.7) -> BaseChatModel:
        """Create an LLM instance with the specified model and temperature.

        Args:
            model_name: Name of the model to use
            temperature: Temperature setting for the model

        Returns:
            An instance of BaseChatModel
        """
        pass
