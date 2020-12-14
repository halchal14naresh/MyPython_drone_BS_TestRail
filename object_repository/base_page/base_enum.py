import enum


class BaseEnum(enum.Enum):
    # locator variable = (locator, locator_type)

    #Errors
    ERROR_MESSAGE = ("//div[@class='noty_body']", "xpath")
