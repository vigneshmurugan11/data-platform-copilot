from data_platform_copilot.config import get_settings
from data_platform_copilot.llm.client import ClaudeClient
from data_platform_copilot.logging_config import setup_logging

setup_logging()

client = ClaudeClient(get_settings())
reply = client.complete(
    messages=[{"role": "user", "content": "What is a data lineage graph?"}],
    system="You are a data platform assistant. Answer in one sentence.",
)
print(reply)
