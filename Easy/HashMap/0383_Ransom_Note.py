class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom={}
        maga={}
        for i in range(len(ransomNote)):
            if ransomNote[i] in ransom:
                ransom[ransomNote[i]]+=1
            else:
                ransom[ransomNote[i]]=1

        for j in range(len(magazine)):
            if magazine[j] in maga:
                maga[magazine[j]]+=1
            else:
                maga[magazine[j]]=1

        for letter in ransom:
            if letter in maga:
                if ransom[letter]>maga[letter]:
                    return False
            else:
                return False
        return True
