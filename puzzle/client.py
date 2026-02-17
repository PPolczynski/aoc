import os
import urllib.request
import urllib.error

_base_url = "https://adventofcode.com/{}/day/{}/input"
_file_template = "y{}d{}"
_input_storage_path = "./tmp"

class Client:
    def __init__(self, token: str, refresh: bool = False, path: str = _input_storage_path):
        self._token = token
        self._refresh = refresh
        self._path = path
        
        if not os.path.exists(self._path):
            os.makedirs(self._path)

    def get(self, year: str, day: str) -> str | None:
        filename = _file_template.format(year, day)
        path = os.path.join(self._path, filename)
        
        if not self._refresh and os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                print(f"[Puzzle] Get failed to read file {path}: {e}")
                return None

        print(f"[Puzzle] fetching input for year {year} day {day}...")
        return self._fetch_and_store(path, year, day)

    def _fetch_and_store(self, path: str, year: str, day: str) -> str | None:
        content = self._fetch_input(year, day)
        if content is None:
            return None
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"[Puzzle] Failed to write file {path}: {e}")
            
        return content

    def _fetch_input(self, year: str, day: str) -> str | None:
        if not self._token:
            print(f"[Puzzle] Error: AOC session token is required to fetch input for year {year} day {day}. Provide it via -token, AOC_SESSION_TOKEN env var, or .env file.")
            return None

        url = _base_url.format(year, day)
        req = urllib.request.Request(url)
        req.add_header("Cookie", f"session={self._token}")
        
        try:
            with urllib.request.urlopen(req) as response:
                if response.status != 200:
                    print(f"[Puzzle] Error HTTP status: {response.status}")
                    return None
                return response.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            print(f"[Puzzle] HTTP Error: {e.code} {e.reason}")
            return None
        except Exception as e:
            print(f"[Puzzle] Error making HTTP request: {e}")
            return None
