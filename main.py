#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

""" See https://github.com/GoogleCloudPlatform/professional-services/blob/master/examples/dataflow-python-examples/batch-examples/README.md """

# pytype: skip-file

from __future__ import absolute_import

import argparse
import logging
import re

from past.builtins import unicode

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

g_schema = {
    'fields': [{
        'name': 'SiteName', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'OrgID', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'Company', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'Shares', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'AllocationPct', 'type': 'DECIMAL', 'mode': 'NULLABLE'
    }, {
        'name': 'InitialCapacity', 'type': 'INT64', 'mode': 'NULLABLE'
    }, {
        'name': 'ExpectedElectricityCertCapacity', 'type': 'INT64', 'mode': 'NULLABLE'
    }, {
        'name': 'InstalledCapacity', 'type': 'DECIMAL', 'mode': 'NULLABLE'
    }, {
        'name': 'EnergySource', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'SiteType', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'PowerGridRegion', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'PowerGridAreaID', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'ExpiryDate', 'type': 'DATE', 'mode': 'NULLABLE'
    }, {
        'name': 'StartDatePeriod', 'type': 'STRING', 'mode': 'NULLABLE'
    }]}
""",, {
        'name': 'LastCol', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'Decision', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'NumOfUnits', 'type': 'INT64', 'mode': 'NULLABLE'
    }, {
        'name': 'Town', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'City', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'County', 'type': 'STRING', 'mode': 'NULLABLE'
    }, {
        'name': 'Watercourses', 'type': 'STRING', 'mode': 'NULLABLE'
    }]
}"""


class DataIngestion:
    """A helper class which contains the logic to translate the file into
    a format BigQuery will accept."""

    def parse_method(self, string_input):
        """This method translates a single line of comma separated values to a
        dictionary which can be loaded into BigQuery.
        Args:
            string_input: A comma separated list of values in the form of
                state_abbreviation,gender,year,name,count_of_babies,dataset_created_date
                Example string_input: KS,F,1923,Dorothy,654,11/28/2016
        Returns:
            A dict mapping BigQuery column names as keys to the corresponding value
            parsed from string_input. In this example, the data is not transformed, and
            remains in the same format as the CSV.
            example output:
            {
                'state': 'KS',
                'gender': 'F',
                'year': '1923',
                'name': 'Dorothy',
                'number': '654',
                'created_date': '11/28/2016'
            }
         """
        logging.info("DataIngestion.parse_method(...) started")
        data_schema = {
            'fields': [{
                'name': 'SiteName', 'type': 'STRING', 'mode': 'NULLABLE'
            }, {
                'name': 'OrgID', 'type': 'STRING', 'mode': 'NULLABLE'
            }, {
                'name': 'Company', 'type': 'STRING', 'mode': 'NULLABLE'
            }, {
                'name': 'Shares', 'type': 'STRING', 'mode': 'NULLABLE'
            }, {
                'name': 'AllocationPct', 'type': 'DECIMAL', 'mode': 'NULLABLE'
            }, {
                'name': 'InitialCapacity', 'type': 'INT64', 'mode': 'NULLABLE'
            }, {
                'name': 'ExpectedElectricityCertCapacity', 'type': 'INT64', 'mode': 'NULLABLE'
            }, {
                'name': 'InstalledCapacity', 'type': 'DECIMAL', 'mode': 'NULLABLE'
            }, {
                'name': 'EnergySource', 'type': 'STRING', 'mode': 'NULLABLE'
            }, {
                'name': 'SiteType', 'type': 'STRING', 'mode': 'NULLABLE'
            }, {
                'name': 'PowerGridRegion', 'type': 'STRING', 'mode': 'NULLABLE'
            }, {
                'name': 'PowerGridAreaID', 'type': 'STRING', 'mode': 'NULLABLE'
            }, {
                'name': 'ExpiryDate', 'type': 'DATE', 'mode': 'NULLABLE'
            }, {
                'name': 'StartDatePeriod', 'type': 'STRING', 'mode': 'NULLABLE'
            }]}
        """, {
            'name': 'LastCol', 'type': 'STRING', 'mode': 'NULLABLE'
        }, {
            'name': 'Decision', 'type': 'STRING', 'mode': 'NULLABLE'
        }, {
            'name': 'NumOfUnits', 'type': 'INT64', 'mode': 'NULLABLE'
        }, {
            'name': 'Town', 'type': 'STRING', 'mode': 'NULLABLE'
        }, {
            'name': 'City', 'type': 'STRING', 'mode': 'NULLABLE'
        }, {
            'name': 'County', 'type': 'STRING', 'mode': 'NULLABLE'
        }, {
            'name': 'Watercourses', 'type': 'STRING', 'mode': 'NULLABLE'
        }]
        }"""

        # Strip out carriage return, newline and quote characters.
        values = re.split(",", re.sub('\r\n', '', re.sub('"', '',
                                                         string_input)))
        cols = []
        scehma_fields = data_schema['fields']
        for x in scehma_fields: cols.append(x['name'])
        row = dict(
            zip(cols,
                values))
        logging.info("DataIngestion.parse_method(...): {}".format(row))
        return row


class WordExtractingDoFn(beam.DoFn):
    """Parse each line of input text into words."""

    def process(self, element):
        """Returns an iterator over the words of this element.

        The element is a line of text.  If the line is blank, note that, too.

        Args:
          element: the element being processed

        Returns:
          The processed element.
        """
        return re.findall(r'[\w\']+', element, re.UNICODE)


def run(argv=None, save_main_session=True):
    """Main entry point; defines and runs the wordcount pipeline."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        default='gs://dataflow-sample',
        help='Input file to process.')
    parser.add_argument(
        '--output',
        dest='output',
        required=True,
        help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    # We use the save_main_session option because one or more DoFn's in this
    # workflow rely on global context (e.g., a module imported at module level).
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session

    data_ingestion = DataIngestion()

    p = beam.Pipeline(options=PipelineOptions(pipeline_args))

    (p

     | 'Read from a File' >> beam.io.ReadFromText(known_args.input, skip_header_lines=1)
     | 'String To BigQuery Row' >> beam.Map(lambda s: data_ingestion.parse_method(s))
     | 'Write to BigQuery' >> beam.io.Write(
                # beam.io.BigQuerySink(
                beam.io.WriteToBigQuery(
                    known_args.output,
                    schema=g_schema,
                    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                    # Deletes all data in the BigQuery table before writing.
                    write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE)))
    p.run().wait_until_finish()



if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
