import os
import requests

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
    "X-GitHub-Api-Version": "2022-11-28",
}

owner = "darlinghq"
repo = "darling"
base = "https://api.github.com"
route = "/repos/{owner}/{repo}/actions/artifacts"
url = base + route.format(owner=owner, repo=repo)

params = { "per_page": 1, "name": "debs" }

response = requests.get(url, params=params, headers=headers)
result = response.json()
latest_artifact = result['artifacts'][0]

download_url = latest_artifact['archive_download_url']
commit = latest_artifact['head_sha']

template = """# Maintainer: Elena Krittik <elenakrittik@gmail.com>

pkgname=darling-edge-bin
pkgver={commit}
pkgrel={pkgrel}
pkgdesc="Darwin/MacOS emulation layer for Linux"
arch=("x86_64")
url="https://github.com/darlinghq/darling"
license=("GPL")

"""