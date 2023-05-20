class Solution {
    public static int romanToInt(String s) {
        Map<Character, Integer> roman = new HashMap();
        roman.put('I', 1);
        roman.put('V', 5);
        roman.put('X', 10);
        roman.put('L', 50);
        roman.put('C', 100);
        roman.put('D', 500);
        roman.put('M', 1000);

        s = s.replace("IV","IIII");
        s = s.replace("IX","VIIII");
        s = s.replace("XL","XXXX");
        s = s.replace("XC","LXXXX");
        s = s.replace("CD","CCCC");
        s = s.replace("CM","DCCCC");
        
        int result = 0;
        char[] stringArr = s.toCharArray();
        for (char c: stringArr) {
            result = roman.getOrDefault(c, 0) + result;
        }
        return result;
    }
}
