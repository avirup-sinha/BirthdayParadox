import datetime, random

def GenerateBirthdays() -> list:
    """This program generates birthdays"""
    birthdays = []
    startDate = datetime.date(year=1999, month=1, day=1)
    for i in range(0, 2):
        newDate = startDate + datetime.timedelta(random.randint(0,364))
        birthdays.append(newDate)
    return birthdays


def checkMatchingBirthdays():
    """This function checks for matching birthdays and return how many
    birthdays are matching."""

if __name__ == "__main__":
    print(GenerateBirthdays())