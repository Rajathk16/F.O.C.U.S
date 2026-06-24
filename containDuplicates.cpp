class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for(int i = 0; i < nums.size(); i++) {
            if(s.find(nums[i]) != s.end()) {
                return true;
            }
            s.insert(nums[i]);
        }
        return false;
    }
};
//tried with brute force approach but while submitting it gave 70/77 testcase passed with time limited error so went to unordered thing ....
