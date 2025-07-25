# coding: utf-8

"""
    Business Units

    Retrieve Business Unit information.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.settings.business_units.api_client import ApiClient
from hubspot.settings.business_units.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class BusinessUnitApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def get_by_user_id(self, user_id, **kwargs):  # noqa: E501
        """Get Business Units for a user  # noqa: E501

        Get Business Units identified by `userId`. The `userId` refers to the user’s ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_user_id(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Identifier of user to retrieve. (required)
        :type user_id: str
        :param properties: The names of properties to optionally include in the response body. The only valid value is `logoMetadata`.
        :type properties: list[str]
        :param name: The names of Business Units to retrieve. If empty or not provided, then all associated Business Units will be returned.
        :type name: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CollectionResponsePublicBusinessUnitNoPaging
        """
        kwargs["_return_http_data_only"] = True
        return await self.get_by_user_id_with_http_info(user_id, **kwargs)  # noqa: E501

    async def get_by_user_id_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Get Business Units for a user  # noqa: E501

        Get Business Units identified by `userId`. The `userId` refers to the user’s ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_user_id_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Identifier of user to retrieve. (required)
        :type user_id: str
        :param properties: The names of properties to optionally include in the response body. The only valid value is `logoMetadata`.
        :type properties: list[str]
        :param name: The names of Business Units to retrieve. If empty or not provided, then all associated Business Units will be returned.
        :type name: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CollectionResponsePublicBusinessUnitNoPaging, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["user_id", "properties", "name"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_by_user_id" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get("user_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `get_by_user_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "user_id" in local_var_params:
            path_params["userId"] = local_var_params["user_id"]  # noqa: E501

        query_params = []
        if local_var_params.get("properties") is not None:  # noqa: E501
            query_params.append(("properties", local_var_params["properties"]))  # noqa: E501
            collection_formats["properties"] = "multi"  # noqa: E501
        if local_var_params.get("name") is not None:  # noqa: E501
            query_params.append(("name", local_var_params["name"]))  # noqa: E501
            collection_formats["name"] = "multi"  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "CollectionResponsePublicBusinessUnitNoPaging",
        }

        return await self.api_client.call_api(
            "/business-units/v3/business-units/user/{userId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )
