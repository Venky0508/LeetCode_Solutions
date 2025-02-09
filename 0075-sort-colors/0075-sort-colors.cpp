class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0};  // Initialize count array to 0
    
        // Count occurrences of 0, 1, and 2
        for (int i = 0; i < nums.size(); i++) {
            count[nums[i]]++;  
        }
        
        int index = 0;
        for (int j = 0; j < 3; j++) {
            int total = count[j];
            while (total > 0) {
                nums[index] = j;
                index++;
                total--;
            }
        }  
    }
};