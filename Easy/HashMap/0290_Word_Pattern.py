class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping={}
        reverse={}
        words=s.split()
        if len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]]!=words[i]:
                    return False
            else:
                if words[i] in reverse:
                    return False
                mapping[pattern[i]]=words[i]
                reverse[words[i]]=pattern[i]
        return True
