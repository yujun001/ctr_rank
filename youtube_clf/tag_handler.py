import json


def get_category_title_dict(json_path):
    """ Returns a dictionary with category_id
     as keys and category title as value."""

    dict = {}
    with open(json_path) as json_file:
        data = json.load(json_file)
        for item in data['items']:
            dict.update({item['id']: item['snippet']['title']})

    return dict


def get_clean_tags(tags):
    """ Given tags column of dataframe,
     normalizes tags by removing double quotation."""

    normalized_tags = []
    final_tags = []
    i = 0
    for tag in tags:
        normalized_tags.append(tag.split("|"))
        final_tags.append([])

    for tag in normalized_tags:
        for word in tag:
            if '"' in word:
                word = word.replace('"', '')
            final_tags[i].append(word)
        i += 1
    return final_tags


