# -*- coding: utf-8 -*-

import six
from jsonschema import RefResolver
# TODO: datetime support

class RefNode(object):

    def __init__(self, data, ref):
        self.ref = ref
        self._data = data

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, value):
        return self._data.__setitem__(key, value)

    def __getattr__(self, key):
        return self._data.__getattribute__(key)

    def __iter__(self):
        return self._data.__iter__()

    def __repr__(self):
        return repr({'$ref': self.ref})

    def __eq__(self, other):
        if isinstance(other, RefNode):
            return self._data == other._data and self.ref == other.ref
        elif six.PY2:
            return object.__eq__(other)
        elif six.PY3:
            return object.__eq__(self, other)
        else:
            return False

    def __deepcopy__(self, memo):
        return RefNode(copy.deepcopy(self._data), self.ref)

    def copy(self):
        return RefNode(self._data, self.ref)

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/'

definitions = {'definitions': {'userInfo': {'type': 'object', 'properties': {'nickName': {'type': 'string'}, 'address': {'type': 'string'}}}, 'inline_response_200_userInfo': {'properties': {'nickName': {'type': 'string'}, 'avartUrl': {'type': 'string'}}}, 'idenInfo': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'sex': {'type': 'string'}, 'tel': {'type': 'string'}, 'idenType': {'type': 'string'}, 'school': {'type': 'string'}, 'company': {'type': 'string'}, 'college': {'type': 'string'}, 'id': {'type': 'string'}}}, 'publishTask_condition': {'properties': {'groups': {'type': 'array', 'items': {'type': 'string'}}, 'sex': {'type': 'string'}, 'creditScore': {'type': 'integer'}}}, 'cert': {'type': 'object', 'properties': {'files': {'type': 'array', 'items': {'type': 'string'}}, 'remarks': {'type': 'string'}}}, 'content': {'type': 'object', 'properties': {'type': {'type': 'string'}, 'wjxId': {'type': 'string'}, 'title': {'type': 'string'}, 'detail': {'type': 'string'}, 'condition': {'$ref': '#/definitions/publishTask_condition'}, 'time': {'type': 'string'}, 'money': {'type': 'number'}, 'number': {'type': 'integer'}}}}, 'parameters': {}}

validators = {
    ('login', 'POST'): {'args': {'required': ['js_code', 'app_id', 'app_secret'], 'properties': {'js_code': {'description': "user's js_code", 'type': 'string'}, 'app_id': {'description': 'miniprogram app_id', 'type': 'string'}, 'app_secret': {'description': 'miniprogram app_secret', 'type': 'string'}, 'encryptedData': {'description': "user's encryptedData when he/she has authensized getUserInfo", 'required': False, 'type': 'string'}}}},
    ('prove', 'GET'): {'args': {'required': [], 'properties': {'userId': {'required': False, 'type': 'string'}}}},
    ('prove', 'POST'): {'json': {'$ref': '#/definitions/idenInfo'}, 'args': {'required': ['cert'], 'properties': {'cert': {'description': "user's cert path", 'type': 'string'}}}},
    ('modify', 'POST'): {'json': {'$ref': '#/definitions/userInfo'}, 'args': {'required': [], 'properties': {'avartUrl': {'required': False, 'type': 'string'}}}},
    ('getProveState', 'GET'): {'args': {'required': [], 'properties': {'userId': {'required': False, 'type': 'string'}}}},
    ('getBalance', 'GET'): {'args': {'required': ['userId'], 'properties': {'userId': {'type': 'string'}}}},
    ('reCharge', 'POST'): {'args': {'required': ['userId', 'money'], 'properties': {'userId': {'type': 'string'}, 'money': {'type': 'number'}}}},
    ('createGroup', 'GET'): {'args': {'required': ['userId', 'groupName'], 'properties': {'userId': {'type': 'string'}, 'groupName': {'type': 'string'}}}},
    ('joinGroup', 'POST'): {'args': {'required': ['userId', 'groupName'], 'properties': {'userId': {'type': 'string'}, 'groupName': {'type': 'string'}}}},
    ('getGroup', 'GET'): {'args': {'required': ['userId'], 'properties': {'userId': {'type': 'string'}}}},
    ('getCreatedGroup', 'GET'): {'args': {'required': ['userId'], 'properties': {'userId': {'type': 'string'}}}},
    ('getJoinedGroup', 'GET'): {'args': {'required': ['userId'], 'properties': {'userId': {'type': 'string'}}}},
    ('getTask', 'GET'): {'args': {'required': ['pageId'], 'properties': {'pageId': {'description': 'Page number', 'type': 'integer', 'default': 0}}}},
    ('getPublishedTask', 'GET'): {'args': {'required': ['userId'], 'properties': {'userId': {'type': 'string'}}}},
    ('getAcceptedTask', 'GET'): {'args': {'required': ['userId'], 'properties': {'userId': {'type': 'string'}}}},
    ('getTaskDetail', 'GET'): {'args': {'required': [], 'properties': {'taskId': {'description': "The task's id in database.", 'required': False, 'type': 'string'}, 'userId': {'required': False, 'type': 'string'}}}},
    ('acceptTask', 'POST'): {'args': {'required': ['userId', 'taskId'], 'properties': {'userId': {'type': 'string'}, 'taskId': {'type': 'string'}}}},
    ('commitJob', 'POST'): {'json': {'$ref': '#/definitions/cert'}, 'args': {'required': ['userId', 'taskId'], 'properties': {'userId': {'type': 'string'}, 'taskId': {'type': 'string'}}}},
    ('addTaskInfo', 'POST'): {'args': {'required': ['userId', 'taskId', 'extraInfo'], 'properties': {'userId': {'type': 'string'}, 'taskId': {'type': 'string'}, 'extraInfo': {'type': 'string'}}}},
    ('abandonTask', 'POST'): {'args': {'required': ['userId', 'taskId'], 'properties': {'userId': {'type': 'string'}, 'taskId': {'type': 'string'}}}},
    ('abortTask', 'POST'): {'args': {'required': ['userId', 'taskId'], 'properties': {'userId': {'type': 'string'}, 'taskId': {'type': 'string'}}}},
    ('publishTask', 'POST'): {'json': {'$ref': '#/definitions/content'}, 'args': {'required': ['userId'], 'properties': {'userId': {'type': 'string'}}}},
}

filters = {
    ('login', 'POST'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'userId': {'type': 'string'}, 'userInfo': {'$ref': '#/definitions/inline_response_200_userInfo'}, 'authState': {'type': 'string'}}}}},
    ('prove', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'sex': {'type': 'string'}, 'idenType': {'type': 'string'}, 'tel': {'type': 'string'}, 'school': {'type': 'string'}, 'company': {'type': 'string'}, 'id': {'type': 'string', 'description': 'student id or worker id'}, 'creditScore': {'type': 'integer'}}}}},
    ('prove', 'POST'): {200: {'headers': None, 'schema': None}},
    ('modify', 'POST'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'nickName': {'type': 'string'}, 'avartUrl': {'type': 'string'}, 'address': {'type': 'string'}}}}},
    ('getProveState', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'properties': {'hasAuthensized': {'type': 'boolean'}}}}},
    ('getBalance', 'GET'): {200: {'headers': None, 'schema': {'properties': {'balance': {'type': 'number'}}}}},
    ('reCharge', 'POST'): {200: {'headers': None, 'schema': {'properties': {'balance': {'type': 'number'}}}}},
    ('createGroup', 'GET'): {200: {'headers': None, 'schema': None}, 400: {'headers': None, 'schema': None}},
    ('joinGroup', 'POST'): {200: {'headers': None, 'schema': None}, 400: {'headers': None, 'schema': None}},
    ('getGroup', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'type': 'string'}}}},
    ('getCreatedGroup', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'type': 'string'}}}},
    ('getJoinedGroup', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'type': 'string'}}}},
    ('getTask', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'icon': {'type': 'string', 'description': "the issuer's head pic"}, 'title': {'type': 'string'}, 'desc': {'type': 'string'}, 'money': {'type': 'number'}, 'left': {'type': 'integer', 'description': 'the num of the left task.'}}}}}, 400: {'headers': None, 'schema': None}},
    ('getPublishedTask', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'type': 'object', 'properties': {'icon': {'type': 'string', 'description': "the issuer's head pic"}, 'id': {'type': 'string'}, 'title': {'type': 'string'}, 'desc': {'type': 'string'}, 'money': {'type': 'number'}, 'left': {'type': 'integer', 'description': 'the num of the left task.'}}}}}, 400: {'headers': None, 'schema': None}},
    ('getAcceptedTask', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'icon': {'type': 'string', 'description': "the issue's head pic"}, 'title': {'type': 'string'}, 'desc': {'type': 'string'}, 'money': {'type': 'number'}, 'left': {'type': 'integer', 'description': 'the num of the left task.'}}}}}, 400: {'headers': None, 'schema': None}},
    ('getTaskDetail', 'GET'): {200: {'headers': None, 'schema': {'properties': {'user': {'type': 'object', 'properties': {'head': {'type': 'string'}, 'nickName': {'type': 'string'}, 'tel': {'type': 'string'}}}, 'content': {'type': 'object', 'properties': {'type': {'type': 'string'}, 'wjxId': {'type': 'string', 'description': "if the type is '问卷星', return wjxId."}, 'title': {'type': 'string'}, 'desc': {'type': 'string'}, 'money': {'type': 'number'}, 'num': {'type': 'integer', 'description': 'the num of people who have got money.'}, 'left': {'type': 'integer', 'description': 'the num of the left task.'}, 'condition': {'type': 'object', 'properties': {'groups': {'type': 'array', 'description': 'he/she who in the group can receive the task', 'items': {'type': 'string'}}, 'sex': {'type': 'string'}}}, 'steps': {'type': 'array', 'items': {'type': 'string'}}}}, 'isPublisher': {'type': 'boolean'}, 'hasReceived': {'type': 'integer', 'description': "0 stands for hasn't, 1 stands for has received, 2 stands for under review, 3 stands for has completed"}}}}, 400: {'headers': None, 'schema': None}},
    ('acceptTask', 'POST'): {200: {'headers': None, 'schema': None}},
    ('commitJob', 'POST'): {200: {'headers': None, 'schema': None}},
    ('addTaskInfo', 'POST'): {200: {'headers': None, 'schema': None}},
    ('abandonTask', 'POST'): {200: {'headers': None, 'schema': None}},
    ('abortTask', 'POST'): {200: {'headers': None, 'schema': None}},
    ('publishTask', 'POST'): {200: {'headers': None, 'schema': None}},
}

scopes = {
}

resolver = RefResolver.from_schema(definitions)

class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True, resolver=None):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults, resolver=resolver)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None, resolver=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key or '$ref' in _schema:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, (dict, RefNode)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize_ref(schema, data):
        if resolver == None:
            raise TypeError("resolver must be provided")
        ref = schema.get(u"$ref")
        scope, resolved = resolver.resolve(ref)
        if resolved.get('nullable', False) and not data:
            return {}
        return _normalize(resolved, data)

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
            'ref': _normalize_ref
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'
        if schema.get(u'$ref', None):
            type_ = 'ref'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors
