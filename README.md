## Dynamic IP Updater for Cloudflare DNS Records

A Python script to automate the process of updating Cloudflare DNS records with the current public IP address of your machine. This script periodically fetches the public IP from multiple sources and uses the Cloudflare API to update specified DNS records. Keep your Cloudflare DNS records accurate even if your IP changes dynamically.

### Features
- Automatically updates Cloudflare DNS records with your machine's current public IP.
- Supports multiple IP retrieval services to ensure reliability.
- Easily customizable to update different DNS records in your Cloudflare account.
- Schedule the script to run at specific intervals using the built-in `schedule` library.
- Ideal for maintaining access to services hosted on your dynamic IP without manual intervention.

