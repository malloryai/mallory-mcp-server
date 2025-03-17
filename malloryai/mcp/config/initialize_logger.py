import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from . import settings


def initialize_logger():
    """
    Sets up the logging configuration for the Mallory MCP Server.

    - Logs INFO and higher level messages to the console.
    - Logs DEBUG and higher level messages to a rotating file.
    """

    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.handlers = []  # Clear existing handlers

    # Console handler for INFO level and above
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler for DEBUG level and above with rotation
    log_dir = Path(settings.LOG_DIR)
    log_dir.mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(
        filename=log_dir / "mallory_mcp_server.log",
        maxBytes=10**6,
        backupCount=5,  # 1MB
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    logging.debug("Logger initialized successfully.")
