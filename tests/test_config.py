from src.config.settings import get_settings


def test_settings_loaded() -> None:
    s = get_settings()
    assert s.service_name == "cicd-predictor-demo"
    assert s.version
