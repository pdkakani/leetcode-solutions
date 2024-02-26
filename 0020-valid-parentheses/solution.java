class Solution {
    public boolean isValid(String s) {

        var input = s.toCharArray();
        Stack<Character> myStack = new Stack<>();
        for (char c: input) {
            if (c == '(' ) {
                myStack.push(')');
            } else if (c == '{') {
                myStack.push('}');
            } else if(c == '[') {
                myStack.push(']');
            }
            if(c == ')' || c == '}' || c == ']') {
                if (myStack.isEmpty()) {
                    return false;
                }
                var topChar = myStack.pop();
                if (topChar != c) {
                    return false;
                }
            }
        }
        return myStack.isEmpty();
    }
}
