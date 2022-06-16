# -*- coding: utf-8 -*-

"""
managementservice

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from managementservice.api_helper import APIHelper


class CreateProjectDto(object):

    """Implementation of the 'CreateProjectDto' model.

    TODO: type model description here.

    Attributes:
        title (string): TODO: type description here.
        description (string): TODO: type description here.
        owner_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title": 'title',
        "description": 'description',
        "owner_id": 'ownerId'
    }

    _optionals = [
        'title',
        'description',
        'owner_id',
    ]

    def __init__(self,
                 title=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 owner_id=APIHelper.SKIP):
        """Constructor for the CreateProjectDto class"""

        # Initialize members of the class
        if title is not APIHelper.SKIP:
            self.title = title 
        if description is not APIHelper.SKIP:
            self.description = description 
        if owner_id is not APIHelper.SKIP:
            self.owner_id = owner_id 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        owner_id = dictionary.get("ownerId") if dictionary.get("ownerId") else APIHelper.SKIP
        # Return an object of this model
        return cls(title,
                   description,
                   owner_id)
