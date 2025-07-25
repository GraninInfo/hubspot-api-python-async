# coding: utf-8
"""
    Public App Crm Cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

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

from hubspot.crm.extensions.cards.configuration import Configuration
import hubspot.crm.extensions.cards.models as models
from hubspot.crm.extensions.cards import rest
from hubspot.crm.extensions.cards.exceptions import ApiValueError, ApiException

from hubspot.api_client import get_api_client
ApiClient = get_api_client(Configuration, models, rest, ApiValueError, ApiException)
