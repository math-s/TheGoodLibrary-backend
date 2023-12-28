from app.domain.authors.manager import AuthorManager

AUTHORS = [
    {
        "name": "Matheus A",
        "country": "BRA",
        "languages": ["Portuguese", "Latin"],
        "birth_date": "2000-01-01",
        "death_date": None
    },
    {
        "name": "Emily B",
        "country": "USA",
        "languages": ["English", "Latin"],
        "birth_date": "1985-05-12",
        "death_date": None
    },
    {
        "name": "Juan C",
        "country": "MEX",
        "languages": ["Spanish", "Latin"],
        "birth_date": "1978-09-23",
        "death_date": None
    },
    {
        "name": "Sophie D",
        "country": "FRA",
        "languages": ["French", "Latin"],
        "birth_date": "1992-03-15",
        "death_date": None
    },
    {
        "name": "Akio E",
        "country": "JPN",
        "languages": ["Japanese", "Latin"],
        "birth_date": "1980-11-07",
        "death_date": None
    },
    {
        "name": "Elena F",
        "country": None,
        "languages": ["Italian", "Latin"],
        "birth_date": "1972-08-29",
        "death_date": None
    },
    {
        "name": "Ravi G",
        "country": "IND",
        "languages": ["Hindi", "Latin"],
        "birth_date": "1989-06-18",
        "death_date": None
    },
    {
        "name": "Luisa H",
        "country": "ESP",
        "languages": ["Spanish"],
        "birth_date": "1983-12-04",
        "death_date": None
    },
    {
        "name": "Khaled I",
        "country": "EGY",
        "languages": [],
        "birth_date": "1975-04-26",
        "death_date": None
    },
    {
        "name": "Yuki J",
        "country": "JPN",
        "languages": ["Japanese", "Latin"],
        "birth_date": "1995-10-10",
        "death_date": None
    }
]


if __name__ == "__main__":

    for row in AUTHORS:
        AuthorManager.create_author(**row)
