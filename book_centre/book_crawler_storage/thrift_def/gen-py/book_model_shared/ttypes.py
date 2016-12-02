#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class TBookIdentifier:
  """
  Attributes:
   - identifier
   - issn
   - asin
   - udc
   - lbc
   - ddc
   - lcc
   - doi
   - google_book_id
   - open_library_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'identifier', None, None, ), # 1
    (2, TType.STRING, 'issn', None, None, ), # 2
    (3, TType.STRING, 'asin', None, None, ), # 3
    (4, TType.STRING, 'udc', None, None, ), # 4
    (5, TType.STRING, 'lbc', None, None, ), # 5
    (6, TType.STRING, 'ddc', None, None, ), # 6
    (7, TType.STRING, 'lcc', None, None, ), # 7
    (8, TType.STRING, 'doi', None, None, ), # 8
    (9, TType.STRING, 'google_book_id', None, None, ), # 9
    (10, TType.STRING, 'open_library_id', None, None, ), # 10
  )

  def __init__(self, identifier=None, issn=None, asin=None, udc=None, lbc=None, ddc=None, lcc=None, doi=None, google_book_id=None, open_library_id=None,):
    self.identifier = identifier
    self.issn = issn
    self.asin = asin
    self.udc = udc
    self.lbc = lbc
    self.ddc = ddc
    self.lcc = lcc
    self.doi = doi
    self.google_book_id = google_book_id
    self.open_library_id = open_library_id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.identifier = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.issn = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.asin = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.udc = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.lbc = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.ddc = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.lcc = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.doi = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.google_book_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.open_library_id = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TBookIdentifier')
    if self.identifier is not None:
      oprot.writeFieldBegin('identifier', TType.STRING, 1)
      oprot.writeString(self.identifier)
      oprot.writeFieldEnd()
    if self.issn is not None:
      oprot.writeFieldBegin('issn', TType.STRING, 2)
      oprot.writeString(self.issn)
      oprot.writeFieldEnd()
    if self.asin is not None:
      oprot.writeFieldBegin('asin', TType.STRING, 3)
      oprot.writeString(self.asin)
      oprot.writeFieldEnd()
    if self.udc is not None:
      oprot.writeFieldBegin('udc', TType.STRING, 4)
      oprot.writeString(self.udc)
      oprot.writeFieldEnd()
    if self.lbc is not None:
      oprot.writeFieldBegin('lbc', TType.STRING, 5)
      oprot.writeString(self.lbc)
      oprot.writeFieldEnd()
    if self.ddc is not None:
      oprot.writeFieldBegin('ddc', TType.STRING, 6)
      oprot.writeString(self.ddc)
      oprot.writeFieldEnd()
    if self.lcc is not None:
      oprot.writeFieldBegin('lcc', TType.STRING, 7)
      oprot.writeString(self.lcc)
      oprot.writeFieldEnd()
    if self.doi is not None:
      oprot.writeFieldBegin('doi', TType.STRING, 8)
      oprot.writeString(self.doi)
      oprot.writeFieldEnd()
    if self.google_book_id is not None:
      oprot.writeFieldBegin('google_book_id', TType.STRING, 9)
      oprot.writeString(self.google_book_id)
      oprot.writeFieldEnd()
    if self.open_library_id is not None:
      oprot.writeFieldBegin('open_library_id', TType.STRING, 10)
      oprot.writeString(self.open_library_id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TBookChecksum:
  """
  Attributes:
   - md5
   - crc32
   - edonkey
   - aich
   - sha1
   - tth
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'md5', None, None, ), # 1
    (2, TType.STRING, 'crc32', None, None, ), # 2
    (3, TType.STRING, 'edonkey', None, None, ), # 3
    (4, TType.STRING, 'aich', None, None, ), # 4
    (5, TType.STRING, 'sha1', None, None, ), # 5
    (6, TType.STRING, 'tth', None, None, ), # 6
  )

  def __init__(self, md5=None, crc32=None, edonkey=None, aich=None, sha1=None, tth=None,):
    self.md5 = md5
    self.crc32 = crc32
    self.edonkey = edonkey
    self.aich = aich
    self.sha1 = sha1
    self.tth = tth

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.md5 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.crc32 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.edonkey = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.aich = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.sha1 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.tth = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TBookChecksum')
    if self.md5 is not None:
      oprot.writeFieldBegin('md5', TType.STRING, 1)
      oprot.writeString(self.md5)
      oprot.writeFieldEnd()
    if self.crc32 is not None:
      oprot.writeFieldBegin('crc32', TType.STRING, 2)
      oprot.writeString(self.crc32)
      oprot.writeFieldEnd()
    if self.edonkey is not None:
      oprot.writeFieldBegin('edonkey', TType.STRING, 3)
      oprot.writeString(self.edonkey)
      oprot.writeFieldEnd()
    if self.aich is not None:
      oprot.writeFieldBegin('aich', TType.STRING, 4)
      oprot.writeString(self.aich)
      oprot.writeFieldEnd()
    if self.sha1 is not None:
      oprot.writeFieldBegin('sha1', TType.STRING, 5)
      oprot.writeString(self.sha1)
      oprot.writeFieldEnd()
    if self.tth is not None:
      oprot.writeFieldBegin('tth', TType.STRING, 6)
      oprot.writeString(self.tth)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TBookMeta:
  """
  Attributes:
   - bookid
   - title
   - volume_info
   - series
   - periodical
   - author
   - year
   - edition
   - publisher
   - city
   - pages
   - language
   - topic
   - library
   - issue
   - book_identifiers
   - commentary
   - dpi
   - color
   - cleaned
   - orientation
   - paginated
   - scanned
   - bookmarked
   - searchable
   - filesize
   - extension
   - file_checksums
   - generic
   - filename
   - visible
   - locator
   - local
   - added_timestamp
   - lastmodified_timestamp
   - cover_url
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'bookid', None, None, ), # 1
    (2, TType.STRING, 'title', None, None, ), # 2
    (3, TType.STRING, 'volume_info', None, None, ), # 3
    (4, TType.STRING, 'series', None, None, ), # 4
    (5, TType.STRING, 'periodical', None, None, ), # 5
    (6, TType.STRING, 'author', None, None, ), # 6
    (7, TType.STRING, 'year', None, None, ), # 7
    (8, TType.STRING, 'edition', None, None, ), # 8
    (9, TType.STRING, 'publisher', None, None, ), # 9
    (10, TType.STRING, 'city', None, None, ), # 10
    (11, TType.I64, 'pages', None, None, ), # 11
    (12, TType.STRING, 'language', None, None, ), # 12
    (13, TType.STRING, 'topic', None, None, ), # 13
    (14, TType.STRING, 'library', None, None, ), # 14
    (15, TType.STRING, 'issue', None, None, ), # 15
    (16, TType.STRUCT, 'book_identifiers', (TBookIdentifier, TBookIdentifier.thrift_spec), None, ), # 16
    (17, TType.STRING, 'commentary', None, None, ), # 17
    (18, TType.I32, 'dpi', None, None, ), # 18
    (19, TType.BOOL, 'color', None, None, ), # 19
    (20, TType.BOOL, 'cleaned', None, None, ), # 20
    (21, TType.BOOL, 'orientation', None, None, ), # 21
    (22, TType.BOOL, 'paginated', None, None, ), # 22
    (23, TType.BOOL, 'scanned', None, None, ), # 23
    (24, TType.BOOL, 'bookmarked', None, None, ), # 24
    (25, TType.BOOL, 'searchable', None, None, ), # 25
    (26, TType.I64, 'filesize', None, None, ), # 26
    (27, TType.STRING, 'extension', None, None, ), # 27
    (28, TType.STRUCT, 'file_checksums', (TBookChecksum, TBookChecksum.thrift_spec), None, ), # 28
    (29, TType.STRING, 'generic', None, None, ), # 29
    (30, TType.STRING, 'filename', None, None, ), # 30
    (31, TType.STRING, 'visible', None, None, ), # 31
    (32, TType.STRING, 'locator', None, None, ), # 32
    (33, TType.I32, 'local', None, None, ), # 33
    (34, TType.I64, 'added_timestamp', None, None, ), # 34
    (35, TType.I64, 'lastmodified_timestamp', None, None, ), # 35
    (36, TType.STRING, 'cover_url', None, None, ), # 36
  )

  def __init__(self, bookid=None, title=None, volume_info=None, series=None, periodical=None, author=None, year=None, edition=None, publisher=None, city=None, pages=None, language=None, topic=None, library=None, issue=None, book_identifiers=None, commentary=None, dpi=None, color=None, cleaned=None, orientation=None, paginated=None, scanned=None, bookmarked=None, searchable=None, filesize=None, extension=None, file_checksums=None, generic=None, filename=None, visible=None, locator=None, local=None, added_timestamp=None, lastmodified_timestamp=None, cover_url=None,):
    self.bookid = bookid
    self.title = title
    self.volume_info = volume_info
    self.series = series
    self.periodical = periodical
    self.author = author
    self.year = year
    self.edition = edition
    self.publisher = publisher
    self.city = city
    self.pages = pages
    self.language = language
    self.topic = topic
    self.library = library
    self.issue = issue
    self.book_identifiers = book_identifiers
    self.commentary = commentary
    self.dpi = dpi
    self.color = color
    self.cleaned = cleaned
    self.orientation = orientation
    self.paginated = paginated
    self.scanned = scanned
    self.bookmarked = bookmarked
    self.searchable = searchable
    self.filesize = filesize
    self.extension = extension
    self.file_checksums = file_checksums
    self.generic = generic
    self.filename = filename
    self.visible = visible
    self.locator = locator
    self.local = local
    self.added_timestamp = added_timestamp
    self.lastmodified_timestamp = lastmodified_timestamp
    self.cover_url = cover_url

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.bookid = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.title = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.volume_info = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.series = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.periodical = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.author = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.year = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.edition = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.publisher = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.city = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I64:
          self.pages = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.STRING:
          self.language = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.STRING:
          self.topic = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.STRING:
          self.library = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.STRING:
          self.issue = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 16:
        if ftype == TType.STRUCT:
          self.book_identifiers = TBookIdentifier()
          self.book_identifiers.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 17:
        if ftype == TType.STRING:
          self.commentary = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 18:
        if ftype == TType.I32:
          self.dpi = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 19:
        if ftype == TType.BOOL:
          self.color = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 20:
        if ftype == TType.BOOL:
          self.cleaned = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 21:
        if ftype == TType.BOOL:
          self.orientation = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 22:
        if ftype == TType.BOOL:
          self.paginated = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 23:
        if ftype == TType.BOOL:
          self.scanned = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 24:
        if ftype == TType.BOOL:
          self.bookmarked = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 25:
        if ftype == TType.BOOL:
          self.searchable = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 26:
        if ftype == TType.I64:
          self.filesize = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 27:
        if ftype == TType.STRING:
          self.extension = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 28:
        if ftype == TType.STRUCT:
          self.file_checksums = TBookChecksum()
          self.file_checksums.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 29:
        if ftype == TType.STRING:
          self.generic = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 30:
        if ftype == TType.STRING:
          self.filename = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 31:
        if ftype == TType.STRING:
          self.visible = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 32:
        if ftype == TType.STRING:
          self.locator = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 33:
        if ftype == TType.I32:
          self.local = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 34:
        if ftype == TType.I64:
          self.added_timestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 35:
        if ftype == TType.I64:
          self.lastmodified_timestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 36:
        if ftype == TType.STRING:
          self.cover_url = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TBookMeta')
    if self.bookid is not None:
      oprot.writeFieldBegin('bookid', TType.I64, 1)
      oprot.writeI64(self.bookid)
      oprot.writeFieldEnd()
    if self.title is not None:
      oprot.writeFieldBegin('title', TType.STRING, 2)
      oprot.writeString(self.title)
      oprot.writeFieldEnd()
    if self.volume_info is not None:
      oprot.writeFieldBegin('volume_info', TType.STRING, 3)
      oprot.writeString(self.volume_info)
      oprot.writeFieldEnd()
    if self.series is not None:
      oprot.writeFieldBegin('series', TType.STRING, 4)
      oprot.writeString(self.series)
      oprot.writeFieldEnd()
    if self.periodical is not None:
      oprot.writeFieldBegin('periodical', TType.STRING, 5)
      oprot.writeString(self.periodical)
      oprot.writeFieldEnd()
    if self.author is not None:
      oprot.writeFieldBegin('author', TType.STRING, 6)
      oprot.writeString(self.author)
      oprot.writeFieldEnd()
    if self.year is not None:
      oprot.writeFieldBegin('year', TType.STRING, 7)
      oprot.writeString(self.year)
      oprot.writeFieldEnd()
    if self.edition is not None:
      oprot.writeFieldBegin('edition', TType.STRING, 8)
      oprot.writeString(self.edition)
      oprot.writeFieldEnd()
    if self.publisher is not None:
      oprot.writeFieldBegin('publisher', TType.STRING, 9)
      oprot.writeString(self.publisher)
      oprot.writeFieldEnd()
    if self.city is not None:
      oprot.writeFieldBegin('city', TType.STRING, 10)
      oprot.writeString(self.city)
      oprot.writeFieldEnd()
    if self.pages is not None:
      oprot.writeFieldBegin('pages', TType.I64, 11)
      oprot.writeI64(self.pages)
      oprot.writeFieldEnd()
    if self.language is not None:
      oprot.writeFieldBegin('language', TType.STRING, 12)
      oprot.writeString(self.language)
      oprot.writeFieldEnd()
    if self.topic is not None:
      oprot.writeFieldBegin('topic', TType.STRING, 13)
      oprot.writeString(self.topic)
      oprot.writeFieldEnd()
    if self.library is not None:
      oprot.writeFieldBegin('library', TType.STRING, 14)
      oprot.writeString(self.library)
      oprot.writeFieldEnd()
    if self.issue is not None:
      oprot.writeFieldBegin('issue', TType.STRING, 15)
      oprot.writeString(self.issue)
      oprot.writeFieldEnd()
    if self.book_identifiers is not None:
      oprot.writeFieldBegin('book_identifiers', TType.STRUCT, 16)
      self.book_identifiers.write(oprot)
      oprot.writeFieldEnd()
    if self.commentary is not None:
      oprot.writeFieldBegin('commentary', TType.STRING, 17)
      oprot.writeString(self.commentary)
      oprot.writeFieldEnd()
    if self.dpi is not None:
      oprot.writeFieldBegin('dpi', TType.I32, 18)
      oprot.writeI32(self.dpi)
      oprot.writeFieldEnd()
    if self.color is not None:
      oprot.writeFieldBegin('color', TType.BOOL, 19)
      oprot.writeBool(self.color)
      oprot.writeFieldEnd()
    if self.cleaned is not None:
      oprot.writeFieldBegin('cleaned', TType.BOOL, 20)
      oprot.writeBool(self.cleaned)
      oprot.writeFieldEnd()
    if self.orientation is not None:
      oprot.writeFieldBegin('orientation', TType.BOOL, 21)
      oprot.writeBool(self.orientation)
      oprot.writeFieldEnd()
    if self.paginated is not None:
      oprot.writeFieldBegin('paginated', TType.BOOL, 22)
      oprot.writeBool(self.paginated)
      oprot.writeFieldEnd()
    if self.scanned is not None:
      oprot.writeFieldBegin('scanned', TType.BOOL, 23)
      oprot.writeBool(self.scanned)
      oprot.writeFieldEnd()
    if self.bookmarked is not None:
      oprot.writeFieldBegin('bookmarked', TType.BOOL, 24)
      oprot.writeBool(self.bookmarked)
      oprot.writeFieldEnd()
    if self.searchable is not None:
      oprot.writeFieldBegin('searchable', TType.BOOL, 25)
      oprot.writeBool(self.searchable)
      oprot.writeFieldEnd()
    if self.filesize is not None:
      oprot.writeFieldBegin('filesize', TType.I64, 26)
      oprot.writeI64(self.filesize)
      oprot.writeFieldEnd()
    if self.extension is not None:
      oprot.writeFieldBegin('extension', TType.STRING, 27)
      oprot.writeString(self.extension)
      oprot.writeFieldEnd()
    if self.file_checksums is not None:
      oprot.writeFieldBegin('file_checksums', TType.STRUCT, 28)
      self.file_checksums.write(oprot)
      oprot.writeFieldEnd()
    if self.generic is not None:
      oprot.writeFieldBegin('generic', TType.STRING, 29)
      oprot.writeString(self.generic)
      oprot.writeFieldEnd()
    if self.filename is not None:
      oprot.writeFieldBegin('filename', TType.STRING, 30)
      oprot.writeString(self.filename)
      oprot.writeFieldEnd()
    if self.visible is not None:
      oprot.writeFieldBegin('visible', TType.STRING, 31)
      oprot.writeString(self.visible)
      oprot.writeFieldEnd()
    if self.locator is not None:
      oprot.writeFieldBegin('locator', TType.STRING, 32)
      oprot.writeString(self.locator)
      oprot.writeFieldEnd()
    if self.local is not None:
      oprot.writeFieldBegin('local', TType.I32, 33)
      oprot.writeI32(self.local)
      oprot.writeFieldEnd()
    if self.added_timestamp is not None:
      oprot.writeFieldBegin('added_timestamp', TType.I64, 34)
      oprot.writeI64(self.added_timestamp)
      oprot.writeFieldEnd()
    if self.lastmodified_timestamp is not None:
      oprot.writeFieldBegin('lastmodified_timestamp', TType.I64, 35)
      oprot.writeI64(self.lastmodified_timestamp)
      oprot.writeFieldEnd()
    if self.cover_url is not None:
      oprot.writeFieldBegin('cover_url', TType.STRING, 36)
      oprot.writeString(self.cover_url)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.bookid is None:
      raise TProtocol.TProtocolException(message='Required field bookid is unset!')
    if self.title is None:
      raise TProtocol.TProtocolException(message='Required field title is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TBookStorage:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TBookStorage')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TBookMetaResult:
  """
  Attributes:
   - error
   - book_meta
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'error', None, None, ), # 1
    (2, TType.STRUCT, 'book_meta', (TBookMeta, TBookMeta.thrift_spec), None, ), # 2
  )

  def __init__(self, error=None, book_meta=None,):
    self.error = error
    self.book_meta = book_meta

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.error = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.book_meta = TBookMeta()
          self.book_meta.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TBookMetaResult')
    if self.error is not None:
      oprot.writeFieldBegin('error', TType.I32, 1)
      oprot.writeI32(self.error)
      oprot.writeFieldEnd()
    if self.book_meta is not None:
      oprot.writeFieldBegin('book_meta', TType.STRUCT, 2)
      self.book_meta.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.error is None:
      raise TProtocol.TProtocolException(message='Required field error is unset!')
    if self.book_meta is None:
      raise TProtocol.TProtocolException(message='Required field book_meta is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TMapBookMetaResult:
  """
  Attributes:
   - error
   - map_book_meta
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'error', None, None, ), # 1
    (2, TType.MAP, 'map_book_meta', (TType.I64,None,TType.STRUCT,(TBookMeta, TBookMeta.thrift_spec)), None, ), # 2
  )

  def __init__(self, error=None, map_book_meta=None,):
    self.error = error
    self.map_book_meta = map_book_meta

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.error = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.map_book_meta = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readI64();
            _val6 = TBookMeta()
            _val6.read(iprot)
            self.map_book_meta[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TMapBookMetaResult')
    if self.error is not None:
      oprot.writeFieldBegin('error', TType.I32, 1)
      oprot.writeI32(self.error)
      oprot.writeFieldEnd()
    if self.map_book_meta is not None:
      oprot.writeFieldBegin('map_book_meta', TType.MAP, 2)
      oprot.writeMapBegin(TType.I64, TType.STRUCT, len(self.map_book_meta))
      for kiter7,viter8 in self.map_book_meta.items():
        oprot.writeI64(kiter7)
        viter8.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.error is None:
      raise TProtocol.TProtocolException(message='Required field error is unset!')
    if self.map_book_meta is None:
      raise TProtocol.TProtocolException(message='Required field map_book_meta is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)