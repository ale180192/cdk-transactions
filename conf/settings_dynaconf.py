from dynaconf import LazySettings

_settings = LazySettings(
    ENVVAR_PREFIX_FOR_DYNACONF=False,
    ROOT_PATH_FOR_DYNACONF="./conf/",
    settings_files=["settings.toml", ]
)

class Settings:

    def get_value(self, key: str) -> object:
        return _settings[key]

    def get_id(self, resource: str) -> str:
        return f"{_settings.ENV}-{_settings.PROJECT_NAME}-{resource}"