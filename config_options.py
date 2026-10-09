# 01 - Configuration file in order to retrieve YAML parameters
from pathlib import Path

import yaml


class ConfigOptions:
    _cfg_path = Path(__file__).resolve().parent / "config.yml"

    with open(_cfg_path, "r", encoding="utf-8") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        base_url = "https://" + cfg["url"]
        browser = cfg.get("browser", "chrome")
        headless = bool(cfg.get("headless", False))
        timeout = int(cfg.get("timeout", 10))
        # Kept for backward-compat with 2023 code that referenced web_d
        web_d = cfg.get("webdriver", browser)