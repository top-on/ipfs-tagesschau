# ipfs_tagesschau

A python package to assist the upload of the latest [tagesschau.de](https://www.tagesschau.de) articles to [IPFS](https://ipfs.io/), the InterPlanetary File System.

This package downloads the RSS feed from tagesschau.de and generates are static website from it.
It is then easy to host this website on IPFS.
The website thus becomes hosted in one of the most robust and censor-resistant ways available.

## How to publish tagesschau.de feed to IPFS

1. Install and run IPFS, e.g. [go-ipfs](https://github.com/ipfs/go-ipfs#install) and [ipfs-desktop](https://github.com/ipfs/ipfs-desktop#install).

2. Run `scripts/tagesschau_to_ipfs.py` to download tagesschau.de articles to `build` folder.

3. Add `build` folder to Files section of [ipfs-desktop](https://docs.ipfs.io/how-to/websites-on-ipfs/single-page-website/#pinning-files). Your content should now hosted on IPFS. It's availability should broadcasted by IPFS's Distributed Hash Table.

4. Explore `build` folder in ipfs-desktop, to get content hash of `build/index.html`.

5. Test successful hosting with an IPFS Gateway, e.g. `https://cloudflare-ipfs.com/ipfs/<content_hash>`
