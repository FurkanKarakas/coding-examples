"""
Given a list of strings representing time in 24-hour or AM/PM format,
this script uses regular expressions to parse and validate the time strings.
It checks for valid time formats and extracts the hour and minute components.
The script can handle various formats, including "HH:MM", "H:MM AM/PM",
and "HH:MM AM/PM". There can be any number of white characters after the minutes
and before the AM/PM indicator. The script also accounts for leading zeros
in the hour and minute components. Valid time strings are converted to datetime
objects. Datetime and invalid time strings are stored in separate lists
in a Result object.
"""


from datetime import datetime
import re


class Result:
    def __init__(self) -> None:
        self.valid_datetimes: list[datetime] = []
        self.valid_times: list[str] = []
        self.invalid_times: list[str | None] = []

    def add_valid_datetime(self, time_obj: datetime) -> None:
        self.valid_datetimes.append(time_obj)

    def add_valid_time(self, time_str: str) -> None:
        self.valid_times.append(time_str)

    def add_invalid_time(self, time_str: str | None) -> None:
        self.invalid_times.append(time_str)


class TimeReporter:
    def __init__(self, result: Result) -> None:
        self.result = result

    def report(self) -> None:
        """
        Prints the valid and invalid time strings.
        """
        print("Valid Times (Input and Parsed):")
        for time_obj, time_str in zip(self.result.valid_datetimes, self.result.valid_times):
            print(f"Input: {time_str} -> Parsed: {time_obj.strftime('%H:%M')}")

        print("\nInvalid Times:")
        for time_str in self.result.invalid_times:
            print(time_str)


class TimeParser:
    def __init__(self) -> None:
        self.result = Result()
        self.pattern_24_hour = r'^(?:[01]?\d|2[0-3]):(?:[0-5]\d)$'
        self.regex_24_hour = re.compile(self.pattern_24_hour)
        self.pattern_12_hour = r'^(0?[1-9]|1[0-2]):([0-5]\d)\s*(AM|PM)$'
        self.regex_12_hour = re.compile(self.pattern_12_hour, re.IGNORECASE)

    def parse_time_strings(self, time_strings: list[str | None]) -> Result:
        """
        Parses a list of time strings and categorizes them into valid and invalid times.

        Args:
            time_strings (list[str | None]): A list of time strings to be parsed.

        Returns:
            Result: An object containing the parsed valid times and invalid time strings.
        """
        for time_str in time_strings:
            if self.is_valid_time_format(time_str):
                # This assertion is safe because we already checked for None
                assert time_str is not None
                time_obj = self.convert_to_datetime(time_str)
                self.result.add_valid_datetime(time_obj)
                self.result.add_valid_time(time_str)
            else:
                self.result.add_invalid_time(time_str)

        return self.result

    def is_valid_time_format(self, time_str: str | None) -> bool:
        """
        Validates the time string format using regular expressions.

        Args:
            time_str (str | None): The time string to be validated.

        Returns:
            bool: True if the time string is valid, False otherwise.
        """
        if time_str is None:
            return False

        return (
            self.regex_24_hour.match(time_str) is not None or
            self.regex_12_hour.match(time_str) is not None
        )

    def convert_to_datetime(self, time_str: str) -> datetime:
        """
        Converts a valid time string to a datetime object.

        Args:
            time_str (str): A valid time string.

        Returns:
            datetime: A datetime object representing the parsed time.
        """
        match_24_hour = self.regex_24_hour.match(time_str)
        match_12_hour = self.regex_12_hour.match(time_str)
        if match_24_hour:
            return datetime.strptime(time_str, "%H:%M")
        elif match_12_hour:
            hour, minute, period = match_12_hour.groups()
            time_str_formatted = f"{hour}:{minute} {period.upper()}"
            return datetime.strptime(time_str_formatted, "%I:%M %p")
        # This case should not occur if the function is called with a valid time string.
        raise ValueError(f"Invalid time format: {time_str}")


if __name__ == "__main__":
    time_strings = [
        "14:30",
        "2:30PM",
        "02:30 am",
        "02:35 aM",
        "13:35 aM",
        "12:56            aM",
        "12:56            aM AM",
        "12:56            aM AM PM",
        "12:56            aM AM PM  ",
        "25:00",
        "12:60",
        "11:59 PM",
        "00:00",
        "13:15",
        "3:45 AM",
        "00:00 PM",
        "0:19 am",
        None,
        "invalid time"
    ]

    parser = TimeParser()
    result = parser.parse_time_strings(time_strings)

    reporter = TimeReporter(result)
    reporter.report()
