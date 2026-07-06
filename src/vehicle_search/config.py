import os
import tomllib
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AppConfig:
    data_path: Path | str
    vehicle_api_url: str | None = None

def load_config(config_path: str | None = None) -> AppConfig:
    values = {}

    if config_path:
        path = Path(config_path)

        if path.exists():
            print(f"Path exists {path}")
            with path.open("rb") as f: # Reads as bytes.
                config_file = tomllib.load(f)

            values.update(config_file.get("vehicle_search", {}))

    if data_path := os.getenv("VEHICLE_SEARCH_DATA_PATH"):
        values["data_path"] = data_path

    if vehicle_api_url := os.getenv("VEHICLE_API_URL"):
        values["vehicle_api_url"] = vehicle_api_url

    print(f"values are {values}")

    if not values.get("data_path"):
        raise ConfigError(
            "Missing required config value: data_path. "
            "Set it in config.toml under [vehicle_search] or use "
            "the VEHICLE_SEARCH_DATA_PATH environment variable."
        )
    return AppConfig(**values)


@lru_cache(maxsize=1)
def get_config(config_path: str | None = None) -> AppConfig:
    return load_config(config_path)


def clear_config_cache() -> None:
    get_config.cache_clear()