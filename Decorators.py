import datetime
import time
from functools import wraps 

class Retry:
    def __init__(self, max_attempts=3, delay=1):
        self.max_attempts = max_attempts
        self.delay = delay
    
    def __call__(self, func):
        def wrapper(*args, **kwds):
            attempts = 0
            while attempts < self.max_attempts:
                try:
                    print(datetime.datetime.now().second)
                    return func(*args, **kwds)
                except Exception as e:
                    attempts += 1
                    if attempts >= self.max_attempts:
                        raise e
                    time.sleep(self.delay * (2 ** attempts))
        return wrapper

class Ad:
    def __init__(self) -> None:
        pass
    
    @Retry(max_attempts=4)
    def mock_request(self):
        print('Trying connection...')
        raise ConnectionError
        

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period =  period
        self.calls = []

    def __call__(self, func):
        def wrapper(*args, **kwds):
            now = time.time()
            
            current = 0
            for c in self.calls:
                if now - c < self.period:
                    current += 1
            
            if current >= self.max_calls:
                raise RuntimeError("Rate limit exceeded")
            
            self.calls.append(now)
            return func(*args, **kwds)
        
        return wrapper    
    

class A:
    def __init__(self):
        pass
    
    @RateLimiter(3, 3)
    def mock_get_request(self):
        return 'data'
    
    def fetch_api(self):
        pass
    
a = A()
print(a.mock_get_request())
print(a.mock_get_request())
print(a.mock_get_request())
time.sleep(2)
print(a.mock_get_request())
print(a.mock_get_request())

