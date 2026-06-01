class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "#" + s
        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        out, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # get j to ind of #
            # length is last ind of prev word to ind of #
            length = int(s[i:j])
            # j+1 -> ind of first letter of next word
            out.append(s[j+1:j+1+length])
            # i to index of last letter of word 
            i = j + 1 + length

        return out