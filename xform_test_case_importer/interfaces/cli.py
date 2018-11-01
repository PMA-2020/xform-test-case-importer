#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command Line Interface."""
from argparse import ArgumentParser
from sys import stderr

from xform_test_case_importer.definitions.error import XFormTestImporterErr
from xform_test_case_importer.xform_test_case_importer import run


def get_parser():
    """Add required fields to parser.

    Returns:
        ArgumentParser: Argeparse object.
    """
    package_description = 'XFormTest Case Importer allows you to autopopulate'\
                          'portions of XFormTest-spec test cases in your' \
                          'XLSForms by allowing you to utilize real form' \
                          'submissions data from similar forms that may have' \
                          'existed in the past.'
    parser = ArgumentParser(description=package_description)

    xlsforms_help = 'Target XLSForms where there will be XFormTest-spec test '\
                    'cases. By this, we mean test cases as specifiedin the ' \
                    'XFormTest documentation: http://xform-test.pma2020.org'
    parser.add_argument('-x', '--xlsforms', nargs='+', help=xlsforms_help)

    submissions_help = 'A submissions data CSV file. By "submissions" data, ' \
                       'we mean the type of CSV dataset file that you would' \
                       'see when exporting submissions from ODK Aggregate '\
                       'or downloading them using ODK Briefcase.'
    parser.add_argument('-s', '--submissions', nargs='+',
                        help=submissions_help)

    return parser


def cli():
    """Command line interface for package.

    Side Effects: Executes program.

    Command Syntax:

    Examples:

    """
    parser = get_parser()
    args = parser.parse_args()

    try:
        run()
    except XFormTestImporterErr as err:
        err = 'An error occurred.\n\n' + str(err)
        print(err, file=stderr)


if __name__ == '__main__':
    cli()
