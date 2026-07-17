from app.utils.hash_utils import generate_hash


def test_same_content_same_hash():
    text = "Blood pressure monitor"

    assert generate_hash(text) == generate_hash(text)


def test_different_content_different_hash():
    hash1 = generate_hash("Version 1")
    hash2 = generate_hash("Version 2")

    assert hash1 != hash2