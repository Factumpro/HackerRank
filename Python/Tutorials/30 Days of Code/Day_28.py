#!/usr/bin/env python3

import re

if __name__ == '__main__':
    pattern = r'@gmail\.com$'
    regexp = re.compile(pattern)
    gmail_names = []
    for _ in range(int(input())):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if regexp.search(emailID) is not None:
            gmail_names.append(firstName)
    [print(name) for name in sorted(gmail_names)]
