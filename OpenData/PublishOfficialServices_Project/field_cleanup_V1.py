__file__ = 'field_cleanup_V1'
__date__ = '6/21/2016'
__author__ = 'ABREZNIC'
"""
The MIT License (MIT)

Copyright (c) 2016 Texas Department of Transportation
Author: Adam Breznicky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import arcpy, datetime, os
from arcpy import env

# variables
remove_fields = ["created_user", "created_date", "last_edited_user", "last_edited_date", "GRID_OP", "CREATE_DT", "CREATE_NM", "EDIT_DT", "EDIT_NM", "OGEOMS", "EDIT_TYPE", "ETL_JOB_ID", "ETL_STAT", "GSC", "CreationDate", "Creator", "EditDate", "Editor"]
local_fgdb = r"C:\TxDOT\Scripts\javascript\OpenData\PublishOfficialServices_Project\Adam.gdb"
feature_class_name = "Texas_Urbanized_Area_Boundaries"

env.workspace = local_fgdb
now = datetime.datetime.now()
feature_class = local_fgdb + os.sep + feature_class_name

print "and away we go..."
print feature_class_name

fields = arcpy.ListFields(feature_class)
for field in fields:
    if field.name in remove_fields:
        print "deleting " + field.name
        arcpy.DeleteField_management(feature_class, field.name)


print "started: " + str(now)
now = datetime.datetime.now()
print "ended: " + str(now)

print "that's all folks!!"
