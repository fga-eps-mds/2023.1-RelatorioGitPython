from setuptools import setup

from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='pyGitInfo',
    version='0.0.5',
    license='MIT License',
    author=['Catlen Cleane', 'Felipe Direito', 'Gabriel Rosa', 'Gabriel Zaranza', 'Rafael Kenji', 'Lucas Lobão', 'Vinicius de Oliveira'],
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='catlen.cleane@hotmail.com, fedireito92@gmail.com, gabriel10919@outlook.com, gabrielzaranza@hotmail.com, rafak.taira@gmail.com, lucaslobao14df@gmail.com, viniciusoliveirasp22@gmail.com',
    keywords=["gitInfo", "github", "git", "relatorio", "reports", "gitReports"],
    description=u'Analisador de repositórios do github',
    packages=['pyGitInfo'],
    install_requires=["pandas>=1.4.0", "matplotlib", "pygithub"],)
