import main
import requests

try:
    if main.artist_id is None:
        print('Please try again')
except RuntimeError:
    print('Please try different keyword search')
finally:
    print('Please try another time. Thank You.')


try:
    if main.track_id is None:
        print('Please try again')
except RuntimeError:
    print('Please try different keyword search')
finally:
    print('Please try another time. Thank You.')


try:
    if main.album_id is None:
        print('Please try again')
except RuntimeError:
    print('Please try different keyword search')
finally:
    print('Please try another time. Thank You.')


def _request(self, url, refresh=False, **params):
    if self.using_cache and refresh is False:
        cache = self._resolve_cache(url, **params)
        if cache is not None:
            return cache
    method = params.get('method', 'GET')
    json_data = params.get('json', {})
    timeout = params.pop('timeout', None) or self.timeout
    if self.is_async:  # return a coroutine
        return self._arequest(url, **params)
    try:
        with self.session.request(
               method, url, timeout=timeout, headers=self.headers, params=params, json=json_data
        ) as resp:
            return self._raise_for_status(resp, resp.text, method=method)
    except requests.Timeout:
        raise TimeoutError
    except requests.ConnectionError:
        raise ConnectionError

