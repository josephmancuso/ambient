"""Sound Model."""

from masonite.orm.models import Model
from masonite.orm.scopes.SoftDeletes import SoftDeletes


class Sound(Model, SoftDeletes):
    """Sound Model."""
    pass