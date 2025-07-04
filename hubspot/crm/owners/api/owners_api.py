# coding: utf-8

"""
    Crm Owners

    HubSpot uses **owners** to assign CRM objects to specific people in your organization. The endpoints described here are used to get a list of the owners that are available for an account. To assign an owner to an object, set the hubspot_owner_id property using the appropriate CRM object update or create a request.  If teams are available for your HubSpot tier, these endpoints will also indicate which team(s) an owner can access, as well as which team is the owner's primary team.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.owners.api_client import ApiClient
from hubspot.crm.owners.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class OwnersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def get_by_id(self, owner_id, **kwargs):  # noqa: E501
        """Read an owner by given `id` or `userId`  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id(owner_id, async_req=True)
        >>> result = thread.get()

        :param owner_id: (required)
        :type owner_id: int
        :param id_property:
        :type id_property: str
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
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
        :rtype: PublicOwner
        """
        kwargs["_return_http_data_only"] = True
        return await self.get_by_id_with_http_info(owner_id, **kwargs)  # noqa: E501

    async def get_by_id_with_http_info(self, owner_id, **kwargs):  # noqa: E501
        """Read an owner by given `id` or `userId`  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id_with_http_info(owner_id, async_req=True)
        >>> result = thread.get()

        :param owner_id: (required)
        :type owner_id: int
        :param id_property:
        :type id_property: str
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
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
        :rtype: tuple(PublicOwner, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["owner_id", "id_property", "archived"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_by_id" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'owner_id' is set
        if self.api_client.client_side_validation and local_var_params.get("owner_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `owner_id` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner_id" in local_var_params:
            path_params["ownerId"] = local_var_params["owner_id"]  # noqa: E501

        query_params = []
        if local_var_params.get("id_property") is not None:  # noqa: E501
            query_params.append(("idProperty", local_var_params["id_property"]))  # noqa: E501
        if local_var_params.get("archived") is not None:  # noqa: E501
            query_params.append(("archived", local_var_params["archived"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "PublicOwner",
        }

        return await self.api_client.call_api(
            "/crm/v3/owners/{ownerId}",
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

    async def get_page(self, **kwargs):  # noqa: E501
        """Get a page of owners  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page(async_req=True)
        >>> result = thread.get()

        :param email: Filter by email address (optional)
        :type email: str
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param limit: The maximum number of results to display per page.
        :type limit: int
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
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
        :rtype: CollectionResponsePublicOwnerForwardPaging
        """
        kwargs["_return_http_data_only"] = True
        return await self.get_page_with_http_info(**kwargs)  # noqa: E501

    async def get_page_with_http_info(self, **kwargs):  # noqa: E501
        """Get a page of owners  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page_with_http_info(async_req=True)
        >>> result = thread.get()

        :param email: Filter by email address (optional)
        :type email: str
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param limit: The maximum number of results to display per page.
        :type limit: int
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
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
        :rtype: tuple(CollectionResponsePublicOwnerForwardPaging, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["email", "after", "limit", "archived"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_page" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get("email") is not None:  # noqa: E501
            query_params.append(("email", local_var_params["email"]))  # noqa: E501
        if local_var_params.get("after") is not None:  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if local_var_params.get("limit") is not None:  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if local_var_params.get("archived") is not None:  # noqa: E501
            query_params.append(("archived", local_var_params["archived"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "CollectionResponsePublicOwnerForwardPaging",
        }

        return await self.api_client.call_api(
            "/crm/v3/owners/",
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
