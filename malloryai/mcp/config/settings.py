import os
from pathlib import Path
from typing import Any, Dict, Callable

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    APP_ENV: str = Field("local", env="APP_ENV")
    MALLORY_API_KEY: str = Field("", env="MALLORY_API_KEY")
    LOG_LEVEL: str = Field("INFO", env="LOG_LEVEL")
    LOG_DIR: str = Field("logs", env="LOG_DIR")

    class Config:
        # Enable case-sensitive environment variables
        case_sensitive = True
        # Enable environment variables (this ensures direct OS env vars are used)
        env_file_encoding = "utf-8"

        @classmethod
        def customise_sources(
            cls,
            init_settings: Callable[..., Dict[str, Any]],
            env_settings: Callable[..., Dict[str, Any]],
            file_secret_settings: Callable[..., Dict[str, Any]],
        ) -> tuple:
            # Get the project root directory (where .env file is located)
            project_root = Path(__file__).parent.parent.parent.parent
            app_env = os.getenv("APP_ENV", "local")

            # Use absolute paths
            env_file = (
                project_root / f".env.{app_env}"
                if cls.env_file_exists(project_root / f".env.{app_env}")
                else project_root / ".env"
            )
            print(f"Looking for env file at: {env_file}")  # Debug print

            def env_file_source(settings: BaseSettings) -> Dict[str, Any]:
                return cls.env_file_loader(env_file)

            # Order of precedence:
            # 1. Environment variables (highest priority)
            # 2. Environment file values
            # 3. Init settings (default values)
            # 4. File secrets (lowest priority)
            return (
                env_settings,  # First check OS environment variables
                env_file_source,  # Then check .env file variables
                init_settings,  # Then use defaults
                file_secret_settings,
            )

        @staticmethod
        def env_file_exists(file_path: Path) -> bool:
            return file_path.is_file()

        @staticmethod
        def env_file_loader(file_path: Path) -> Dict[str, Any]:
            env_vars = {}
            if file_path.exists():
                print(f"Loading environment variables from: {file_path}")  # Debug print
                with file_path.open() as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            if "=" in line:
                                key, value = line.split("=", 1)
                                env_vars[key.strip()] = (
                                    value.strip().strip('"').strip("'")
                                )
                print(f"Loaded variables: {list(env_vars.keys())}")  # Debug print
            else:
                print(f"ENV file not found at: {file_path}")  # Debug print
            return env_vars
