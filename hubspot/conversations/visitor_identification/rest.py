# coding: utf-8

"""
    Visitor Identification

    The Visitor Identification API allows you to pass identification information to the HubSpot chat widget for otherwise unknown visitors that were verified by your own authentication system.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import io
import json
import logging
import re
import ssl

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import urlencode
import urllib3

from hubspot.conversations.visitor_identification.exceptions import ApiException, UnauthorizedException, ForbiddenException, NotFoundException, ServiceException, ApiValueError


logger = logging.getLogger(__name__)


from hubspot.rest import get_rest_client, get_rest_response
RESTResponse = get_rest_response()
RESTClientObject = get_rest_client(ApiException, UnauthorizedException, ForbiddenException, NotFoundException, ServiceException, ApiValueError, RESTResponse)
