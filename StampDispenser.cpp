
#include <stdlib.h>
#include <assert.h>

/// <summary>
/// Facilitates dispensing stamps for a postage stamp machine.
/// </summary>
class StampDispenser
{
    
public:

    int* stampD;
    size_t numStampD;

    /// <summary>
    /// Initializes a new instance of the <see cref="StampDispenser"/> 
    /// class that will be able to dispense the given types of stamps.
    /// </summary>
    /// <param name="stampDenominations">
    /// The values of the types of stamps that the machine has.  
    /// Should be sorted in descending order and contain at least a 1.
    /// </param>
    /// <param name="numStampDenominations">
    /// The number of types of stamps in the stampDenominations array. 
    /// </param>
    StampDispenser(const int* stampDenominations, size_t numStampDenominations);
    
    /// <summary>
    /// Returns the minimum number of stamps that the machine can dispense to
    /// fill the given request.
    /// </summary>
    /// <param name="request">
    /// The total value of the stamps to be dispensed.
    /// </param>
    /// <returns>
    /// The minimum number of stamps needed to fill the given request.
    /// </returns>
    int CalcNumStampsToFillRequest(int request);

    /// <summary>
    /// Updates the currentRequestList array with values for the currentRequest
    /// fill the given request.
    /// </summary>
    /// <param name="currentRequestList">
    /// List of all the values that we have found for the optimal stamps
    /// where the indecies are the request value and the value there is the 
    /// optimal number of stamps to return
    /// </param>
    /// <returns>
    /// <param name="request">
    /// Current value of the request that we are calculating
    /// </param>
    void FillRequestHelper(int* currentRequestList, int currentRequest);
    
    /// <summary>
    /// Destructor for dynamically allocated array
    /// </summary>
    ~StampDispenser(); 



}; 


StampDispenser::StampDispenser(const int* stampDenominations, 
    size_t numStampDenominations):stampD(new int[numStampDenominations]), 
    numStampD(numStampDenominations){

    int i;
    // Initialize dynamically allocated array
    for (i = 0; i < numStampDenominations; i++){
        stampD[i] = stampDenominations[i];
    }
}

void StampDispenser::FillRequestHelper(int* currentRequestList, 
    int currentRequest) {
        // Variable to hold the current best option 
        // (Initialized to the largest int and should be reduced 
        // to a smaller value after iterations)
        size_t bestOption = (size_t) -1;
        int i;
        int difference;
        int currentNum;
        for (i = 0; i < this->numStampD; i++){
            if (currentRequest == 0){
                bestOption = 0;
            }
            else if (this->stampD[i] <= currentRequest){
                difference = currentRequest - this->stampD[i];
                currentNum = currentRequestList[difference] + 1;
                if (currentNum < bestOption){
                    bestOption = currentNum;
                }
            }
        }
        currentRequestList[currentRequest] = bestOption;
        
}

int StampDispenser::CalcNumStampsToFillRequest(int request){
        // Declare array for holding requests 
        int optimizedRequests[request + 1];
        int i;
        for (i = 0; i <= request; i ++){
            this->FillRequestHelper(optimizedRequests, i);
        }
        return optimizedRequests[request]; 
}

StampDispenser::~StampDispenser(){
    // Deallocated dynamically allocated array
    delete[] stampD;
}

int main()
{
    int stampDenominations[] = {90, 30, 24, 10, 6, 2, 1};
    StampDispenser stampDispenser(stampDenominations, 7);
    assert(stampDispenser.CalcNumStampsToFillRequest(18) == 3);

    return 0;
}
