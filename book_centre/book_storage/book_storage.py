from mongoengine import *
from datetime import datetime

class BookIdentifier(Document):
    identifier = StringField(max_length=600)
    issn = StringField(max_length=9)
    asin = StringField(max_length=200)
    udc = StringField(max_length=200)
    lbc = StringField(max_length=200)
    ddc = StringField(max_length=45)
    lcc = StringField(max_length=45)
    doi = StringField(max_length=45)
    google_book_id  = StringField(max_length=45)
    open_library_id = StringField(max_length=200)


class BookFileCheck(Document):
    md5 = StringField(max_length=32)
    crc32 = StringField(max_length=8)
    edonkey = StringField(max_length=32)
    aich = StringField(max_length=32)
    sha1 = StringField(max_length=40)
    tth = StringField(max_length=39)


class BookMeta(Document):
    bookid = DecimalField(precision=15, required=True, unique= True, primary_key=True)
    title = StringField(max_length=2000, required=True)
    volumeinfo = StringField(max_length=100)
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
    identifier = EmbeddedDocumentField(BookIdentifier)
    commentary = StringField(max_length=10000)
    dpi = DecimalField(precision=6)
    color = BooleanField(default=False)
    cleaned = BooleanField(default=True)
    orientation = DecimalField(default=1)
    paginated = BooleanField(default=True)
    scanned = BooleanField(default=False)
    bookmarked = BooleanField(default=False)
    searchable = BooleanField(default=True)
    filesize = DecimalField(precision=20, default=0)
    extension = StringField(max_length=50)
    filecheck = EmbeddedDocumentField(BookFileCheck)
    generic = StringField(max_length=32)
    filename = StringField(max_length=50)
    visible = StringField(max_length=3)
    locator = StringField(max_length=733)
    local = DecimalField(precision=10)
    timeadded = DateTimeField(default=datetime.utcnow(), required=True)
    timelastmodified = DateTimeField(default=datetime.utcnow())
    coverurl = StringField(max_length=200)


class BookStorage(Document):
    bookid = DecimalField(precision=15, required=True)
    url = StringField(max_length=200, required=True)
