class MyAppCriticalError(Exception):
    """MyApp struggle in a critical error."""


class MyAppStartupError(MyAppCriticalError):
    """Error starting up MyApp."""


class MyAppDatabaseError(MyAppCriticalError):
    """MyApp database error."""


class MyAppDependencyError(MyAppCriticalError):
    """Missing dependency error."""


class MyAppOperationalError(Exception):
    """MyApp operation error."""


class MyAppMachineError(MyAppOperationalError):
    """Error managing analysis machine."""



