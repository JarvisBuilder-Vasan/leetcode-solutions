class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i=1
        while(i<len(words)):
                sort=sorted(words[i])
                other=sorted(words[i-1])
                new1="".join(sort)
                new2="".join(other)
                if new1==new2:
                    del(words[i])
                else:
                    i+=1

        return words

    
