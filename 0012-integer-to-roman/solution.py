class Solution:
        def intToRoman(self, num: int) -> str:
            result = []
            romans = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
            
            # # starting with 1, units place
            # mult = 1
            
            # mynum = num

            # while mynum > 0:
            #     temp = (mynum % 10) * mult

            #     while temp > 0:

            #         if temp in romans:
            #             result.append(romans[temp])
            #             temp = 0
            #         else:
            #             if mult in romans:
            #                 result.append(romans[mult])
            #             temp -= mult

            #     mynum = mynum // 10
            #     mult *= 10

            # return "".join(reversed(result))

            for val in romans.keys():
                while num > 0 and num >= val:
                    result.append(romans[val] * (num//val))
                    num %= val
            return "".join(result)
                        
                

        
