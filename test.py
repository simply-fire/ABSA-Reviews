from collections import defaultdict

data = [
    {"battery": "positive"},
    {" display": "positive"},
    {"cord length": "negative"},
    {"Key traversal": "negative"},
    {"key traversal": "positive"},
    {" brightness": "positive"},
    {"performance of Processor": "negative"},
    {"battery life": "negative"},
    {"noaspectterm": "none"},
    {"Processor": "positive"},
    {" display": "positive"},
    {"battery": "negative"},
    {" display": "negative"},
    {"battery": "positive"},
    {" processing power": "positive"},
    {" display": "negative"},
    {"cord": "T-NEU"},
    {" battery life": "positive"},
    {" cord": "T-NEU"},
    {" cord": "T-NEU"},
    {"noaspectterm": "none"},
    {"tech guy": "negative"},
    {" service center": "negative"},
    {" sales team": "negative"},
    {" retail shop": "negative"},
    {"noaspectterm": "none"},
    {"GUI": "positive"},
    {" GUI": "positive"},
    {" applications": "positive"},
    {" use": "positive"},
    {" T-POS": "positive"},
    {"start up": "positive"},
    {" T-POS": "positive"},
    {"noaspectterm": "none"},
    {"features": "positive"},
    {" iChat": "positive"},
    {" Photobooth": "positive"},
    {" garage band": "positive"},
    {"=O more": "O"},
    {"noaspectterm": "none"},
    {"features": "positive"},
    {" features": "positive"},
    {" T-POS": "positive"},
    {"noaspectterm": "none"},
    {"GUI": "negative"},
    {" screen": "negative"},
    {" power light": "negative"},
    {" hard drive light": "negative"},
    {" light": "negative"},
    {" flashing": "negative"},
    {"noaspectterm": "none"},
    {"rubber": "T-POS enclosure"},
    {"multi-touch": "positive"},
    {" gestures": "positive"},
    {" tracking area": "positive"},
    {" external mouse": "positive"},
    {" gaming": "T-NEU"},
    {"noaspectterm": "none"},
    {"noaspectterm": "none"},
    {"noaspectterm": "none"},
    {"speed": "positive"},
    {" T-POS": "positive"},
    {"noaspectterm": "none"},
    {"Windows 7": "positive"},
    {"noaspectterm": "none"},
]


def count_sentiment_values(array_of_dicts):
    counts = defaultdict(lambda: {"positive": 0, "negative": 0, "none": 0})

    for dictionary in array_of_dicts:
        for key, value in dictionary.items():
            if value == "positive":
                counts[key]["positive"] += 1
            elif value == "negative":
                counts[key]["negative"] += 1
            elif value == "none":
                counts[key]["none"] += 1
    return counts


print(count_sentiment_values(data))
