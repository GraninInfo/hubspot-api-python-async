# coding: utf-8

"""
    CRM Deal Splits

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.objects.deal_splits.api_client import ApiClient
from hubspot.crm.objects.deal_splits.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class BatchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def read(self, batch_input_public_object_id, **kwargs):  # noqa: E501
        """Read a batch of deal split objects by their associated deal object internal ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read(batch_input_public_object_id, async_req=True)
        >>> result = thread.get()

        :param batch_input_public_object_id: (required)
        :type batch_input_public_object_id: BatchInputPublicObjectId
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
        :rtype: BatchResponseDealToDealSplits
        """
        kwargs["_return_http_data_only"] = True
        return await self.read_with_http_info(batch_input_public_object_id, **kwargs)  # noqa: E501

    async def read_with_http_info(self, batch_input_public_object_id, **kwargs):  # noqa: E501
        """Read a batch of deal split objects by their associated deal object internal ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read_with_http_info(batch_input_public_object_id, async_req=True)
        >>> result = thread.get()

        :param batch_input_public_object_id: (required)
        :type batch_input_public_object_id: BatchInputPublicObjectId
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
        :rtype: tuple(BatchResponseDealToDealSplits, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["batch_input_public_object_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method read" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_public_object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("batch_input_public_object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_public_object_id` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_public_object_id" in local_var_params:
            body_params = local_var_params["batch_input_public_object_id"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "BatchResponseDealToDealSplits",
            207: "BatchResponseDealToDealSplitsWithErrors",
        }

        return await self.api_client.call_api(
            "/crm/v3/objects/deals/splits/batch/read",
            "POST",
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

    async def upsert(self, public_deal_splits_batch_create_request, **kwargs):  # noqa: E501
        """Create or replace deal splits for deals with the provided IDs. Deal split percentages for each deal must sum up to 1.0 (100%) and may have up to 8 decimal places  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upsert(public_deal_splits_batch_create_request, async_req=True)
        >>> result = thread.get()

        :param public_deal_splits_batch_create_request: (required)
        :type public_deal_splits_batch_create_request: PublicDealSplitsBatchCreateRequest
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
        :rtype: BatchResponseDealToDealSplits
        """
        kwargs["_return_http_data_only"] = True
        return await self.upsert_with_http_info(public_deal_splits_batch_create_request, **kwargs)  # noqa: E501

    async def upsert_with_http_info(self, public_deal_splits_batch_create_request, **kwargs):  # noqa: E501
        """Create or replace deal splits for deals with the provided IDs. Deal split percentages for each deal must sum up to 1.0 (100%) and may have up to 8 decimal places  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upsert_with_http_info(public_deal_splits_batch_create_request, async_req=True)
        >>> result = thread.get()

        :param public_deal_splits_batch_create_request: (required)
        :type public_deal_splits_batch_create_request: PublicDealSplitsBatchCreateRequest
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
        :rtype: tuple(BatchResponseDealToDealSplits, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["public_deal_splits_batch_create_request"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method upsert" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'public_deal_splits_batch_create_request' is set
        if self.api_client.client_side_validation and local_var_params.get("public_deal_splits_batch_create_request") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `public_deal_splits_batch_create_request` when calling `upsert`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "public_deal_splits_batch_create_request" in local_var_params:
            body_params = local_var_params["public_deal_splits_batch_create_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "BatchResponseDealToDealSplits",
            207: "BatchResponseDealToDealSplitsWithErrors",
        }

        return await self.api_client.call_api(
            "/crm/v3/objects/deals/splits/batch/upsert",
            "POST",
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
