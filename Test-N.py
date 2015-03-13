#!/usr/bin/env python3
from sys import exit
from test.http_test import HTTPTest
from misc.wget_file import WgetFile

"""
    This test ensures that Wget correctly handles the -N command for checking timestamp of local files and server files .
"""
TEST_NAME = "Checking time stamp"
############# File Definitions ###############################################
File1 = "Test Contents."



File1_rules = {
	"Last_Modified" : "Sat, 28 Nov 2009 03:50:37 GMT"	
}

A_File = WgetFile ("File1", File1,File1_rules)

WGET_OPTIONS = "-N "
WGET_URLS = [["File1"]]



Files = [[A_File]]
ExistingFiles = [A_File]

ExpectedReturnCode = 0
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
    "ExpectedRetcode"   : ExpectedReturnCode

}

err = HTTPTest (
                name=TEST_NAME,
                pre_hook=pre_test,
                test_params=test_options,
                post_hook=post_test
).begin ()

exit (err)
