import sys
import pytest
from auto_syspath import __version__

orig_path = sys.path[:]

def test_version():
    assert __version__ == '0.1.0'


def test_cwd():
    import auto_syspath.cwd as _

    import src as _

    with pytest.raises(ModuleNotFoundError):
        import hoge as _
    with pytest.raises(ModuleNotFoundError):
        import huga as _
    with pytest.raises(ModuleNotFoundError):
        import fuga as _
    with pytest.raises(ModuleNotFoundError):
        import huga.fuga as _
    sys.path = orig_path


def test_src():
    import auto_syspath.src as _

    import src as _
    import hoge as _
    import huga as _
    import huga.fuga as _

    with pytest.raises(ModuleNotFoundError):
        import fuga as _
    sys.path = orig_path


def test_poetry():
    import auto_syspath.poetry as _

    import src as _
    import hoge as _
    import huga as _
    with pytest.raises(ModuleNotFoundError):
        import fuga as _
    import huga.fuga as _

    sys.path = orig_path

def test_all():
    import auto_syspath.all as _

    import src as _
    import hoge as _
    import huga as _
    import fuga as _
    import huga.fuga as _

    sys.path = orig_path