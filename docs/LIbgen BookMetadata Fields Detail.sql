CREATE TABLE `addedrowsinupdated` (
  `ID` int(15) unsigned NOT NULL AUTO_INCREMENT,
  `Title` varchar(2000) DEFAULT '',
  `VolumeInfo` varchar(100) DEFAULT '',
  `Series` varchar(300) DEFAULT '',
  `Periodical` varchar(200) DEFAULT '',
  `Author` varchar(1000) DEFAULT '',
  `Year` varchar(14) DEFAULT '',
  `Edition` varchar(60) DEFAULT '',
  `Publisher` varchar(400) DEFAULT '',
  `City` varchar(100) DEFAULT '',
  `Pages` varchar(100) DEFAULT '',
  `Language` varchar(150) DEFAULT '',
  `Topic` varchar(500) DEFAULT '',
  `Library` varchar(50) DEFAULT '',
  `Issue` varchar(100) DEFAULT '',
  `Identifier` varchar(600) DEFAULT '',
  `ISSN` varchar(9) DEFAULT '',
  `ASIN` varchar(200) DEFAULT '',
  `UDC` varchar(200) DEFAULT '',
  `LBC` varchar(200) DEFAULT '',
  `DDC` varchar(45) DEFAULT '',
  `LCC` varchar(45) DEFAULT '',
  `Doi` varchar(45) DEFAULT '',
  `Googlebookid` varchar(45) DEFAULT '',
  `OpenLibraryID` varchar(200) DEFAULT '',
  `Commentary` varchar(10000) DEFAULT '',
  `DPI` int(6) unsigned DEFAULT '0',
  `Color` varchar(1) DEFAULT '',
  `Cleaned` varchar(1) DEFAULT '',
  `Orientation` varchar(1) DEFAULT '',
  `Paginated` varchar(1) DEFAULT '',
  `Scanned` varchar(1) DEFAULT '',
  `Vector` varchar(1) DEFAULT '',
  `Bookmarked` varchar(1) DEFAULT '',
  `Searchable` varchar(1) DEFAULT '',
  `Filesize` bigint(20) unsigned NOT NULL DEFAULT '0',
  `Extension` varchar(50) DEFAULT '',
  `MD5` char(32) DEFAULT '',
  `CRC32` char(8) DEFAULT '',
  `eDonkey` char(32) DEFAULT '',
  `AICH` char(32) DEFAULT '',
  `SHA1` char(40) DEFAULT '',
  `TTH` char(39) DEFAULT '',
  `Generic` char(32) DEFAULT '',
  `Filename` char(50) DEFAULT '',
  `Visible` char(3) DEFAULT '',
  `Locator` varchar(733) DEFAULT '',
  `Local` int(10) unsigned DEFAULT '0',
  `TimeAdded` timestamp NOT NULL DEFAULT '2000-01-01 05:00:00',
  `TimeLastModified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Coverurl` varchar(200) DEFAULT '',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `MD5` (`MD5`),
  KEY `Identifier` (`Identifier`(333)) USING BTREE,
  FULLTEXT KEY `Title` (`Title`),
  FULLTEXT KEY `Author` (`Author`),
  FULLTEXT KEY `Language` (`Language`),
  FULLTEXT KEY `Extension` (`Extension`),
  FULLTEXT KEY `Publisher` (`Publisher`),
  FULLTEXT KEY `Topic` (`Topic`),
  FULLTEXT KEY `MD51` (`MD5`),
  FULLTEXT KEY `Series` (`Series`),
  FULLTEXT KEY `Year` (`Year`),
  FULLTEXT KEY `Title1` (`Title`,`Author`,`Series`,`Publisher`,`Year`,`Periodical`,`VolumeInfo`),
  FULLTEXT KEY `Generic` (`Generic`),
  FULLTEXT KEY `Identifierfulltext` (`Identifier`)
) ENGINE=MyISAM AUTO_INCREMENT=866842 DEFAULT CHARSET=utf8;
