"""MAX messenger platform plugin."""

if __package__:
    from .adapter import register
else:
    from adapter import register

__all__ = ["register"]
