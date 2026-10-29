from types import SimpleNamespace

from data_platform_copilot.config import Settings
from data_platform_copilot.llm.client import ClaudeClient


class FakeMessages:
    def __init__(self) -> None:
        self.last_kwargs: dict = {}

    def create(self, **kwargs):
        self.last_kwargs = kwargs
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text="hello")],
            usage=SimpleNamespace(input_tokens=3, output_tokens=2),
        )


def make_client() -> tuple[ClaudeClient, FakeMessages]:
    client = ClaudeClient(Settings(anthropic_api_key="test-key"))
    fake = FakeMessages()
    client._client = SimpleNamespace(messages=fake)
    return client, fake


def test_complete_returns_text_and_tokens():
    client, _ = make_client()  # arrange

    reply = client.complete(  # act
        messages=[{"role": "user", "content": "hi"}]
    )

    assert reply.text == "hello"  # assert
    assert reply.input_tokens == 3
    assert reply.output_tokens == 2


def test_system_prompt_only_sent_when_given():
    client, fake = make_client()

    client.complete(messages=[{"role": "user", "content": "hi"}], system="be brief")

    assert fake.last_kwargs["system"] == "be brief"

    client.complete(messages=[{"role": "user", "content": "hi"}])

    assert "system" not in fake.last_kwargs
