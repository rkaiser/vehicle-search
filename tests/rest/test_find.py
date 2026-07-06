from vehicle_search.rest.find import find_vehicle


class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {
            "results": [
                {"make": "honda", "year": 2020}
            ]
        }


def test_find_vehicle_calls_requests(monkeypatch):
    calls = []

    def fake_get(url, params=None, timeout=None):
        calls.append({
            "url": url,
            "params": params,
            "timeout": timeout,
        })
        return FakeResponse()

    monkeypatch.setattr("vehicle_search.rest.find.requests.get", fake_get)

    find_vehicle("honda", 2020,  "https://carapi.app/api/models/v2")
    assert calls == [
        {
            "url": "https://carapi.app/api/models/v2?make=honda&year=2020&page=1",
            "params": None,
            "timeout": None,
        }
    ]