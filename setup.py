from setuptools import setup, find_packages

setup(
    name="rune_agent",
    version="0.1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["rune-agent = rune_agent:main"]},  # Assumes a main() in your script
    description="Elder Futhark Rune Transliterater",
    author="Schon Kane",
)
