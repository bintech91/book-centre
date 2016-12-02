#!/bin/sh

THRIFT_EXE=thrift
TFOLDER=thrift

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#thrift
rm -f gen-python/*

$THRIFT_EXE --gen py book_model_shared.thrift
$THRIFT_EXE --gen py book_storage_service.thrift

rm -f ../thrift/book_model_shared/*.py

mv gen-py/book_model_shared/*.py  ../thrift/book_model_shared/
mv gen-py/book_storage_service/*.py  ../thrift/book_model_shared/

rm -f gen-py/book_model_shared/*.py
rm -f gen-py/book_storage_service/*.py
