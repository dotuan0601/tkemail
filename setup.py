from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='tkmail',
    version='0.1.1',
    description='Send email with smtp setup',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Tuandv',
    author_email='tuan.dv@teko.vn',
    keywords=['email', 'Email', 'SendEmail', 'Send Email', 'send email'],
    url='',
    download_url='https://pypi.org/project/tkmail/'
)

install_requires = []

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)