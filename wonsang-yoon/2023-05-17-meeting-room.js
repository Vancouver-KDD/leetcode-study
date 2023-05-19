let meetings = [[9, 19],[0,5],[10,15],[30,40]];

for(let i = 0; i < meetings.length; i++){
    let start = meetings[i][0];
    let end = meetings[i][1];
    for(let y = i + 1; y < meetings.length; y++){
        let next_start = meetings[y][0];
        let next_end = meetings[y][1];
        if(end > next_start){
            return false;
        }
    }
}
return true