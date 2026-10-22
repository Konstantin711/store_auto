import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    base_url: str
    admin_email: str
    admin_password: str

    def url(self, path: str) -> str:
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"


def load_settings() -> Settings:
    load_dotenv()

    return Settings(
        base_url=os.getenv("BASE_URL", "http://localhost:3000"),
        admin_email=os.environ["ADMIN_EMAIL"],
        admin_password=os.environ["ADMIN_PASSWORD"],
    )