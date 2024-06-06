import json
import requests
import pytest

# Function to fetch Lambda URL from the provided API
def get_lambda_url():
    api_url = "https://kxealgo7y6ufpghixbqxt5m5lm0zlrqe.lambda-url.us-east-1.on.aws/"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        raise ValueError(f"Failed to fetch Lambda URL. Status code: {response.status_code}")

@pytest.fixture
def lambda_url():
    return get_lambda_url()

def test_lambda_function(lambda_url):
    event = {"key": "value"}

    # Send a POST request to the Lambda function
    response = requests.post(lambda_url, data=json.dumps(event))

    # Check if the request was successful (status code 200)
    assert response.status_code == 200

    try:
        result = response.json()
        if isinstance(result, int):
            result = {"views": result}
        assert "views" in result
        assert isinstance(result["views"], int)

    except json.JSONDecodeError:
        # Handle the case where the response is not a valid JSON
        pytest.fail("Response is not a valid JSON")

if __name__ == "__main__":
    pytest.main()