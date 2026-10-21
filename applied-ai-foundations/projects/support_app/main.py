from pathlib import Path
import logging
import json
import sys

from message_loader import load_messages

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    filename = sys.argv[1] if len(sys.argv) > 1 else "messages.json"
    try:
        messages = load_messages(Path(filename))
    except FileNotFoundError:
        logger.error("Input file not found: %s", filename)
    except json.JSONDecodeError as exc:
        logger.error(
            "Malformed JSON in %s at line %d, column %d",
            filename,
            exc.lineno,
            exc.colno,
        )
    except ValueError as exc:
        logger.error("Invalid message structure: %s", exc)

    else:
        logger.info("Successfully loaded %d messages", len(messages))


if __name__ == "__main__":
    main()
