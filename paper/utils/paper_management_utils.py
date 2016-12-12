"""
File contains functions that are used in the management
of the paper files, 

TODO: This will be added in an admin dashboard for the paper management
"""
from paper.models import Paper


def get_storage_size(tag=None, size='mb'):
    """
    Returns the storage size of papers, 
    @param size - this can be 'kb', 'mb', 'gb'
    """
    if size == 'kb':
        return round(get_storage_size_bytes(tag) / 1024.0, 2)
    elif size == 'mb':
        return round(get_storage_size_bytes(tag) / 1024.0 / 1024.0, 2)
    elif size == 'gb':
        return round(get_storage_size_bytes(tag) / 1024.0 / 1024.0 / 1024.0, 2)
    else:
        raise Exception("ERROR: Invalid size parameter")


def get_storage_size_bytes(tag=None):
    """
    Returns the storage size of the papers in bytes.
   
    @param tag - a specific tag to filter based on.
    """
    if tag:
        papers = Paper.objects.filter(tags=tag)
    else:
        papers = Paper.objects.all()

    total_size = 0
    for paper in papers:
        total_size = total_size + paper.paper_file.size

    return total_size
