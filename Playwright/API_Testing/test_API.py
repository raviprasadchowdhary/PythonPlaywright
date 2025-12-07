from Playwright.API_Testing.helper import getAuthToken, addToCartZaraCoat3


def test_getAuthToken(playwright):
    print(f"Authentication token is: {getAuthToken(playwright)}")

    assert getAuthToken(playwright) is not None

