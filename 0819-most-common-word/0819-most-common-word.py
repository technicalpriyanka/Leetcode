class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols="!?',;."
        for ch in paragraph:
            if ch in paragraph:
                if ch in symbols:
                    paragraph = paragraph.replace(ch, " ")
                    
        paragraph = paragraph.lower().split()
        
        count=0
        freq_word = ""    
        for word in set(paragraph):
            if word not in banned and paragraph.count(word) > count:
                count = paragraph.count(word)
                freq_word=word
                
        return freq_word