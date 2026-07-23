import os
import tomllib
from dataclasses import dataclass
from functools import lru_cache
from importlib.resources import files
from pathlib import Path
from typing import Any


class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AppConfig:
    data_path: Path | str
    vehicle_api_url: str | None = None

@dataclass
class AppContext:
    config: AppConfig
    force: bool

def load_config(config_path: Path | None = None) -> AppConfig:
    values = {}

    config_file = read_toml(config_path)
    values.update(config_file.get("vehicle_search", {}))

    if data_path := os.getenv("VEHICLE_SEARCH_DATA_PATH"):
        values["data_path"] = data_path

    if vehicle_api_url := os.getenv("VEHICLE_API_URL"):
        values["vehicle_api_url"] = vehicle_api_url

    if not values.get("data_path"):
        raise ConfigError(
            "Missing required config value: data_path. "
            "Set it in config.toml under [vehicle_search] or use "
            "the VEHICLE_SEARCH_DATA_PATH environment variable."
        )
    return AppConfig(**values)

def read_toml(path: Path | None = None) -> dict[str, Any]:
    if path is not None:
        with path.open("rb") as config_file:
            return tomllib.load(config_file)
    
    default_config = files("vehicle_search").joinpath("defaults", "config.toml",)

    with default_config.open("rb") as config_file:
        return tomllib.load(config_file)
    
@lru_cache(maxsize=1)
def get_config(config_path: Path | None = None) -> AppConfig:
    return load_config(config_path)


def clear_config_cache() -> None:
    get_config.cache_clear()