import pytest
from app.server import ToolRegistry

def test_read_file_works(tmp_path):
    (tmp_path / "hello.txt").write_text("hello")
    registry = ToolRegistry(str(tmp_path))
    assert registry.call("read_file", path="hello.txt") == "hello"

def test_path_traversal_is_blocked(tmp_path):
    registry = ToolRegistry(str(tmp_path))
    with pytest.raises(PermissionError): registry.call("read_file", path="../secret.txt")
    assert registry.audit.events[-1]["allowed"] is False
