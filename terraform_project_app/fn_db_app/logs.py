import os
import logging

from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)
conn = os.environ['APPLICATIONINSIGHTS_CONNECTION_STRING']
logger.addHandler(AzureLogHandler(connection_string=conn))
