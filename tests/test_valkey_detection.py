import importlib
import importlib.util

import tests.base as base


def test_django_valkey_not_enabled_when_module_missing(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(importlib.util, "find_spec", lambda _name: None)
        reloaded_base = importlib.reload(base)

        assert reloaded_base.HAS_DJANGO_VALKEY is False
        assert "django_valkey" not in reloaded_base.TEST_CACHES
        assert "django_valkey" not in reloaded_base.QUERY_SUPPORTED_CACHES
        assert "django_valkey" not in reloaded_base.OPERATIONAL_CACHES

    importlib.reload(base)
