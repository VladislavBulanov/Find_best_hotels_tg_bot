import os

from dotenv import load_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

load_dotenv()


class SiteSettings(BaseSettings):
    api_key: SecretStr = os.getenv("RAPID_API_KEY")
    host_api: StrictStr = os.getenv("HOST_API")
