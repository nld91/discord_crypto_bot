from typing import Callable, Any, Tuple
from cachetools import TTLCache

CACHE = TTLCache(maxsize=100, ttl=300)

def cache_data(cache_key_prefix: str) -> Callable:
    """
    Decorator function to cache function calls using a TTLCache.

    Parameters:
    cache_key_prefix (str): The prefix to use for caching the function result.

    Returns:
    Callable: The decorated function.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        def wrapper(*args: Tuple[Any, ...], **kwargs: Any) -> Any:
            
            token_symbol = args[0]

            # Check cache for existing data
            cache_key=f"{cache_key_prefix}:{token_symbol}"
            cached_data = CACHE.get(cache_key)

            if cached_data is not None:
                return cached_data

            # Call the decorated function
            result = func(*args, **kwargs)

            # Cache the result
            CACHE[cache_key] = result

            return result
        
        # Add a dynamic docstring to the wrapper function
        wrapper.__doc__ = f"Cached version of {func.__name__} with prefix '{cache_key_prefix}'"

        return wrapper

    return decorator