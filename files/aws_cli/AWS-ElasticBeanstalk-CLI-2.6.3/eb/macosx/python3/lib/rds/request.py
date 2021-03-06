#!/usr/bin/env python
#==============================================================================
# Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License"). You may not use
# this file except in compliance with the License. A copy of the License is
# located at
#
#       http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file. This file is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or
# implied. See the License for the specific language governing permissions
# and limitations under the License.
#==============================================================================

from lib.utility import misc

class Request(object):
    '''
    Convert and store RDS request parameters
    '''
    
    def __init__(self):
        self._request = dict()

    def _set_to_list(self, name_set):
        name_list = []
        if isinstance(name_set, set):
            for name in name_set:
                name_list.append(str(name))
        else:
            name_list.append(str(name_set))
        return name_list         
    
    def __repr__(self):
        try:
            text = 'Request API: {0}. \nParameters: [\n'.format(self._request['Operation'])
        except:
            text = 'Parameters:[\n'
        
        for key,value in self._request.items():
            text = text + ' {0} : {1}\n'.format(key, value)
        text = text + ']'
        
        return text
    
    def get_dict(self):
        return self._request
    
    def set_action(self, name):
        self._request['Action'] = misc.to_unicode(name)

    def set_engine(self, string):
        self._request['Engine'] = misc.to_unicode(string)

    def set_engine_version(self, string):
        self._request['EngineVersion'] = misc.to_unicode(string)

    def set_db_instance_identifier(self, string):
        self._request['DBInstanceIdentifier'] = misc.to_unicode(string)

    def set_db_snapshot_identifier(self, string):
        self._request['DBSnapshotIdentifier'] = misc.to_unicode(string)

    def set_snapshot_type(self, string):
        self._request['SnapshotType'] = misc.to_unicode(string)
    
    def set_default_only(self, string):
        self._request['DefaultOnly'] = misc.to_unicode(string)

    def set_db_parameter_group_family(self, string):
        self._request['DBParameterGroupFamily'] = misc.to_unicode(string)

    def set_list_supported_character_sets(self, string):
        self._request['ListSupportedCharacterSets'] = misc.to_unicode(string)

    def set_marker(self, string):
        self._request['Marker'] = misc.to_unicode(string)
        
    def set_max_records(self, num):
        self._request['MaxRecords'] = misc.to_unicode(num)
        
        
        
        
class Response(object):
    
    def __init__(self, request_id, result = None, marker = None):
        self._request_id = request_id
        self._result = result
        self._marker = marker
        
    def __repr__(self):
        return 'API Response.\n Request ID: {0}\n Results: {1}'.\
            format(self.request_id, misc.collection_to_string(self._result))
        
    @property
    def request_id(self):
        return self._request_id
    
    @property
    def result(self):
        return self._result
    
    @property
    def marker(self):
        return self._marker
    