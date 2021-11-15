from setuptools import find_packages, setup

setup(
    name="cloudflare-request-header-plugin",
    version="1.0.0",
    description="Custom Cloudflare request header plugin for MLflow",
    author="Xinyu Lim",
    author_email="xinyu.lim@foodpanda.com",
    url="https://github.com/xlim7/cloudflare-request-header-plugin",
    license="MIT",
    packages=find_packages(),
    install_requires=["mlflow"],
    entry_points={
        "mlflow.request_header_provider": (
            "unused=cloudflare_request_header_plugin."
            "cloudflare_request_header_provider:CloudflareRequestHeaderProvider"
        ),
    },
)
