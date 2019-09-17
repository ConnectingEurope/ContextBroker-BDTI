from cb_bdti.conf.static import *


class OrionNotReachable(Exception):
	def __init__(self, url):
		"""
		This exception is called when the Orion's subscription service is not reachable
		:param str url: URL to reach Orion
		"""
		message = "Orion's subscription service is not reachable at %s" % url
		super(OrionNotReachable, self).__init__(message)


class CygnysNotReachable(Exception):
	def __init__(self, url):
		"""
		This exception is called when the Cygnus's notification service is not reachable
		:param str url: URL to reach Cygnus
		"""
		message = 'Cygnus notification service is not reachable at %s' % url
		super(CygnysNotReachable, self).__init__(message)

class CygnysNotReachableSSH(Exception):
	def __init__(self):
		"""
		This exception is called when the Cygnus's notification service is not reachable
		:param str url: URL to reach Cygnus
		"""
		message = 'Cygnus host is not reachable via SSH'
		super(CygnysNotReachableSSH, self).__init__(message)


class SectionKeyError(Exception):
	def __init__(self, section, key):
		"""
		This exception is called if a key is not present in the given section
		:param str section: a section of the configuration file
		:param str key: a key of a section of the configuration file
		"""
		message = '"%s" key is not present in "%s" section' % (key, section)
		super(SectionKeyError, self).__init__(message)


class NoDataModelsIntegrated(Exception):
	def __init__(self):
		"""
		This exception is called if a key is not present in the given section
		:param str section: a section of the configuration file
		:param str key: a key of a section of the configuration file
		"""
		message = 'You did not specify any Data Model for %s key in config file' %DATA_MODELS
		super(NoDataModelsIntegrated, self).__init__(message)


class HdfsNotReachable(Exception):
	def __init__(self, host, port, remotely, cygnus_ip):
		"""
		This exception is called if the HDFS cannot be reached with the given parameters
		:param str host: HDFS host
		:param str port:  HDFS port
		:param bool remotely: indicates if the connection to HDFS is a remote connection
		:param str cygnus_ip: Cygnus IP if connection is remote
		"""
		message = 'HDFS is not reachable. Unable to connect to %s:%s' % (host, port)
		message += " from Cygnus (%s)" %cygnus_ip
		super(HdfsNotReachable, self).__init__(message)


class NotValidHdfsFormatFile(Exception):
	def __init__(self, format_file):
		"""
		This exception is called if a not valid format file is provided
		:param str format_file: the format file
		"""
		message = '"%s" file format is not valid. Allowed file formats: %s' % (
			format_file, ", ".join(HDFS_FORMAT_FILE_LIST))
		super(NotValidHdfsFormatFile, self).__init__(message)


class CygnusImageNotFound(Exception):
	def __init__(self):
		"""
		This exception is called if the docker image from Cygnus is not found
		"""
		message = 'Docker image from Cygnus (%s) was not found' %CYGNUS_IMAGE_NAME
		super(CygnusImageNotFound, self).__init__(message)


class NotValidThrottling(Exception):
	def __init__(self, datamodel):
		"""
		This exception is called if a datamodel contains an invalid throttling value
		:param str datamodel: the name of a datamodel
		"""
		message = 'Not valid throttling for %s Data Model. It must be an integer value' % datamodel
		super(NotValidThrottling, self).__init__(message)


class NotValidExpires(Exception):
	def __init__(self, datamodel):
		"""
		This exception is called if a datamodel contains an invalid expiration value
		:param str datamodel: the name of a datamodel
		"""
		message = 'Not valid expires for %s Data Model. Must be in ISO8601 format. E.g. 2020-01-01, 2020-01-01T10:10.' % datamodel
		super(NotValidExpires, self).__init__(message)


class NotValidTypes(Exception):
	def __init__(self, datamodel, valid_types):
		"""
		This exception is called if a datamodel contains an invalid types value
		:param str datamodel: the name of a datamodel
		:param valid_types: types allowed for a datamodel
		"""
		message = 'Not valid types for %s Data Model. Must be one or more of these values: %s' % (datamodel, ', '.join(valid_types))
		super(NotValidTypes, self).__init__(message)


class CreateSubscriptionError(Exception):
	def __init__(self, status_code):
		"""
		This exception is called if a subscription for a datamodel cannot be created
		:param str url: the URL of the subscription
		"""
		message = 'Orion request subscription failed. Code error: %s' %status_code
		super(CreateSubscriptionError, self).__init__(message)

class DeleteSubscriptionError(Exception):
	def __init__(self, data_model, url, msg=None):
		"""
		This exception is called if a subscription for a datamodel cannot be deleted
		:param str url: the URL of the subscription
		"""
		message = 'Error trying to delete a %s subscription at %s' %(data_model, url)
		message = '%s. %s'%(message, msg) if msg else message
		super(DeleteSubscriptionError, self).__init__(message)

class NotValidHost(Exception):
	def __init__(self, type_host, host):
		"""
		This exception is called when an invalid host and type host are given
		:param str type_host: type host
		:param str host: name of the host
		"""
		message = 'Not valid %s host: %s' %(type_host, host if host else 'empty host')
		super(NotValidHost, self).__init__(message)

class DataModelNotIntegrated(Exception):
	def __init__(self, datamodel):
		"""
		This exception is called when attempting to modify or delete
		a datamodel that has not been previosuly implemented
		:param str datamodel: the name of a datamodel
		"""
		message = 'The %s Data Model has not been previously integrated' %(datamodel)
		super(DataModelNotIntegrated, self).__init__(message)

class FieldNotInformed(Exception):
	def __init__(self, key, section):
		"""
		This exception is called when attempting to integrate
		a datamodel not included in the configuration file
		:param str datamodel: the name of a datamodel
		"""
		message = '“%s” key is not informed in "%s" section' %(key, section)
		super(FieldNotInformed, self).__init__(message)

class DataModelNotPresent(Exception):
	def __init__(self, datamodel):
		"""
		This exception is called when attempting to integrate
		a datamodel not included in the configuration file
		:param str datamodel: the name of a datamodel
		"""
		message = 'There is no %s section in the configuration file' %(datamodel)
		super(DataModelNotPresent, self).__init__(message)
