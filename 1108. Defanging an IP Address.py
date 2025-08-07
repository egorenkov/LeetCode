class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return "".join(["[.]" if s == "." else s for s in address])
