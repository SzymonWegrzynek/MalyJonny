import hashlib
import sys


def zlam_hash(hash_format, wordlist, hash_1):
    if hash_format == md5:
        md5 = hashlib.md5(b"{i}").hexdigest()
    elif hash_format == sha3_512:
        sha3_512 = hashlib.sha3_512(b"{i}").hexdigest()
    elif hash_format == sha256:
        sha256 = hashlib.sha256(b"{i}").hexdigest()


if len(sys.argv) == 4:
    hash_format = sys.argv[1]
    wordlist = sys.argv[2]
    hash_1 = sys.argv[3]
    zlam_hash(hash_format, wordlist, hash_1)
else:
    print("Za malo arg")
