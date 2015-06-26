# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.
import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys
try:
    import s3_settings
except:
    print ("There should be a s3_settings.py file with the name \
           of the bucket with the photos.")

def allowed_file(filename):
    return '.' in filename and \
              filename.rsplit('.', 1)[1] in s3_settings.ALLOWED_EXTENSIONS


def get_s3_photos(folder):
    """
    Get photos from S3 bucket.

    :returns: A list of photos.
    :rtype: list

    """
    conn = S3Connection(s3_settings.ACCESS_KEY, s3_settings.SECRET)
    bucket = conn.get_bucket(s3_settings.BUCKET)
    rs = bucket.list(s3_settings.FOLDER)
    photos = []
    for photo in rs:
        if allowed_file(photo.name.lower()):
            link = dict(
                url_b="http://" + s3_settings.BUCKET + ".s3.amazonaws.com/" + photo.name
            )
            print(link)
            photos.append(link)

    return photos
