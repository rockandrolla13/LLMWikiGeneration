"""Time source for LLM Wiki.

The stdlib's naive UTC constructor is deprecated from Python 3.12. Its obvious
replacement, ``datetime.now(timezone.utc)``, returns a timezone-AWARE value
whose ``isoformat()`` ends in "+00:00". Every timestamp in this codebase is
serialised as ``value.isoformat() + "Z"``, so swapping in the aware version
would emit "...+00:00Z" and corrupt every date written to a wiki page.

``utc_now()`` returns a naive datetime holding UTC -- identical to what the
deprecated constructor produced -- so behaviour and on-disk format are
unchanged.
"""

from datetime import datetime, timezone


def utc_now() -> datetime:
    """Return the current UTC time as a naive datetime.

    Returns:
        Current UTC time with tzinfo stripped, matching the legacy contract.
    """
    return datetime.now(timezone.utc).replace(tzinfo=None)
