from datetime import date
from typing import Dict
from dataclasses import dataclass
from typing import List
from datetime import datetime
from pycountry import countries, languages
from pycountry.db import Country


@dataclass
class Author:
    name: str
    birth_date: date
    country: Country
    languages: List[str]

    def __post_init__(self) -> None:
        if self.birth_date.__class__ == str:
            self.birth_date = (
                datetime.fromisoformat(self.birth_date).date()
                if self.birth_date
                else None
            )
        if self.country:
            try:
                if len(self.country) == 2:
                    self.country = countries.get(alpha_2=self.country)
                elif len(self.country) == 3:
                    self.country = countries.get(alpha_3=self.country)
            except LookupError:
                self.country = None
        if self.languages:
            self.languages = [
                languages.get(name=language.lower()) for language in self.languages
            ]

    @property
    def first_name(self) -> str:
        return self.name.split(" ")[0]

    def __eq__(self, __value: "Author") -> bool:
        if self.__class__ != __value.__class__:
            return False
        return self.name == __value.name and self.birth_date == __value.birth_date

    @property
    def as_dict(self) -> Dict:
        return {
            "name": self.name,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None,
            "country": self.country.alpha_3 if self.country else None,
            "languages": [lang.name for lang in self.languages],
        }

    @property
    def to_representation(self) -> Dict:
        return {
            "name": self.name,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None,
            "country": {
                "name": self.country.name,
                "alpha_3": self.country.alpha_3,
                "flag": self.country.flag,
            }
            if self.country
            else None,
            "languages": [lang.name for lang in self.languages]
            if self.languages
            else None,
        }
