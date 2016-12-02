from future.backports.email.quoprimime import body_check
from mongoengine import *
from datetime import datetime
from mongoengine.context_managers import switch_db

class MBookIdentifier(EmbeddedDocument):
    identifier = StringField(max_length=600)
    issn = StringField(max_length=9)
    asin = StringField(max_length=200)
    udc = StringField(max_length=200)
    lbc = StringField(max_length=200)
    ddc = StringField(max_length=45)
    lcc = StringField(max_length=45)
    doi = StringField(max_length=45)
    googlebookid = StringField(max_length=45)
    openlibraryid = StringField(max_length=200)


class MBookChecksum(EmbeddedDocument):
    md5 = StringField(max_length=32)
    crc32 = StringField(max_length=8)
    edonkey = StringField(max_length=32)
    aich = StringField(max_length=32)
    sha1 = StringField(max_length=40)
    tth = StringField(max_length=39)


class MBookMeta(Document):
    bookid = DecimalField(precision=15, required=True, unique=True)
    title = StringField(max_length=2000, required=True)
    volume_info = StringField(max_length=100)
    series = StringField(max_length=300)
    periodical = StringField(max_length=200)
    author = StringField(max_length=1000)
    year = StringField(max_length=14)
    edition = StringField(max_length=60)
    publisher = StringField(max_length=400)
    city = StringField(max_length=100)
    pages = StringField(max_length=100)
    language = StringField(max_length=150)
    topic = StringField(max_length=500)
    library = StringField(max_length=50)
    issue = StringField(max_length=100)
    book_identifiers = EmbeddedDocumentField(MBookIdentifier)
    commentary = StringField(max_length=10000)
    dpi = DecimalField(precision=6)
    color = DecimalField(precision=1, min_value=0, max_value=1, default=0)
    cleaned = DecimalField(precision=1, min_value=0, max_value=1, default=1)
    orientation = DecimalField(precision=1, min_value=0, max_value=1, default=0)
    paginated = DecimalField(precision=1, min_value=0, max_value=1, default=0)
    scanned = DecimalField(precision=1, min_value=0, max_value=1, default=0)
    bookmarked = DecimalField(precision=1, min_value=0, max_value=1, default=0)
    searchable = DecimalField(precision=1, min_value=0, max_value=1, default=1)
    filesize = DecimalField(precision=20, default=0)
    extension = StringField(max_length=50)
    file_checksums = EmbeddedDocumentField(MBookChecksum)
    generic = StringField(max_length=32)
    filename = StringField(max_length=50)
    visible = StringField(max_length=3)
    locator = StringField(max_length=733)
    local = DecimalField(precision=10)
    added_timestamp = DateTimeField(default=datetime.utcnow())
    lastmodified_timestamp = DateTimeField(default=datetime.utcnow())
    cover_url = StringField(max_length=200)
    downloaded = DecimalField(precision=1, min_value=0, max_value=1, default=0)

class MBookStorage(Document):
    storage_bookid = DecimalField(precision=15, required=True, unique=True)
    local_storage = StringField(max_length=1000)
    url_storage = ListField(StringField(max_length=1000))

