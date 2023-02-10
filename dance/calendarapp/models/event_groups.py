from django.db import models

from danceschool.models import Commands
from calendarapp.models import Event, EventAbstract


class EventGroups(EventAbstract):
    """ Event groups model """

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events_group")
    command = models.ForeignKey(
        Commands, on_delete=models.CASCADE, related_name="event_groups"
    )

    class Meta:
        unique_together = ["event", "command"]

    def __str__(self):
        return str(self.command)
