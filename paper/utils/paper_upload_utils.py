from paper.models import Tag


def get_tags_from_string(tags_string):
    """
    Returns tags got from a tag string instance,
    it creates tag instances for tags that do not exist
    """
    tags = []
    tags_string_list = tags_string.split(',')
 
    for tag_string in tags_string_list:
        tag_string =  tag_string.strip()
        tag = Tag.objects.filter(name=tag_string)

        if tag:
            tags.append(tag)
        else:
            tag = Tag.objects.create(name=tag_string)
            tags.append(tag)

    return tags
