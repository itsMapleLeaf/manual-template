from .lib import world


class TemplateWorldSpec(world.WorldSpec):
    def __init__(self):
        super().__init__(
            game="YourGameName",
            creator="YourName",
            filler_item_name="Useless Filler Item",
        )

        self.define_item("Test Item")
        self.define_location("Test Location")


world_spec = TemplateWorldSpec()
