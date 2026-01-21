import logging

# Configure logging to track lookups and potential matches
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Using a frozenset for immutability and O(1) average lookup performance.
# In production, replace with a Redis Bloom Filter or a Trie structure.
MALWARE_DATABASE = frozenset(
    {
        "malware.com/bad-file.exe",
        "evil-site.net/phishing/login.html",
        "unsafe.biz:8080/virus",
        "mypagina.com",
    }
)


def is_url_malicious(hostname: str, path: str) -> bool:
    """
    Evaluates if a given URL is malicious based on prefix-matching.
    """
    # Normalization: Clean slashes and convert to lowercase
    clean_hostname = hostname.strip("/").lower()
    clean_path = path.strip("/").lower()

    # URL Construction: Join parts ensuring a consistent format
    full_url = f"{clean_hostname}/{clean_path}" if clean_path else clean_hostname

    # Prefix Matching: Check if URL starts with any blacklisted entry.
    # Note: For high-volume (1M+), a Trie would be more efficient.
    for malware_prefix in MALWARE_DATABASE:
        if full_url.startswith(malware_prefix.lower()):
            logger.warning(f"Malware detected: {full_url}")
            return True

    logger.info(f"URL allowed: {full_url}")
    return False
