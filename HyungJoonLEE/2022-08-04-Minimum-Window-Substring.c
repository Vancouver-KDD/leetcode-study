#include <limits.h>
#include "common.h"

#define LEN  128
char* minWindow(char* s, char* t)
{
    int counter[LEN] = {0};
    int start=0, end=0, tLen=strlen(t), sLen=strlen(s);
    int minStart=0, minLen=INT_MAX;
    for(int i = 0; i < LEN; i++) counter[i] = -sLen; //distinguish the letter in and not in t;
    for(int i = 0; t[i]; i++) counter[t[i]] = 0;
    for(int i = 0; t[i]; i++) counter[t[i]]++;
    while(end < sLen)
    {
        if(counter[s[end]]-- > 0) tLen--;
        end++; //move to the next character;
        while(tLen == 0) //a valid substring;
        {
            if(end-start < minLen) //collect the minimal only;
                minStart=start, minLen=end-start;
            counter[s[start]]++;
            if(counter[s[start]] > 0) tLen++; //if s[start] is in t;
            start++; //move forward by ignoring s[start];
        }
    }
    if(minLen != INT_MAX)
    {
        char* t = (char*)malloc(sizeof(char)*(minLen+1));
        *t = '\0';
        strncat(t, s+minStart, minLen);
        return t;
    }
    return "";
}