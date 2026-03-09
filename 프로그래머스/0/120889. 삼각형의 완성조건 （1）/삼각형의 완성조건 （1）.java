import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        
         Arrays.sort(sides);
        
        int sum = sides[0] + sides[1];
        
        return sum > sides[2] ? 1 : 2;
    }
}