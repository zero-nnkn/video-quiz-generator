from typing import Literal

from pydantic import BaseModel


class ServiceInfo(BaseModel):
    """
    LLM Service Info class, including service name and API Key or Cookie.
    """

    service: Literal['GoogleBard', 'OpenAIGPT']
    service_key: str
