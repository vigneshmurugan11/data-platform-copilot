import logging
from dataclasses import dataclass

import anthropic

from data_platform_copilot.config import Settings

logger = logging.getLogger(__name__)


@dataclass
class LLMReply:
    text: str
    input_tokens: int
    output_tokens: int


class ClaudeClient:
    def __init__(self, settings: Settings) -> None:
        self._client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
        self._model = settings.anthropic_model

    def complete(self, messages: list[dict], system: str | None = None) -> LLMReply:
        kwargs = {}
        if system is not None:
            kwargs["system"] = system

        response = self._client.messages.create(
            model=self._model, max_tokens=1024, messages=messages, **kwargs
        )

        text = "".join(block.text for block in response.content if block.type == "text")

        logger.info(
            "tokens in=%d out=%d",
            response.usage.input_tokens,
            response.usage.output_tokens,
        )
        return LLMReply(
            text=text,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
        )
