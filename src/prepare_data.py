from src.models import SpentStat


def prepare_data(data: dict[str, SpentStat]):
    result: list[tuple[str, float]] = []
    for key, val in data.items():
        result.append((key, val.median))
    result.sort(key=lambda item: item[1], reverse=True)
    return result
