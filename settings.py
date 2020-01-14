# Specifying data
CSV_SEP = ";"
NA_FILL = ""
EVAL_INDICATOR = 'ev:'
DEFAULT_SPECIFIER = '{{DEFAULT}}'
LOG_LOC = r'C:\data'
LOG_LEVEL = 'DEBUG'
ENV_DIR = 'env'
KEYVAULT_SYSTEM = 'Keepass'
DEFAULT_FILE_NAME = '{prefix}{type}{subtype}{datetime}{suffix}.{extension}'
DEFAULT_DATE_FORMAT = '%Y_%m_%d'
DEFAULT_TIME_FORMAT = '%H_%M'
DEFAULT_DATETIME_FORMAT = '%Y_%m_%d_%H_%M_%S'
EVIDENCE_ARCHIVE_NAME = 'testcase_{test_name}_(run_on_{datetime})'
DEFAULT_DATE_TIME_ORDER = ('year', 'month', 'day', 'hour', 'minute', 'second',)

""" The following section of settings cannot be changed after the framework has started, 
and thus can only be changed by altering this file. """

# Generic keyword settings
REQUIRED_KW_PROPERTIES = ('mandatory_variables', 'iterable', )

# About extended keywords
EXTENDED_KW_DIRECTORY = ('keywords',)

# About bare keywords
BARE_KW_DIRECTORY = ('',)

# About pom keywords
INCLUDE_POM = False
INCLUDE_POM_AS_KEYWORDS = False
POM_MODULES = ('system.pom',)
POM_KW_NAMING_CONVENTION = '({screen}) {action}'
POM_VALID_PREFIXES = ('get', 'assert', 'click', 'input', 'select')
POM_DEFAULT_KW_PROPERTIES = {'iterable': None}

# Location data
LIBRARY_MODULES = ('lib',)
SYSTEM_UNDER_TEST_MODULES = ('sys',)
