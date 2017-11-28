class EventSourcingError(Exception):
    """Base eventsourcing exception."""


class TopicResolutionError(EventSourcingError):
    """Raised when unable to resolve a topic to a Python class."""


class EntityVersionNotFound(EventSourcingError):
    """Raise when accessing an entity version that does not exist."""


class ConcurrencyError(EventSourcingError):
    """Raised when appending events at the wrong version to a versioned stream."""


class ConsistencyError(EventSourcingError):
    """Raised when applying an event stream to a versioned entity."""


class MismatchedOriginatorError(ConsistencyError):
    """Raised when applying an event to an inappropriate object."""


class MismatchedOriginatorIDError(MismatchedOriginatorError):
    """Raised when applying an event to the wrong entity or aggregate."""


class MismatchedOriginatorVersionError(MismatchedOriginatorError):
    """Raised when applying an event to the wrong version of an entity or aggregate."""


class MutatorRequiresTypeNotInstance(ConsistencyError):
    """Raised when mutator function received a class rather than an entity."""


class DataIntegrityError(EventSourcingError):
    "Raised when a sequenced item data is damaged (hash doesn't match data)"


class SealHashMismatch(DataIntegrityError):
    "Raised when an event's seal hash doesn't match the hash of the state of the event."


class MismatchedLastHashError(DataIntegrityError, MismatchedOriginatorError):
    """Raised when applying an event with last hash different to aggregate head hash."""


class EntityIsDiscarded(AssertionError):
    """Raised when access to a recently discarded entity object is attempted."""


class ProgrammingError(EventSourcingError):
    """Raised when programming errors are encountered."""


class RepositoryKeyError(KeyError, EventSourcingError):
    """Raised when using entity repository's dictionary like interface  to get an entity that does not exist."""


class ArrayIndexError(IndexError, EventSourcingError):
    """Raised when appending item to an array that is full."""


class DatasourceSettingsError(EventSourcingError):
    "Raised when an error is detected in settings for a datasource."


class SequencedItemConflict(EventSourcingError):
    "Raised when an integer sequence error occurs e.g. trying to save a version that already exists."


class TimeSequenceError(EventSourcingError):
    "Raised when a time sequence error occurs e.g. trying to save a timestamp that already exists."
