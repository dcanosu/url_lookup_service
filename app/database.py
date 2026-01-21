# We store "hostname/path" strings here
# In a real app, this might be a Redis cache or a SQL database
MALWARE_DATABASE = {
    "malware.com/bad-file.exe",
    "evil-site.net/phishing/login.html",
    "unsafe.biz:8080/virus",
    "mypagina.com",
}


def is_url_malicious(hostname: str, path: str) -> bool:
    """
    Combines hostname and path to check against our known malware list.
    """
    # Standardize the lookup string
    # lookup_url = f"{hostname}/{path}"
    hostname = hostname.strip("/")
    path = path.strip("/")

    # full_url = f"{hostname}/{path}".strip("/")
    full_url = f"{hostname}/{path}" if path else hostname

    # Check if it exists in our set
    # return lookup_url in MALWARE_DATABASE
    # Search if any prefix of the DB match with the start of the url
    for malware_url in MALWARE_DATABASE:
        if full_url.startswith(malware_url):
            return True
    return False
