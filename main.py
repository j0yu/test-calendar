from datetime import datetime, timezone
from pathlib import Path

from icalendar import Calendar, Event


def main():
    cal = Calendar()
    nye = Event()
    nye.DTSTART = datetime(
        2025, 12, 31, hour=0, minute=0, second=0, tzinfo=timezone.utc
    )
    nye.DTEND = datetime(
        2025, 12, 31, hour=23, minute=59, second=59, tzinfo=timezone.utc
    )
    cal.add_component(nye)
    Path("test.ics").write_bytes(cal.to_ical())


if __name__ == "__main__":
    main()
