# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class MonitoringOperations(object):
    """MonitoringOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_history_server_data(
        self,
        workspace_name,  # type: str
        pool_name,  # type: str
        livy_id,  # type: str
        app_id,  # type: str
        attempt_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.HistoryServerDataResponse"
        """Get History Server Data for a given workspace, pool, livyid, appid and attemptId.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param pool_name: The spark pool name.
        :type pool_name: str
        :param livy_id: The livy id.
        :type livy_id: str
        :param app_id: The application id.
        :type app_id: str
        :param attempt_id: The attempt id.
        :type attempt_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HistoryServerDataResponse or  or the result of cls(response)
        :rtype: ~azure.synapse.models.HistoryServerDataResponse or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.HistoryServerDataResponse"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get_history_server_data.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'poolName': self._serialize.url("pool_name", pool_name, 'str'),
            'livyId': self._serialize.url("livy_id", livy_id, 'str'),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'attemptId': self._serialize.url("attempt_id", attempt_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 401]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('HistoryServerDataResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_history_server_data.metadata = {'url': '/monitoring/workloadTypes/spark/pools/{poolName}/livyIds/{livyId}/applications/{appId}/attemptIds/{attemptId}/historyServerData'}

    def get_spark_job_list(
        self,
        workspace_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SparkJobListViewResponse"
        """Get list of spark applications for the workspace.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkJobListViewResponse or  or the result of cls(response)
        :rtype: ~azure.synapse.models.SparkJobListViewResponse or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SparkJobListViewResponse"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get_spark_job_list.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 401]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SparkJobListViewResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_spark_job_list.metadata = {'url': '/monitoring/workloadTypes/spark/Applications'}

    def get_application_details(
        self,
        workspace_name,  # type: str
        pool_name,  # type: str
        livy_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SparkJobListViewResponse"
        """Get one spark application details given the workspace name, pool name and livyid.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param pool_name: The spark pool name.
        :type pool_name: str
        :param livy_id: The livy id.
        :type livy_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkJobListViewResponse or  or the result of cls(response)
        :rtype: ~azure.synapse.models.SparkJobListViewResponse or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SparkJobListViewResponse"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get_application_details.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'poolName': self._serialize.url("pool_name", pool_name, 'str'),
            'livyId': self._serialize.url("livy_id", livy_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 401]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SparkJobListViewResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_application_details.metadata = {'url': '/monitoring/workloadTypes/spark/pools/{poolName}/livyIds/{livyId}'}

    def get_history_server_properties(
        self,
        workspace_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.HistoryServerPropertiesResponse"
        """Get History server properties.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HistoryServerPropertiesResponse or  or the result of cls(response)
        :rtype: ~azure.synapse.models.HistoryServerPropertiesResponse or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.HistoryServerPropertiesResponse"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get_history_server_properties.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 401]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('HistoryServerPropertiesResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_history_server_properties.metadata = {'url': '/monitoring/workloadTypes/spark/historyServerProperties'}

    def get_history_server_diagnostic(
        self,
        workspace_name,  # type: str
        pool_name,  # type: str
        livy_id,  # type: str
        app_id,  # type: str
        attempt_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.HistoryServerDiagnosticResponse"
        """Get History Server Diagnostic Data for a given workspace, pool, livyid, appid and attemptId.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param pool_name: The spark pool name.
        :type pool_name: str
        :param livy_id: The livy id.
        :type livy_id: str
        :param app_id: The application id.
        :type app_id: str
        :param attempt_id: The attempt id.
        :type attempt_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HistoryServerDiagnosticResponse or  or the result of cls(response)
        :rtype: ~azure.synapse.models.HistoryServerDiagnosticResponse or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.HistoryServerDiagnosticResponse"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get_history_server_diagnostic.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'poolName': self._serialize.url("pool_name", pool_name, 'str'),
            'livyId': self._serialize.url("livy_id", livy_id, 'str'),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'attemptId': self._serialize.url("attempt_id", attempt_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 401]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('HistoryServerDiagnosticResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_history_server_diagnostic.metadata = {'url': '/monitoring/workloadTypes/spark/pools/{poolName}/livyIds/{livyId}/applications/{appId}/attemptIds/{attemptId}/historyServerDiagnostic'}

    def get_history_server_graph(
        self,
        workspace_name,  # type: str
        pool_name,  # type: str
        livy_id,  # type: str
        app_id,  # type: str
        attempt_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.HistoryServerGraphResponse"
        """Get History Server Graph Data for a given workspace, pool, livyid, appid and attemptId.

        :param workspace_name: The name of the workspace to execute operations on.
        :type workspace_name: str
        :param pool_name: The spark pool name.
        :type pool_name: str
        :param livy_id: The livy id.
        :type livy_id: str
        :param app_id: The application id.
        :type app_id: str
        :param attempt_id: The attempt id.
        :type attempt_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HistoryServerGraphResponse or  or the result of cls(response)
        :rtype: ~azure.synapse.models.HistoryServerGraphResponse or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.HistoryServerGraphResponse"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01-preview"

        # Construct URL
        url = self.get_history_server_graph.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self._config.synapse_dns_suffix", self._config.synapse_dns_suffix, 'str', skip_quote=True),
            'poolName': self._serialize.url("pool_name", pool_name, 'str'),
            'livyId': self._serialize.url("livy_id", livy_id, 'str'),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'attemptId': self._serialize.url("attempt_id", attempt_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 401]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('HistoryServerGraphResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_history_server_graph.metadata = {'url': '/monitoring/workloadTypes/spark/pools/{poolName}/livyIds/{livyId}/applications/{appId}/attemptIds/{attemptId}/historyServerGraph'}