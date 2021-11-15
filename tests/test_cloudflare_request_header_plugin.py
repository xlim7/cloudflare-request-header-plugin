import os

from cloudflare_request_header_plugin.cloudflare_request_header_provider import (
    CloudflareRequestHeaderProvider,
)


def test_cloudflare_request_header_provider_in_context():
    provider = CloudflareRequestHeaderProvider()
    in_context = provider.in_context()
    assert in_context


def test_cloudflare_request_header_provider_request_headers():
    os.environ["CF_ACCESS_TOKEN"] = "test_client_token"
    provider = CloudflareRequestHeaderProvider()
    request_headers = provider.request_headers()
    assert request_headers["cf-access-token"] == "test_client_token"
