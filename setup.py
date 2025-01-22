import setuptools


__version__ = "0.0.0"

REPO_NAME = "ml_customer_segmentation"
AUTHOR_USER_NAME = "Radhika5062"
SRC_REPO = "customer_segmentation"
AUTHOR_EMAIL = "radhikamaheshwari26@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "Python package for customer segmentation",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)
