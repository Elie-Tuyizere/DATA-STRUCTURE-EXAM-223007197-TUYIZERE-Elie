# My project question 
## Question 104
Insurance Premium Manager
Description: Calculate insurance premiums using a dynamic bracket array; multiple 
premium managers share a base interface.
Tasks:

• Define struct Applicant { char vin[17]; int age; char 
vehicleType[10]; }; and struct Bracket { float minAge, 
maxAge, premium; }; allocate Bracket* brackets dynamically.

• Create an abstract class PremiumManager with virtual float 
calculate(const Applicant*) = 0;, then derive LiabilityManager
: PremiumManager and ComprehensiveManager : PremiumManager
to demonstrate inheritance and polymorphism.

• Store PremiumManager* in a dynamic PremiumManager** managers; 
calling managers[i]->calculate(applicant) dispatches correctly.

• Use pointer arithmetic on brackets to find the matching premium.

• Implement addBracket(Bracket) and removeBracket(int index) by 
resizing Bracket*.
# Screenshot of output of my project
![image](https://github.com/user-attachments/assets/7331dc7b-b8f3-4270-a810-8b83dd3e5ac1)
