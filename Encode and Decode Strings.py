class Codec:
    # CLEVER: a simple way to decode
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return "".join( "{}:{}".format(len(s), s) for s in strs )
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            j = s.index(":", i)
            i = j + int( s[i:j] ) + 1
            strs.append( s[j+1: i] )
        return strs
        

# Your Codec object will be instantiated and called as such:
strs = ["hello", "world"]
codec = Codec()
a = codec.decode(codec.encode(strs))
print(a)