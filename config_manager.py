import logging
from typing import Dict, Any
from pathlib import Path
import yaml

logger = logging.getLogger(__name__)

class ConfigurationManager:
    def __init__(self, config_path: str):
        self._config = {}
        
        try:
            with open(config_path) as f:
                self._config = yaml.safe_load(f)
                
            logger.info("Configuration loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load configuration: {str(e)}")
            
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting with optional default."""
        return self._config.get(key, default)
        
    def set_setting(self, key: str, value: Any) -> None:
        """Set a configuration setting."""
        try:
            self._config[key] = value
            logger.info(f"Setting {key} updated to {value}.")
        except Exception as e:
            logger.error(f"Failed to update setting {key}: {str(e)}")