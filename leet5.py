class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # word_value = {}
        letter_count = Counter(letters)
        def backtrack(index, letter_count, current_sum):
            print(index, current_sum, "=========>")
            if index == len(words):
                print('+++++++++++++++++')
                self.ans = max(self.ans, current_sum)
                return
            current_word = words[index]
            temp = letter_count.copy()
            current_word_sum = 0
            valid = True
            print(current_word)
            for c in current_word:
                if letter_count[c] ==0:
                    print('invalid')
                    valid = False
                    break
                current_word_sum += score[ord(c) - 97]
                letter_count[c] -=1
            if valid:
                print('valid')
                backtrack(index+1, letter_count, current_sum + current_word_sum)
            letter_count = temp.copy()
            backtrack(index+1, letter_count, current_sum)

        self.ans = 0
        backtrack(0, letter_count, 0)
        return self.ans
        
            
        # for w in words:
        #     wv=0
        #     for l in w:
        #         wv += score[alphabet[l]]
        #     word_value[w]=wv
        # print(word_value)
        # possibilities = {}
        # temp = letters
        
        # print(letterss)            



            
                
