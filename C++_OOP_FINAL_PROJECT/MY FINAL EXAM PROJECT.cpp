#include <iostream>
#include <cstring>

using namespace std;

// Applicant structure
struct Applicant {
    char vin[17];
    int age;
    char vehicleType[10];
};

// Bracket structure
struct Bracket {
    float minAge;
    float maxAge;
    float premium;
};

// Abstract base class
class PremiumManager {
protected:
    Bracket* brackets = NULL;  // Changed from nullptr to NULL
    int bracketCount = 0;

public:
    virtual ~PremiumManager() {
        delete[] brackets;
    }

    void addBracket(const Bracket& b) {
        Bracket* newBrackets = new Bracket[bracketCount + 1];
        for (int i = 0; i < bracketCount; ++i) {
            newBrackets[i] = brackets[i];
        }
        newBrackets[bracketCount] = b;

        delete[] brackets;
        brackets = newBrackets;
        ++bracketCount;
    }

    void removeBracket(int index) {
        if (index < 0 || index >= bracketCount) return;

        Bracket* newBrackets = new Bracket[bracketCount - 1];
        for (int i = 0, j = 0; i < bracketCount; ++i) {
            if (i != index) {
                newBrackets[j++] = brackets[i];
            }
        }

        delete[] brackets;
        brackets = newBrackets;
        --bracketCount;
    }

    virtual float calculate(const Applicant* applicant) = 0;
};

// Liability Manager
class LiabilityManager : public PremiumManager {
public:
    float calculate(const Applicant* applicant) override {
        for (Bracket* b = brackets; b < brackets + bracketCount; ++b) {
            if (applicant->age >= b->minAge && applicant->age <= b->maxAge) {
                return b->premium;
            }
        }
        return 0.0f; // Default if no bracket found
    }
};

// Comprehensive Manager
class ComprehensiveManager : public PremiumManager {
public:
    float calculate(const Applicant* applicant) override {
        for (Bracket* b = brackets; b < brackets + bracketCount; ++b) {
            if (applicant->age >= b->minAge && applicant->age <= b->maxAge) {
                return b->premium * 1.2f; // Example adjustment
            }
        }
        return 0.0f;
    }
};

//  Example usage
int main() {
    PremiumManager** managers = new PremiumManager*[2];
    managers[0] = new LiabilityManager();
    managers[1] = new ComprehensiveManager();

    // Add some brackets
    Bracket b1 = { 18, 25, 500 };
    Bracket b2 = { 26, 40, 300 };
    Bracket b3 = { 41, 65, 200 }; 
    
    managers[0]->addBracket(b1);
    managers[0]->addBracket(b2);
    managers[0]->addBracket(b3);

    managers[1]->addBracket(b1);
    managers[1]->addBracket(b2);
    managers[1]->addBracket(b3);

    // Get applicant input from user
    Applicant applicant;

    cout << "Enter applicant's Vehicle Identity Number ";
    cin >> applicant.vin;

    cout << "Enter applicant's age: ";
    cin >> applicant.age;

    cout << "Enter applicant's vehicle type: ";
    cin >> applicant.vehicleType;

    // Calculate premiums
    for (int i = 0; i < 2; ++i) {
        float premium = managers[i]->calculate(&applicant);
        cout << "Manager " << i << " premium: $" << premium << endl;
    }
    
	// Clean up
    delete managers[0];
    delete managers[1];
    delete[] managers;

    return 0;
}

