"""CreateSoundsTable Migration."""

from masonite.orm.migrations import Migration


class CreateSoundsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("sounds") as table:
            table.increments('id')
            table.string('name', 63)
            table.string('path')
            table.string('label', 63)
            
            table.timestamps()
            table.timestamp('deleted_at').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("sounds")
