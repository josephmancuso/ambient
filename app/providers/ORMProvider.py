"""A ORMProvider Service Provider."""

from masonite.providers import ServiceProvider
from masoniteorm.commands import MigrateCommand, MakeMigrationCommand

class ORMProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self):
        """Boots services required by the container."""
        self.commands(
            MigrateCommand(),
            MakeMigrationCommand(),
        )
