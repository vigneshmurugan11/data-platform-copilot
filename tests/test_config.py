from data_platform_copilot.config import get_settings


def test_get_settings_reads_api_key(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")

    settings = get_settings()

    assert settings.anthropic_api_key == "test-key"