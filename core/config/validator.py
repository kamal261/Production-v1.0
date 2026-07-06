from core.exceptions import ConfigurationError


class ConfigValidator:

    REQUIRED = [
        "site_url",
        "wp_site",
        "wp_username",
        "wp_app_password"
    ]

    @classmethod
    def validate(cls, config: dict):

        missing = []

        for key in cls.REQUIRED:

            if not config.get(key):

                missing.append(key)

        if missing:

            raise ConfigurationError(
                f"Missing configuration: {', '.join(missing)}"
            )

        return True