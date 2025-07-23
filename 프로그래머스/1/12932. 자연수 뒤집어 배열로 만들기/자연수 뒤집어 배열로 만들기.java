class Solution {
    public long[] solution(long n) {
        String str = String.valueOf(n);
        
        long[] answer = new long[str.length()];
        
        long num;
        for (int i = 0; i < str.length(); i++) {
            
            answer[i] = n % 10;
            n /= 10;
        }
        return answer;
    }
}