from datetime import datetime, timezone
from pathlib import Path

from icalendar import Calendar, Event


def main():
    cal = Calendar()
    cal.add("prodid", "test-calendar/test")
    cal.add("version", "2.0")
    nye = Event()
    nye.uid = "nye-test@test-calendar/test"
    nye.DTSTAMP = datetime.now().astimezone()
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
