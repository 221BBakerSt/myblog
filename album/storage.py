from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
import os


class ImageStorage(FileSystemStorage):
    """override _save"""

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # initialisation
        super(ImageStorage, self).__init__(location, base_url)
 
    # name refers to the absolute path of the uploaded file
    def _save(self, name, content):
        # extension name
        extension = os.path.splitext(name)[1]
        # directory name
        directory = os.path.dirname(name)
        # filename without path
        filename = str.replace(os.path.splitext(name)[0], directory, "")
        # hash it and then get the absolute value
        filename = str(abs(hash(filename)))
        # new absolute path of the uploaded file
        name = os.path.join(directory, filename + extension)
        # call parent method
        return super(ImageStorage, self)._save(name, content)
