class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = map(int, date.split('.'))
        creation_month = cls.get_month_name(month)
        return cls(name, id, year, creation_month, age_restriction)

    @staticmethod
    def get_month_name(month: int) -> str:
        months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        return months.get(month, "Unknown")

    def __repr__(self) -> str:
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "\
               f"has age restriction {self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"
