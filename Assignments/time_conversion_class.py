# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Object Oriented Programming - Classes & Methods
# File    : time_conversion_class.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - Time Conversion Class
#
# Create a Time class that converts a value in seconds to various formats.
#
#   __init__(self, time: int)
#       Initialise with total time in seconds.
#
#   seconds_to_minutes(self) -> str
#       Convert to minutes and seconds.
#       e.g. 170 → "2 min 50 sec"
#
#   seconds_to_hours(self) -> str
#       Convert to hours, minutes, and seconds.
#       e.g. 10890 → "3 hrs 1 min 30 sec"
#
#   seconds_to_days(self) -> str
#       Convert to days, hours, minutes, and seconds.
#       e.g. 86460 → "1 days 0 hrs 1 min 0 sec"
# -----------------------------------------------------------------------------


class Time:
    """A class to represent time and convert it from seconds to different formats."""

    def __init__(self, time: int):
        """Initialise with total time in seconds."""
        self.time = time

    def seconds_to_minutes(self) -> str:
        """Convert total seconds to minutes and seconds."""
        minutes = self.time // 60
        seconds = self.time % 60
        return f"{minutes} min {seconds} sec"

    def seconds_to_hours(self) -> str:
        """Convert total seconds to hours, minutes, and seconds."""
        hours             = self.time // 3600
        remaining_seconds = self.time % 3600
        minutes           = remaining_seconds // 60
        seconds           = remaining_seconds % 60
        return f"{hours} hrs {minutes} min {seconds} sec"

    def seconds_to_days(self) -> str:
        """Convert total seconds to days, hours, minutes, and seconds."""
        days                          = self.time // 86400
        remaining_seconds_after_days  = self.time % 86400
        hours                         = remaining_seconds_after_days // 3600
        remaining_seconds_after_hours = remaining_seconds_after_days % 3600
        minutes                       = remaining_seconds_after_hours // 60
        seconds                       = remaining_seconds_after_hours % 60
        return f"{days} days {hours} hrs {minutes} min {seconds} sec"


# --- driver code ---
if __name__ == "__main__":
    t    = int(input("enter time in seconds: "))
    time = Time(t)

    print("seconds_to_minutes :", time.seconds_to_minutes())
    print("seconds_to_hours   :", time.seconds_to_hours())
    print("seconds_to_days    :", time.seconds_to_days())