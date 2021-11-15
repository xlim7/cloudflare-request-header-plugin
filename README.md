## MLFlow Cloudflare Request Header plugin

This package provides a custom MLflow plugin that allows users to pass custom headers when authenticating to a MLflow server that is protected using Cloudflare Access.


### Implementation overview
* `cloudflare-request-header-plugin`: this package includes the `CloudflareRequestHeaderProvider` class that is used to specify the custom request header `cf-access-token` required for a user to authenticate to the MLflow server when using the MLflow Python API.
* `setup.py` file defines the entrypoint that tells MLflow to automatically register the custom request header provider to the registry when this package is installed. The entrypoint is configured as follows:

```
entry_points={
    "mlflow.request_header_provider": "unused=cloudflare_request_header_plugin.cloudflare_request_header_provider:CloudflareRequestHeaderProvider"
}
```

### Usage

Install this package using pip and then use MLflow as normal.

```bash
pip install -e cloudflare-request-header-plugin
```

The plugin expects Cloudflare Access credentials to be set in the `CF_ACCESS_TOKEN` environment variable on the client application.


### Useful references
- [Cloudflare access service tokens](https://blog.cloudflare.com/give-your-automated-services-credentials-with-access-service-tokens/)
- [MLflow custom plugins](https://www.mlflow.org/docs/latest/plugins.html#defining-a-plugin)
