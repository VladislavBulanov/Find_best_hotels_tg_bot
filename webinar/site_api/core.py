from settings import SiteSettings
from site_api.utils.site_api_handler import SiteApiInterface

site = SiteSettings()
url = "https://" + site.host_api
headers = {
    "X-RapidAPI-Key": site.api_key.get_secret_value(),
    "X-RapidAPI-Host": site.host_api,
}
params = {"json": "true", "fragment": "true"}

siteapi = SiteApiInterface


if __name__ == "__main__":
    siteapi()
