"""Config for tests."""
import os


PKG_NAME = 'xform_test_case_importer'
TEST_PACKAGES = [PKG_NAME, 'test']
TEST_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'
TEST_STATIC_DIR = TEST_DIR + 'static/'
