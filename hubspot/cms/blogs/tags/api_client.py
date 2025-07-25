# coding: utf-8
"""
    Tags

    Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import atexit
import datetime
from dateutil.parser import parse
import json
import mimetypes
from multiprocessing.pool import ThreadPool
import os
import re
import tempfile

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import quote

from hubspot.cms.blogs.tags.configuration import Configuration
import hubspot.cms.blogs.tags.models as models
from hubspot.cms.blogs.tags import rest
from hubspot.cms.blogs.tags.exceptions import ApiValueError, ApiException

from hubspot.api_client import get_api_client
ApiClient = get_api_client(Configuration, models, rest, ApiValueError, ApiException)
