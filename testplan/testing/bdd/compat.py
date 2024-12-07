"""Compatibility layer for gherkin package."""
import io
import os

from gherkin.token_scanner import TokenScanner as BaseTokenScanner


class CompatibleTokenScanner(BaseTokenScanner):
    """
    A compatible wrapper for gherkin's TokenScanner that fixes file mode deprecation.

    This wrapper uses 'r' mode instead of the deprecated 'rU' mode while maintaining
    the same functionality as the original TokenScanner.
    """
    def __init__(self, path_or_str):
        # Initialize base class first to set up all necessary attributes
        super().__init__("")  # Initialize with empty string, we'll set io properly below

        if isinstance(path_or_str, str) and os.path.exists(path_or_str):
            # Use 'r' mode instead of 'rU' for file paths
            self.io = io.open(path_or_str, 'r', encoding='utf8')
        else:
            # For string content, use StringIO as in the original
            self.io = io.StringIO(path_or_str)

        # Reset line number as we're starting fresh
        self.line_number = 0
