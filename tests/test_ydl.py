from ypc import ydl_utils
import pytest


SEARCH_FILE = "tests/test_files/search_terms.txt"
SEARCH_TERM = "xtc - making plans for nigel"
YOUTUBE_FILE = "tests/test_files/youtube_urls.txt"
YOUTUBE_URL = "https://www.youtube.com/watch?v=WfKhVV-7lxI"


def test_ydl_get_url():
    if not isinstance(ydl_utils.ydl_get_url(SEARCH_TERM), str):
        raise AssertionError()
