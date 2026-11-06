"""MAX messenger platform plugin."""

__all__ = ["register"]


def register(ctx):
    """Register the MAX platform with Hermes.

    The adapter is imported lazily so that loading this package (for example
    while collecting tests) does not require the Hermes gateway modules.
    """
    if __package__:
        from .adapter import register as _register
    else:
        from adapter import register as _register

    return _register(ctx)
