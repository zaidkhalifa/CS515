import time

class TimerError(Exception):
    """Custom exception for Timer class errors."""
    pass

class Timer:
    """A Timer class for measuring elapsed time.
    
    >>> t = Timer()
    >>> t.start()
    >>> t.start()  # doctest:
    Traceback (most recent call last):
    timer.TimerError: timer is already running
    
    >>> t2 = Timer()
    >>> t2.stop()  # doctest:
    Traceback (most recent call last):
    timer.TimerError: timer is not running
    
    >>> t3 = Timer()
    >>> t3.start()
    >>> from time import sleep
    >>> sleep(0.1)
    >>> t3.stop()
    >>> total = t3.total()
    >>> 0.005 <= total <= 0.105
    True
    
    >>> t3.reset()
    >>> t3.total()
    0.0
    """
    def __init__(self):
        self._start_time = None
        self._total_time = 0.0
        self._running = False

    def start(self):
        if self._running:
            raise TimerError("timer is already running")
        self._start_time = time.time()
        self._running = True

    def stop(self):
        if not self._running:
            raise TimerError("timer is not running")
        self._total_time += time.time() - self._start_time
        self._running = False

    def reset(self):
        self._total_time = 0.0

    def total(self):
        if self._running:
            return self._total_time + (time.time() - self._start_time)
        return self._total_time

if __name__ == "__main__":
    import doctest
    doctest.testmod()