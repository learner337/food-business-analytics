def date_separator(text):
    """
    takes a string input and separates the date and time
    :param text:
    :return:
    """
    # date = ""
    # time = ""
    # TODO: write

    text = str(text)
    date = text[0:10]
    time = text[11:19]
    return date, time
