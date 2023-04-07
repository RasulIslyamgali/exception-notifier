from exception_notifier.config import settings


def parse_common_exception_traceback(exception_traceback: list[str]) -> dict[str, str]:
    traceback_ = '\n'.join(exception_traceback)
    return {
        'traceback': traceback_,
    }


def format_traceback(exception_traceback: list[str]):
    exclamation_mark_emoji = b'\xE2\x9D\x97'.decode('utf-8')

    parsed_traceback = parse_common_exception_traceback(exception_traceback)
    parsed_traceback.update({'service_name': settings.SERVICE_NAME})

    parsed_traceback["traceback"] = parsed_traceback["traceback"].replace('_', r'\_')

    formatted_traceback_message = f'{exclamation_mark_emoji * 3}Exception Notifier{exclamation_mark_emoji * 3}\n\n' \
                                  f'Service: *{parsed_traceback["service_name"]}* \n\n' \
                                  f'{parsed_traceback["traceback"]}'

    return formatted_traceback_message
