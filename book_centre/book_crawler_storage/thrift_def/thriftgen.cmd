#!/bin/sh

THRIFT_EXE=thrift
TFOLDER=thrift

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#thrift
rm -f gen-python/*

$THRIFT_EXE --gen py book_model_shared.thrift
$THRIFT_EXE --gen py book_crawler_storage_shared.thrift
$THRIFT_EXE --gen py book_crawler_storage_service.thrift