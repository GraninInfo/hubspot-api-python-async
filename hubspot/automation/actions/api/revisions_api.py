# coding: utf-8

"""
    Automation Actions V4

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.automation.actions.api_client import ApiClient
from hubspot.automation.actions.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class RevisionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def get_by_id(self, definition_id, revision_id, app_id, **kwargs):  # noqa: E501
        """Gets a revision for a given definition by revision id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id(definition_id, revision_id, app_id, async_req=True)
        >>> result = thread.get()

        :param definition_id: (required)
        :type definition_id: str
        :param revision_id: (required)
        :type revision_id: str
        :param app_id: (required)
        :type app_id: int
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
        :rtype: PublicActionRevision
        """
        kwargs["_return_http_data_only"] = True
        return await self.get_by_id_with_http_info(definition_id, revision_id, app_id, **kwargs)  # noqa: E501

    async def get_by_id_with_http_info(self, definition_id, revision_id, app_id, **kwargs):  # noqa: E501
        """Gets a revision for a given definition by revision id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id_with_http_info(definition_id, revision_id, app_id, async_req=True)
        >>> result = thread.get()

        :param definition_id: (required)
        :type definition_id: str
        :param revision_id: (required)
        :type revision_id: str
        :param app_id: (required)
        :type app_id: int
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
        :rtype: tuple(PublicActionRevision, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["definition_id", "revision_id", "app_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_by_id" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'definition_id' is set
        if self.api_client.client_side_validation and local_var_params.get("definition_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `definition_id` when calling `get_by_id`")  # noqa: E501
        # verify the required parameter 'revision_id' is set
        if self.api_client.client_side_validation and local_var_params.get("revision_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `revision_id` when calling `get_by_id`")  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and local_var_params.get("app_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "definition_id" in local_var_params:
            path_params["definitionId"] = local_var_params["definition_id"]  # noqa: E501
        if "revision_id" in local_var_params:
            path_params["revisionId"] = local_var_params["revision_id"]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["developer_hapikey"]  # noqa: E501

        response_types_map = {
            200: "PublicActionRevision",
        }

        return await self.api_client.call_api(
            "/automation/v4/actions/{appId}/{definitionId}/revisions/{revisionId}",
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

    async def get_page(self, definition_id, app_id, **kwargs):  # noqa: E501
        """Get all revisions for a given definition  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page(definition_id, app_id, async_req=True)
        >>> result = thread.get()

        :param definition_id: (required)
        :type definition_id: str
        :param app_id: (required)
        :type app_id: int
        :param limit: The maximum number of results to display per page.
        :type limit: int
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
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
        :rtype: CollectionResponsePublicActionRevisionForwardPaging
        """
        kwargs["_return_http_data_only"] = True
        return await self.get_page_with_http_info(definition_id, app_id, **kwargs)  # noqa: E501

    async def get_page_with_http_info(self, definition_id, app_id, **kwargs):  # noqa: E501
        """Get all revisions for a given definition  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page_with_http_info(definition_id, app_id, async_req=True)
        >>> result = thread.get()

        :param definition_id: (required)
        :type definition_id: str
        :param app_id: (required)
        :type app_id: int
        :param limit: The maximum number of results to display per page.
        :type limit: int
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
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
        :rtype: tuple(CollectionResponsePublicActionRevisionForwardPaging, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["definition_id", "app_id", "limit", "after"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_page" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'definition_id' is set
        if self.api_client.client_side_validation and local_var_params.get("definition_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `definition_id` when calling `get_page`")  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and local_var_params.get("app_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `get_page`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "definition_id" in local_var_params:
            path_params["definitionId"] = local_var_params["definition_id"]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []
        if local_var_params.get("limit") is not None:  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if local_var_params.get("after") is not None:  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["developer_hapikey"]  # noqa: E501

        response_types_map = {
            200: "CollectionResponsePublicActionRevisionForwardPaging",
        }

        return await self.api_client.call_api(
            "/automation/v4/actions/{appId}/{definitionId}/revisions",
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
