import json
import os


def load_appsetting(environment):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Go up two levels to the project root
    filename = os.path.join(project_root, f"appsetting_{environment.lower()}.json")

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        raise


class UrlProvider:
    try:
        appsetting = load_appsetting('dev')
    except FileNotFoundError:
        print("Failed to load appsetting. Ensure the file exists.")
        raise

    @staticmethod
    def home_page_url() -> str:
        return UrlProvider.appsetting["MainPageUrl"]

    @staticmethod
    def url_builder(url_path: str) -> str:
        return f"{UrlProvider.home_page_url()}{url_path}"

    @staticmethod
    def client_url(client_name) -> str:
        print(UrlProvider.appsetting)
        return UrlProvider.appsetting[client_name]

# Example usage:
# home_url = UrlProvider.home_page_url()
# built_url = UrlProvider.url_builder(UrlPath.AddUser)
# client_url = UrlProvider.client_url(ClientsEnum.Client_1)
