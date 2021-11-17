def intToRoman(num: int) -> str:
        # include the cases 4, 9, 40, 90, 400, and 900 in dict along with reg values
	dict = {1: "I", 4: "IV", 5: "V", 9:"IX", 10: "X", 40:"XL", 50: "L", 90:"XC", 100: "C", 400:"CD", 500: "D" , 900:"CM",1000: "M"}
        rem = num
        finString = ""
        while not rem == 0:
            highest = 0
            for key in dict:
                if key <= rem:
                    highest = key
                else:
                  break
            if highest == 0:
              return
            rem = rem - highest 
            finString += dict[highest]
        return finString
                    
        
print(intToRoman(52)) # will return LII
