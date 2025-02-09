from setuptools import setup

setup(name="anekos.py",
      author="regulad",
      url="https://github.com/regulad/anekos.py",
      version="1.0.0",
      packages=["anekos"],
      install_requires=["aiohttp>=3.6.2"],
      license="MIT",
      description="An unofficial async wrapper for nekos.life API!",
      python_requires=">=3.6"
)
