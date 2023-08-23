#include <iostream>

using namespace std;

int main()
{

    string str="qmnjvsanvwewcflctvprjtjtvvplvlfvxjavqildhcxmlnvcnacyclpafcgytvfvwfvwgqyppqqpqcsywsqrxqmnjvafycgvtlvhfcwtylaeuqfvxjatkbvcqnsqslhfavawnccveasfuqbqvqtcyllrqrxxwacfypsdcuqfavrqcgefqpyattracxwvtaawwddveasflcbqvdtrawmvupqquwxdecgqcwtyqyaflvlqsyqklhqsnafqvmllhvqpawrnqgvfusrecwawyqpfnwgawdgf";


    // string str="breakerofthiscodewillbeblessedbythesqueakyspiritresidingintheholegoaheadandfindawayofbreakingthespellonhimcastbytheevil?affarthespiritofthecavemanisalwayswithyoufindthemagicwandthatwillletyououtofthecavesitwouldmakeyouamagiciannolessthan?affartogothroughspeakthepassword"
   ; int j=0;
    
    for(int i=0; i<str.length();i++){
        j++;
        cout<<str[i];
        if(j==5){
            cout<<" ";
            j=0;
            
        }
    }

    return 0;
}