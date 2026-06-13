class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')
        
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # land first, then water
                land_end = landStartTime[i] + landDuration[i]
                water_start = max(land_end, waterStartTime[j])
                finish1 = water_start + waterDuration[j]
                
                # water first, then land
                water_end = waterStartTime[j] + waterDuration[j]
                land_start = max(water_end, landStartTime[i])
                finish2 = land_start + landDuration[i]
                
                ans = min(ans, finish1, finish2)
        
        return ans