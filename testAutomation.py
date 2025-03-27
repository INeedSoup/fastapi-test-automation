import requests

testcases = [
    ("http://localhost:8000/add/2/2", 4, "Test addition of 2 and 2"),
]

def test_api():
    for url, expected, description in testcases:
        response = requests.get(url)
        result = response.json()["result"]
        assert result == expected, f"{description}. Expected {expected}, got {result}"
        print(f"✅ {description} passed.")

if __name__ == "__main__":
    test_api()
