'''
165. Compare Version Numbers

https://leetcode.com/problems/compare-version-numbers/

Compare two version numbers version1 and version2.
If version1 > version2 return 1;
if version1 < version2 return -1;
otherwise return 0.

You may assume that the version strings are:
non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0.

For example,
version number 3.4 has a revision number of 3 and 4 for its first and second level revision number.
Its third and fourth level revision number are both 0.



Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

Example 4:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”

Example 5:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number,
which means its third level revision number is default to "0"


Note:

Version strings are composed of numeric strings separated by dots .
and this numeric strings may have leading zeroes.
Version strings do not start or end with dots,
and they will not be two consecutive dots.
'''


def compareVersion(self, version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    # 学学
    version1 = [int(val) for val in version1.split(".")]
    version2 = [int(val) for val in version2.split(".")]

    if len(version1) > len(version2):
        min_version = version2
        max_version = version1
    else:
        min_version = version1
        max_version = version2

    # Compare up to min character
    for i in range(len(min_version)):
        if version1[i] > version2[i]:
            return 1
        elif version1[i] < version2[i]:
            return -1

    if len(version1) == len(version2):
        return 0

    for j in range(i + 1, len(max_version)):
        if max_version[j] > 0:
            return 1 if max_version == version1 else - 1
    return 0

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split('.')
        s2 = version2.split('.')

        # Ailgning them
        if len(s1) >= len(s2):
            s2.extend('0' * (len(s1) - len(s2)))
        else:
            s1.extend('0' * (len(s2) - len(s1)))

        c = [int(s1[i]) - int(s2[i]) for i in range(len(s1))]
        for item in c:
            if item < 0:
                return -1
            elif item > 0:
                return 1
        return 0

# refernece:
# https://leetcode.com/problems/compare-version-numbers/discuss/311157/Python-Easy-to-Understand-O(n)
# https://leetcode.com/problems/compare-version-numbers/discuss/51008/Concise-Python-code



