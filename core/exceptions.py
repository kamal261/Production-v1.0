class SEOAIError(Exception):
    pass


class ConfigurationError(SEOAIError):
    pass


class ProviderError(SEOAIError):
    pass


class CrawlError(SEOAIError):
    pass


class WordPressError(SEOAIError):
    pass