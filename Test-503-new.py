#!/usr/bin/env python3
from sys import exit
from test.http_test import HTTPTest
from misc.wget_file import WgetFile

"""
    This test ensures that Wget handles a 503 Service Unavailable response
    correctly.
"""
TEST_NAME = "503 Service Unavailable"
############# File Definitions ###############################################
File1 = """All happy families are alike;
Each unhappy family is unhappy in its own way"""
#File2 = "Anyone for chocochip cookies?"

File1_rules = {
    "Response"          : 503
}

A_File = WgetFile ("File1", File1, rules=File1_rules)
#B_File = WgetFile ("File2", File2)

Request_List = [
    [
        "GET /File1"
        
    ]
]


WGET_OPTIONS = " "
WGET_URLS = [["File1"]]

Files = [[A_File]]

ExpectedReturnCode = 8
ExpectedDownloadedFiles = []

################ Pre and Post Test Hooks #####################################
pre_test = {
    "ServerFiles"       : Files
}
test_options = {
    "WgetCommands"      : WGET_OPTIONS,
    "Urls"              : WGET_URLS
}
post_test = {
    "ExpectedFiles"     : ExpectedDownloadedFiles,
    "ExpectedRetcode"   : ExpectedReturnCode,
    "FilesCrawled"      : Request_List
}

err = HTTPTest (
                name=TEST_NAME,
                pre_hook=pre_test,
                test_params=test_options,
                post_hook=post_test
).begin ()

exit (err)
