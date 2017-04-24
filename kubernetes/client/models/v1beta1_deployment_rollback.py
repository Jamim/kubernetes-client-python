# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1DeploymentRollback(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, kind=None, name=None, rollback_to=None, updated_annotations=None):
        """
        V1beta1DeploymentRollback - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'kind': 'str',
            'name': 'str',
            'rollback_to': 'V1beta1RollbackConfig',
            'updated_annotations': 'dict(str, str)'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'name': 'name',
            'rollback_to': 'rollbackTo',
            'updated_annotations': 'updatedAnnotations'
        }

        self._api_version = api_version
        self._kind = kind
        self._name = name
        self._rollback_to = rollback_to
        self._updated_annotations = updated_annotations

    @property
    def api_version(self):
        """
        Gets the api_version of this V1beta1DeploymentRollback.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1beta1DeploymentRollback.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1beta1DeploymentRollback.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1beta1DeploymentRollback.
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """
        Gets the kind of this V1beta1DeploymentRollback.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1beta1DeploymentRollback.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1beta1DeploymentRollback.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1beta1DeploymentRollback.
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1beta1DeploymentRollback.
        Required: This must match the Name of a deployment.

        :return: The name of this V1beta1DeploymentRollback.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1beta1DeploymentRollback.
        Required: This must match the Name of a deployment.

        :param name: The name of this V1beta1DeploymentRollback.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def rollback_to(self):
        """
        Gets the rollback_to of this V1beta1DeploymentRollback.
        The config of this deployment rollback.

        :return: The rollback_to of this V1beta1DeploymentRollback.
        :rtype: V1beta1RollbackConfig
        """
        return self._rollback_to

    @rollback_to.setter
    def rollback_to(self, rollback_to):
        """
        Sets the rollback_to of this V1beta1DeploymentRollback.
        The config of this deployment rollback.

        :param rollback_to: The rollback_to of this V1beta1DeploymentRollback.
        :type: V1beta1RollbackConfig
        """
        if rollback_to is None:
            raise ValueError("Invalid value for `rollback_to`, must not be `None`")

        self._rollback_to = rollback_to

    @property
    def updated_annotations(self):
        """
        Gets the updated_annotations of this V1beta1DeploymentRollback.
        The annotations to be updated to a deployment

        :return: The updated_annotations of this V1beta1DeploymentRollback.
        :rtype: dict(str, str)
        """
        return self._updated_annotations

    @updated_annotations.setter
    def updated_annotations(self, updated_annotations):
        """
        Sets the updated_annotations of this V1beta1DeploymentRollback.
        The annotations to be updated to a deployment

        :param updated_annotations: The updated_annotations of this V1beta1DeploymentRollback.
        :type: dict(str, str)
        """

        self._updated_annotations = updated_annotations

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other