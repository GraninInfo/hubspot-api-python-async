# coding: utf-8

"""
    Imports

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.imports.api_client import ApiClient
from hubspot.crm.imports.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class PublicImportsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def get_errors(self, import_id, **kwargs):  # noqa: E501
        """get_errors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_errors(import_id, async_req=True)
        >>> result = thread.get()

        :param import_id: (required)
        :type import_id: int
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param limit: The maximum number of results to display per page.
        :type limit: int
        :param include_error_message: Set to True to receive a message explaining the error.
        :type include_error_message: bool
        :param include_row_data: Set to True to receive the data values for the errored row.
        :type include_row_data: bool
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
        :rtype: CollectionResponsePublicImportErrorForwardPaging
        """
        kwargs["_return_http_data_only"] = True
        return await self.get_errors_with_http_info(import_id, **kwargs)  # noqa: E501

    async def get_errors_with_http_info(self, import_id, **kwargs):  # noqa: E501
        """get_errors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_errors_with_http_info(import_id, async_req=True)
        >>> result = thread.get()

        :param import_id: (required)
        :type import_id: int
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param limit: The maximum number of results to display per page.
        :type limit: int
        :param include_error_message: Set to True to receive a message explaining the error.
        :type include_error_message: bool
        :param include_row_data: Set to True to receive the data values for the errored row.
        :type include_row_data: bool
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
        :rtype: tuple(CollectionResponsePublicImportErrorForwardPaging, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["import_id", "after", "limit", "include_error_message", "include_row_data"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_errors" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'import_id' is set
        if self.api_client.client_side_validation and local_var_params.get("import_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `import_id` when calling `get_errors`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "import_id" in local_var_params:
            path_params["importId"] = local_var_params["import_id"]  # noqa: E501

        query_params = []
        if local_var_params.get("after") is not None:  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if local_var_params.get("limit") is not None:  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if local_var_params.get("include_error_message") is not None:  # noqa: E501
            query_params.append(("includeErrorMessage", local_var_params["include_error_message"]))  # noqa: E501
        if local_var_params.get("include_row_data") is not None:  # noqa: E501
            query_params.append(("includeRowData", local_var_params["include_row_data"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "CollectionResponsePublicImportErrorForwardPaging",
        }

        return await self.api_client.call_api(
            "/crm/v3/imports/{importId}/errors",
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
