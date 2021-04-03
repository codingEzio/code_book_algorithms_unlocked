# Status
#   solved by myself        : yes
#   submitted to leetcode   : yes


class Solution:
    """
    "1.1.1.1" -> "1[.]1[.]1[.]1"

    There aren't too many variations when it comes to solve this extremely
    simple problem. Either use the built-in methods, like `replace` and those
    regex methods, or replace the three `.` one by one.

    Related source code of the `replace` method
    https://github.com/python/cpython/blob/master/Objects/stringlib/replace.h
    """

    def defang_ipv4_address(self, address):
        return address.replace(".", "[.]", -1)
