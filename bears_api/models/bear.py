# coding: utf-8

"""
    Swagger Bearsapi (Simple)

    A sample API that uses a bears=mongostore as an example to demonstrate features in the swagger-2.0 specification

    OpenAPI spec version: 1.0.1
    Contact: foo@example.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat

from six import iteritems


class Bear(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'created_at': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': '_id',
        'created_at': 'created_at',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, id=None, created_at=None, name=None):
        """
        Bear - a model defined in Swagger
        """

        self._id = None
        self._created_at = None
        self._id = None
        self._name = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        self.id = id
        self.name = name

    @property
    def id(self):
        """
        Gets the id of this Bear.

        :return: The id of this Bear.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Bear.

        :param id: The id of this Bear.
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Bear.

        :return: The created_at of this Bear.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Bear.

        :param created_at: The created_at of this Bear.
        :type: str
        """

        self._created_at = created_at

    # @property
    # def id(self):
    #     """
    #     Gets the id of this Bear.
    #
    #     :return: The id of this Bear.
    #     :rtype: str
    #     """
    #     return self._id
    #
    # @id.setter
    # def id(self, id):
    #     """
    #     Sets the id of this Bear.
    #
    #     :param id: The id of this Bear.
    #     :type: str
    #     """
    #     if id is None:
    #         raise ValueError("Invalid value for `id`, must not be `None`")
    #
    #     self._id = id

    @property
    def name(self):
        """
        Gets the name of this Bear.

        :return: The name of this Bear.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Bear.

        :param name: The name of this Bear.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, Bear):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
