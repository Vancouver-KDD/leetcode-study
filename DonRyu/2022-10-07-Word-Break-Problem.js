const wordBreak =(str, wordDict)=>{
    if (!wordDict || wordDict.length === 0) return false
    for(let i=0; I<wordDict.length; i++){
        const dictIndex = str.indexOf(wordDict[i])
        if(dictIndex === -1){
            return false
        }
    }
    return true
}
