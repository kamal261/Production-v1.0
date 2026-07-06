"""
Temporary shim for seo_keyword.engine to satisfy imports in tests.
Replace with the real implementation when available.
"""
class KeywordEngine:
    def __init__(self, *args, **kwargs):
        raise RuntimeError(
            "KeywordEngine is a stub placeholder. Replace seo_keyword/engine.py with the real implementation."
        )

__all__ = ["KeywordEngine"]
