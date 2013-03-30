try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

long_desc = """
	This tool allows you to convert CSVs into a format appropriate for Ledger. It's particularly useful when you need to specify multipart transactions.
"""


setup(name="csvToLedger",
      version=1.0,
      description="Basic python script to convert CSVs to Ledger format",
      author="Ben Smith",
      author_email="ben@wbpsystems.com",
      url="https://github.com/tazzben/csvToLedger",
      license="MIT",
      packages=[],
      scripts=['csvToLedger'],
      package_dir={},
      long_description=long_desc,
      classifiers=[
          'Topic :: Text Processing',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop'
      ]
     )