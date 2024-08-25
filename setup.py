from setuptools import setup, find_packages

setup(
    name='num2wordsnepalihindi',
    version='0.4.1',
    description='Number to Hindi/Nepali words conversion',
    url='https://github.com/AarushThapa/number-to-words-nepali-hindi',
    author='Aarush Thapa',
    author_email='contact@aarushthapa.com.np',
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='number words conversion, nepali, hindi, nepali number to words, hindi words to number, nepali words to number, hindi number to words',
    install_requires=[],
)
